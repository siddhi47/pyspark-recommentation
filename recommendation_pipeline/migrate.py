import boto3
import os
import logging
from pymongo import MongoClient
import pandas as pd


def migrate_to_hdfs_from_s3(s3_bucket, s3_file, hdfs_path, spark, *args, **kwargs):
    """Migrate data from s3 to hdfs"""

    if "logger" in kwargs:
        logger = kwargs["logger"]
    else:
        logger = logging.getLogger(__name__)

    s3 = boto3.resource("s3")
    if not os.path.exists("tmp"):
        os.mkdir("tmp")
    logger.info("Downloading file from s3")
    s3.Bucket(s3_bucket).download_file(
        s3_file, "tmp/{}".format(os.path.basename(s3_file))
    )
    logger.info("Downloaded file from s3")
    logger.info("Uploading file to hdfs")
    df = spark.read.csv("tmp/{}".format(os.path.basename(s3_file)), header=True)
    try:
        df.write.mode("overwrite").csv(
            hdfs_path,
            header=True,
        )
        logger.info("Uploaded file to hdfs")
    except Exception as e:
        logger.error("Upload failed", e)


def migrate_to_mongo_from_s3(
    s3_bucket, s3_file, mongo_uri, mongo_db, mongo_collection, *args, **kwargs
):
    """Migrate data from s3 to mongodb"""

    if "logger" in kwargs:
        logger = kwargs["logger"]
    else:
        logger = logging.getLogger(__name__)

    s3 = boto3.resource("s3")
    if not os.path.exists("tmp"):
        os.mkdir("tmp")
    db = MongoClient(mongo_uri)[mongo_db]
    logger.info("Downloading file from s3")
    s3.Bucket(s3_bucket).download_file(
        s3_file, "tmp/{}".format(os.path.basename(s3_file))
    )
    logger.info("Downloaded file from s3")
    logger.info("Uploading file to mongodb")
    df = pd.read_csv("tmp/{}".format(os.path.basename(s3_file)), sep=";")

    if "Rating" in s3_file or "Book" in s3_file:
        df["ISBN"] = pd.to_numeric(df["ISBN"], errors="coerce")
        df.dropna(subset=["ISBN"], inplace=True)
        df["ISBN"] = df["ISBN"].astype(int)

    try:
        db[mongo_collection].drop()
        db[mongo_collection].insert_many(df.to_dict("records"))
        logger.info("Uploaded file to mongodb")
    except Exception as e:
        logger.error("Upload failed", e)
