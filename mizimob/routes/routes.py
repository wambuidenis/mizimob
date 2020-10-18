from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required
from mizimob import app, bcrypt, db
from mizimob.forms.product import LoginForm, ProductForm, CategoryForm
from mizimob.models.models import User, Category, CategorySChema, UserSchema
from flask_sqlalchemy import sqlalchemy

user_schema = UserSchema()
users_schema = UserSchema(many=True)

category_schema = CategorySChema()
categories_schema = CategorySChema(many=True)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/item')
def item():
    return render_template("work-single.html")


@app.route("/admin/login", methods=["POST", 'GET'])
def login():
    # login = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for("products_all"))

    # loading the form
    login = LoginForm()

    # checking the form data status
    if login.validate_on_submit():
        print("form_data", login.email.data, login.password.data)
        user = User.query.filter_by(email=login.email.data).first()
        if user and bcrypt.check_password_hash(user.password, login.password.data):
            next_page = request.args.get("next")
            login_user(user)
            return redirect(next_page) if next_page else redirect(url_for('products_all'))
        else:
            flash("Login unsuccessful Please Check Email and Password", "danger ")
    return render_template("login.html", form=login)


@app.route("/admin/product/all")
@login_required
def products_all():
    return render_template("manage_product.html")



@app.route("/admin/product/edit/<int:id>")
@login_required
def edit_project():
    pass


@app.route("/admin/category/add", methods=["POST"])
def add_category():
    form = CategoryForm()
    return render_template()


@app.route('/cart')
def cart():
    return render_template("cart.html")


@app.route("/db/seed", methods=["POST"])
def seeder():
    # category seed
    category = Category("rentals")
    db.session.add(category)

    # user seed
    user = User("Denis", "Kiruku", "254719573310", "denniskiruku@gmail.com", bcrypt.generate_password_hash("1234"))
    db.session.add(user)
    try:
        #  category
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        return {"Error!": "DB Aleardy Seeded",
                "details": {
                    "category": category_schema.dump(category), 'user': user_schema.dump(user)
                }
                }, 500

    return {"category": category_schema.dump(category), 'user': user_schema.dump(user)}, 201

@app.route("/admin/product/add", methods=['POST', "GET"])
def add():
    form = ProductForm()
    return render_template("add.html",form=form)


@app.route("/admin/product/events", methods=['POST', "GET"])
def events():
    return render_template("events.html")


@app.route("/admin/product/travel", methods=["POST", "GET"])
def travel():
    return render_template("travel.html")


@app.route("/admin/rentals/rentals", methods=["POST", "GET"])
def rentals():
    return render_template("rentals.html")

    pass
