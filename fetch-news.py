import requests  # Library for making web requests

API_KEY = "0780ffa381f44946a9b3e406eee00264"  # Replace with your API key
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

response = requests.get(url)  # Send a request to the API
data = response.json()  # Convert response to JSON format

print(data)  # Print raw API response
