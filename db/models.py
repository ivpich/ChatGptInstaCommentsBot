from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    comment_id = Column(String, unique=True, nullable=False)
    post_id = Column(String, nullable=False)
    comment_text = Column(Text)
    response_text = Column(Text)
    tokens_spent = Column(Integer)

    def __repr__(self):
        return f"<Comment(comment_id='{self.comment_id}', post_id='{self.post_id}')>"
