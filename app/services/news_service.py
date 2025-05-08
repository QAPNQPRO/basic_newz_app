# app/services/news_service.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class NewsService:
    API_KEY = os.getenv('NEWS_API_KEY')
    BASE_URL = "https://newsapi.org/v2/top-headlines"
    

    def get_top_headlines(self, country="us", category="general"):
        params = {
            "apiKey": self.API_KEY,
            "country": country,
            "category": category,
            "pageSize": 10
        }
        response = requests.get(self.BASE_URL, params=params)
        if response.status_code == 200:
            return response.json().get('articles', [])
        return []
