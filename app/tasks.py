from celery import Celery
from app.news_fetcher import fetch_latest_news
from app.database import session_local
from app.models import News
from datetime import datetime

celery = Celery("tasks", broker="redis://localhost:6379/0")

@celery.task
def fetch_and_store_news():
    db = session_local()
    articles = fetch_latest_news()
    for article in articles:
        news = News(
            title = article.get("title"),
            description = article.get("description"),
            url = article.get("url"),
            published_at = datetime.strptime(article.get("publishedAt", datetime.utcnow().isoformat()), "%Y-%m-%dT%H:%M:%SZ")
        )
        db.add(news)
    db.commit()
    db.close()