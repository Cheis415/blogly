"""Blogly application."""

from flask import Flask, render_template, redirect, request
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret_key'
toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route("/")
def take_home():
    user = User.query.all()
    return render_template("/users.html", user=user)


@app.route("/create")
def go_create():

    return render_template("/create.html")


@app.route("/create", methods=["POST"])
def create_user():

    first = request.form["first_name"]
    last = request.form["last_name"]
    url = request.form["url"] if request.form["url"] else None
    user = User(first_name=first, last_name=last, img_url=url)
    db.session.add(user)
    db.session.commit()

    return redirect("/")
