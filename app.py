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
    books = mongo[os.getenv("MONGO_DB")][
        os.getenv("MONGO_COLLECTION_PREDICTIONS")
    ].find_one({"USER-ID": int(user_id)})

    return jsonify(books["Books"])


if __name__ == "__main__":
    app.run(debug=True)
