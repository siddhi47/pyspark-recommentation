import boto3
from dotenv import load_dotenv
import os
from pyspark.sql import SparkSession
from pyspark import SparkConf
from argparse import ArgumentParser
from recommendation_pipeline.migrate import (
    migrate_to_hdfs_from_s3,
    migrate_to_mongo_from_s3,
)
from recommendation_pipeline.train import train_ALS, preprocess, save_model_s3
from recommendation_pipeline.inference import (
    download_model,
    load_model,
    get_recommendations_for_one_user,
    get_books_from_book_ids,
    get_recommendations_for_all_users,
)
from pymongo import MongoClient

def parse_args():
    parser = ArgumentParser()

    parser.add_argument(
        "-o",
        "--option",
        dest="option",
        choices=["migrate", "train", "predict"],
    )

    parser.add_argument(
        "-u",
        "--user_id",
        dest="user_id",
        type=int,
        default=17,
    )
    parser.add_argument(
        "-n",
        "--n",
        dest="n",
        type=int,
        default=10,
    )

    return parser.parse_args()


def migrate():
    load_dotenv()
    conf = SparkConf()

    spark = SparkSession.builder.config(conf=conf).getOrCreate()

    migrate_to_hdfs_from_s3(
        os.getenv("S3_BUCKET"),
        "book_recommendation_data_raw/Ratings.csv",
        "hdfs://localhost:9000/processed/Ratings.csv",
        spark,
    )
    migrate_to_mongo_from_s3(
        os.getenv("S3_BUCKET"),
        "book_recommendation_data_raw/Books.csv",
        os.getenv("MONGO_URL"),
        os.getenv("MONGO_DB"),
        os.getenv("MONGO_COLLECTION"),
    )


def train():
    load_dotenv()
    conf = SparkConf()
    spark = SparkSession.builder.config(conf=conf).getOrCreate()

    df = spark.read.csv(
        "hdfs://localhost:9000/processed/Ratings.csv", sep=";", header=True
    )
    df = preprocess(df)

    model = train_ALS(
        df,
        "User-ID",
        "ISBN",
        "Rating",
        10,
        10,
        0.01,
        40,
    )
    save_model_s3(model, os.getenv("S3_BUCKET"), "models/als_model")


def predict(user_id, n):
    load_dotenv()
    conf = SparkConf()
    #conf.set("spark.executor.memory", "10g")

    spark = SparkSession.builder.config(conf=conf).getOrCreate()
    download_model(os.getenv("S3_BUCKET"), "models/als_model", "tmp/models/als.zip")
    model = load_model("tmp/models/als")
    mongo_client = MongoClient(os.getenv("MONGO_URL"))
    book_list = get_recommendations_for_one_user(
        model,
        user_id,
        n,
    )
    books = get_books_from_book_ids(
        book_list,
        mongo_client,
        os.getenv("MONGO_DB"),
        os.getenv("MONGO_COLLECTION"),
    )

    return books


def main(args):
    if args.option == "migrate":
        migrate()
        migrate()
    elif args.option == "train":
        train()
    elif args.option == "predict":
        print(predict(args.user_id, args.n))
        print(predict(17, args.n))
        print(predict(18, args.n))


if __name__ == "__main__":
    main(parse_args())
