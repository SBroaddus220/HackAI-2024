from flask import Flask, request, jsonify
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/submit-text", methods=["POST"])
def submit_text():
    data = request.json
    text = data["text"]
    # Process the text as needed
    print(text)  # Example action: print the text
    return jsonify({"message": "Text received successfully"})


if __name__ == "__main__":
    app.run(debug=True)
