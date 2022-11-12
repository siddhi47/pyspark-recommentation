import boto3


def download_model(bucket, key, local_path):
    s3 = boto3.resource("s3")
    s3.Bucket(bucket).download_file(key, local_path)
    return


def load_model(local_path):
    from pyspark.ml.recommendation import ALSModel

    model = ALSModel.load(local_path)
    return model


def get_recommendations_for_all_users(model, n):
    return model.recommendForAllUsers(n).collect()

def get_recommendations_for_one_user(model, user_id, n):
    return model.recommendForAllUsers(n).where(f"id = {user_id}").collect()


def get_books_from_book_ids(book_ids, client, db_name, collection_name):
    """
    Get books from book_ids from mongodb
    """
    books = []
    book_ids = [str(book_id.ISBN).zfill(10) for book_id in book_ids[0][1]]
    for book_id in book_ids:
        book = client[db_name][collection_name].find_one({"ISBN": book_id})['Title']
        books.append(book)
    return books
