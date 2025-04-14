import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
NEWS_API_URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

def fetch_latest_news():
    response = requests.get(NEWS_API_URL)
    print(response)
    if response.status_code == 200:
        print(response.json())
        return response.json().get("articles", [])
    return []