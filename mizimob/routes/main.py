from flask import render_template
from mizimob import app


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/item')
def item():
    return render_template("work-single.html")


@app.route("/admin/login")
def admin_login():
    return render_template("login.html")