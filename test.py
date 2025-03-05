import requests
api = "https://api.quotable.io/quotes/random"
response = requests.get(api)
data = response.json()
print(data)