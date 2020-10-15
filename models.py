"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """User class for blogly"""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    first_name = db.Column(db.String(50),
                    nullable=False)
    last_name = db.Column(db.String(50),
                    nullable=False)
    img_url = db.Column(db.String(500),
                    nullable=False,
                    default="/static/blank-profile-picture-973460_960_720.webp")

    
    posts = db.relationship('Post')


class Post(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    title = db.Column(db.String(200),
                    nullable=False)
    content = db.Column(db.String(1000000),
                    nullable=False)
    created_at = db.Column(db.DateTime,
                    nullable=False)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False)   

    user = db.relationship('User')



