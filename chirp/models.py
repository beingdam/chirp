from datetime import datetime
from sqlalchemy import Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from chirp import db

class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    image_file: Mapped[str] = mapped_column(String(120), nullable=False, default='default.jpg')
    password: Mapped[str] = mapped_column(String(60), nullable=False)
    posts: Mapped["Post"] = relationship(backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
class Post(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    date_posted: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


# from flask import session
# from flask_session import Session
# from flask_sqlalchemy import SQLAlchemy

# with app.app_context():
#     db.create_all()