# flask app for mongo API
from flask import Flask, jsonify, request
import pymongo
import os
import logging
import json
import dotenv

dotenv.load_dotenv()
app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URL")
mongo = pymongo.MongoClient(app.config["MONGO_URI"])


@app.route("/api/v1/books_recommendation_for_user/<user_id>", methods=["GET"])
def get_books_for_user(user_id):
    try:
        books = mongo[os.getenv("MONGO_DB")][
            os.getenv("MONGO_COLLECTION_PREDICTIONS")
        ].find_one({"USER-ID": int(user_id)})

        authors = []
        for book in books["Books"]:
            author = mongo[os.getenv("MONGO_DB")][
                os.getenv("MONGO_COLLECTION")
            ].find_one({"Title": str(book)})
            authors.append(author["Author"])
        list_rec = []
        for b, a in zip(books["Books"], authors):
            list_rec.append({"Title": b, "Author": a})

        # get read books
        read_books = mongo[os.getenv("MONGO_DB")][
            os.getenv("MONGO_COLLECTION_RATINGS")
        ].find({"User-ID": int(user_id)})

        read_books = [x["ISBN"] for x in read_books]
        # get books names from ISBN

        read_books_names = []
        read_books_authors = []
        for book in read_books:
            book_name = mongo[os.getenv("MONGO_DB")][
                os.getenv("MONGO_COLLECTION")
            ].find_one({"ISBN": book})

            read_books_names.append(book_name["Title"])
            read_books_authors.append(book_name["Author"])

        list_read = []
        for b, a in zip(read_books_names, read_books_authors):
            list_read.append({"Title": b, "Author": a})

        return jsonify({"id": str(user_id), "recommendation": list_rec, "read": list_read})

    except Exception as e:
        logging.error(e)
        return jsonify([])


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
