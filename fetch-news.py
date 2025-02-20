import requests  # Library for making web requests

API_KEY = "your-api-key"  # Replace with your API key
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

response = requests.get(url)  # Send a request to the API
data = response.json()  # Convert response to JSON format

print(data['response'])  # Print raw API response
