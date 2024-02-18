#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Flask app for the ChromaDB retrieval process.
"""

from pprint import pprint
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import datetime
import logging
from dotenv import load_dotenv
import os
from pathlib import Path

from chromadb_tests.chromadb_tests import load_txt_documents, load_pdf_documents
from chromadb_tests.chromadb_tests import store_documents, query_with_retrieval

from config import LOGGER_CONFIG

# **********
# Sets up logger
logger = logging.getLogger(__name__)


# **********
# Create the Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

messages = []

# Get environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set")


# **********
def init_chromadb():
    global db
    global db_spec
    global db_reqs
    documents_txt_dir = Path("./documents/txt")
    documents_pdf_dir = Path("./documents/pdf")
    docs = load_txt_documents(documents_txt_dir)
    docs.extend(load_pdf_documents(documents_pdf_dir))
    docs_reqs = load_txt_documents(documents_txt_dir)
    docs_spec = load_pdf_documents(documents_pdf_dir)

    db_reqs = store_documents(docs_reqs)
    db_spec = store_documents(docs_spec)
    db = store_documents(docs)
    logger.info("ChromaDB initialized with documents.")


# Call the function to initialize ChromaDB at the start of the app
init_chromadb()


# **********
@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/submit-text", methods=["POST"])
def submit_text():
    data = request.json
    pprint(f"request.json: {data}")
    text = data["text"]
    context = data["context"]

    # ****
    # User message
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text = f"Today's date: {current_date}\n\n{text}"
    user_message = {
        "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "role": "user",
        "message": text,
        "context": context,
    }
    messages.append(user_message)

    # ****
    # Generate response
    if context == "reqs":
        response = query_with_retrieval(text, db_reqs, OPENAI_API_KEY)
    elif context == "spec":
        response = query_with_retrieval(text, db_spec, OPENAI_API_KEY)
    response_message = {
        "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "role": "user",
        "message": response,
        "context": context,
    }
    messages.append(response_message)

    print(text)
    print(response)
    return jsonify(
        {"message": "Text received successfully", "response": response_message}
    )


@app.route("/get-messages", methods=["GET"])
def get_messages():
    print(messages)
    return jsonify(messages)


# **********
if __name__ == "__main__":
    import logging.config

    logging.disable(logging.DEBUG)
    logging.config.dictConfig(LOGGER_CONFIG)

    # Load environment variables
    load_dotenv()

    app.run(debug=True, port=5000)
