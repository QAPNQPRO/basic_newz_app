# app/routes/home_routes.py
from flask import Blueprint, render_template, session
from app.services.news_service import NewsService

home_bp = Blueprint('home', __name__)
news_service = NewsService()

@home_bp.route('/')
def index():
    news_articles = news_service.get_top_headlines()
    return render_template('home.html', user=session.get('user'), news=news_articles)
