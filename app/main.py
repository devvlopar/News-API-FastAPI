from fastapi import FastAPI, Depends
from app.database import session_local
from sqlalchemy.orm import Session
from app.models import News


app = FastAPI()

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

@app.get('/news')
def read_news(db: Session = Depends(get_db)):
    return db.query(News).order_by(News.published_at.desc()).limit(10).all()