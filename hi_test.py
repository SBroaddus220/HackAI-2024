import requests

# Define the URL of the API
url = 'http://localhost:8084/completion'

# Define the headers
headers = {
    'Content-Type': 'application/json',
}

# Define the payload
data = {
    "prompt": "Building a website can be done in 10 simple steps:",
    "n_predict": 128
}

# Convert the payload to JSON
json_data = data

# Make the POST request
response = requests.post(url, json=json_data, headers=headers)

# Print the response text
print(response.text)
