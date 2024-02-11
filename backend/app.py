from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/submit-text", methods=["POST"])
def submit_text():
    data = request.json
    text = data["text"]
    # Your processing logic here
    print(text)
    return jsonify({"message": "Text received successfully"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Specify the port for Flask to run on