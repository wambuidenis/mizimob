from flask import render_template
from mizimob import app
from mizimob.forms.product import LoginForm


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/item')
def item():
    return render_template("work-single.html")


@app.route("/admin/login", methods=["POST", 'GET'])
def admin_login():
    login_form = LoginForm()
    return render_template("login.html", form=login_form)


@app.route("/admin/product/all")
def manage_routes():
    return render_template("manage_account.html")


@app.route("/admin/product/all")
def product_all():
    pass


@app.route("/admin/product/edit/<int:id>")
def edit_project():
    pass


@app.route("/admin/product/add")
def add_product():
    pass


@app.route('/cart')
def cart():
    return render_template("cart.html")
