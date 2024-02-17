#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Flask app for the ChromaDB retrieval process.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import datetime
import logging
from dotenv import load_dotenv
import os
from pathlib import Path

from chromadb_tests.chromadb_tests import load_documents, store_documents, query_with_retrieval

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
    documents_dir = Path("./documents")
    docs = load_documents(documents_dir)
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
    text = data["text"]
    
    # ****
    # User message
    user_message = {
        "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "role": "user",
        "message": text,
    }
    messages.append(user_message)
    
    # ****
    # Generate response
    response = query_with_retrieval(text, db, OPENAI_API_KEY)  # Notice db is used directly
    response_message = {
        "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "role": "user",
        "message": response,
    }
    messages.append(response_message)
    
    print(text)
    print(response)
    return jsonify({"message": "Text received successfully", "response": response_message})


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
    

