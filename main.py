import boto3
from dotenv import load_dotenv
import os
from pyspark.sql import SparkSession
from pyspark import SparkConf
from recommendation_pipeline.migrate import migrate_to_hdfs_from_s3

def main():
    load_dotenv()
    conf = SparkConf()
 
    spark = SparkSession.builder.config(
        conf=conf
            ).getOrCreate()
    
    migrate_to_hdfs_from_s3(
        os.getenv('S3_BUCKET'),
        'book_recommendation_data_raw/Books.csv',
        'hdfs://localhost:9000/processed/Books.csv',
        spark
    )
    #spark write to hdfs

if __name__ == "__main__":
    main()
