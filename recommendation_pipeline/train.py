from pyspark.ml.recommendation import ALS
from pyspark.sql.types import *
import boto3



def preprocess(df): 
    """
        Preprocessing the data
    """
    ratings_df = (
        df.withColumn("User-ID", df["User-ID"].cast(IntegerType()))
        .withColumn("ISBN", df["ISBN"].cast(IntegerType()))
        .withColumn("Rating", df["Rating"].cast(IntegerType()))
        .na.drop()
    )
    return ratings_df


def train_ALS(
    dataframe, user_col, item_col, rating_col, rank, maxIter, regParam, alpha
):
    """
        Training the model using MLlib ALS (Altenative Least Square) algorithm
    """
    als = ALS(
        maxIter=maxIter,
        regParam=regParam,
        rank=rank,
        userCol=user_col,
        itemCol=item_col,
        ratingCol=rating_col,
        coldStartStrategy="drop",
        nonnegative=True,
        implicitPrefs=True,
        alpha=alpha,
    )
    model = als.fit(dataframe)
    return model


def compress_folder(folder):
    import shutil

    shutil.make_archive(folder, "zip", folder)

    return


def save_model_s3(model, bucket, key):
    """
        Saving the trained model to S3 cloud
    """
    model.write().overwrite().save("tmp/models/als")
    s3 = boto3.resource("s3")

    # compress the model file into zip
    compress_folder("tmp/models/als")

    # upload the zip file to s3
    s3.meta.client.upload_file("tmp/models/als.zip", bucket, key)

