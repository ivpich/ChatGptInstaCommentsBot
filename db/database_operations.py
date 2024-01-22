from db.database import SessionLocal
from db.models import Comment
from contextlib import contextmanager

@contextmanager
def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def add_comment(db, comment_data):
    db_comment = Comment(**comment_data)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def get_comment_by_id(db, comment_id):
    return db.query(Comment).filter(Comment.comment_id == comment_id).first()
