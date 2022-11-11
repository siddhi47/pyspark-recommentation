import boto3
import os
import logging
def migrate_to_hdfs_from_s3(s3_bucket, s3_file, hdfs_path, spark, *args, **kwargs):
    """Migrate data from s3 to hdfs"""

    if 'logger' in kwargs:
        logger = kwargs['logger']
    else:
        logger = logging.getLogger(__name__)

    s3 = boto3.resource('s3')
    if not os.path.exists('tmp'):
        os.mkdir('tmp')

    logger.info('Downloading file from s3')
    s3.Bucket(s3_bucket).download_file(s3_file, 'tmp/{}'.format(os.path.basename(s3_file)))
    logger.info('Downloaded file from s3')
    logger.info('Uploading file to hdfs')
    df = spark.read.csv('tmp/{}'.format(os.path.basename(s3_file)), header=True).write.csv(hdfs_path, header=True)

    df.write.mode('overwrite').csv(hdfs_path, header=True, )
    logger.info('Uploaded file to hdfs')


def migrate_to_mongo_from_s3(s3_bucket, s3_file, mongo_uri, mongo_db, mongo_collection, *args, **kwargs):
    """Migrate data from s3 to mongodb"""

    if 'logger' in kwargs:
        logger = kwargs['logger']
    else:
        logger = logging.getLogger(__name__)

    s3 = boto3.resource('s3')
    if not os.path.exists('tmp'):
        os.mkdir('tmp')

    logger.info('Downloading file from s3')
    s3.Bucket(s3_bucket).download_file(s3_file, 'tmp/{}'.format(os.path.basename(s3_file)))
    logger.info('Downloaded file from s3')
    logger.info('Uploading file to mongodb')
    df = pd.read_csv('tmp/{}'.format(os.path.basename(s3_file)))
    df.to_json(mongo_uri, mongo_db, mongo_collection)
    logger.info('Uploaded file to mongodb')
