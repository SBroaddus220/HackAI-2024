from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

messages = []


messages = []


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/submit-text", methods=["POST"])
def submit_text():
    data = request.json
    text = data["text"]

    messages.append(
        {
            "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "role": "user",
            "message": text,
        }
    )

    print(text)
    return jsonify({"message": "Text received successfully"})


@app.route("/get-messages", methods=["GET"])
def get_messages():
    print(messages)
    return jsonify(messages)


if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Specify the port for Flask to run on
