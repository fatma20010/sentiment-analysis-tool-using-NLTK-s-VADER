import requests

# Define the API endpoint
url = "http://127.0.0.1:5000/analyze"

# Define the input text
data = {"text": "I love this food!"}

# Send a POST request
response = requests.post(url, json=data)

# Print the response
print("Response JSON:", response.json())
