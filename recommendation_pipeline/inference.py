import boto3


def download_model(bucket, key, local_path):
    s3 = boto3.resource("s3")
    s3.Bucket(bucket).download_file(key, local_path)
    return

def load_model(local_path):
    from pyspark.ml.recommendation import ALSModel
    model = ALSModel.load(local_path)
    return model

def get_recommendations_for_one_user(model, user_id, n):
    return model.recommendForAllUsers(n).where(f"id = {user_id}").collect()
