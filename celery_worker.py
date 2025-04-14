from app.tasks import celery

celery.conf.beat_schedule = {
    'fetch-news-every-minute': {
        'task': 'app.tasks.fetch_and_store_news',
        'schedule': 60.0,
    },
}
celery.conf.timezone = 'UTC'

if __name__ == "__main__":
    celery.start()