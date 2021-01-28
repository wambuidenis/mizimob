from flask import render_template, request, redirect, url_for, flash, send_from_directory, redirect, session
from flask_login import login_user, current_user, login_required, logout_user
from flask_sqlalchemy import sqlalchemy

from mizimob import app, bcrypt, db
from mizimob.forms.product import (LoginForm, ProductForm, CategoryForm, PhoneEmail, OrderForm, CategoryForm,
                                   RegisterForm, CartForm, Checkout)
from mizimob.models.models import (User, Category, CategorySchema, UserSchema, Product, Media, MediaSchema,
                                   ProductSchema, Order, OrderSchema, Cart, CartSchema)
from mizimob.others.utils import validate_email, validate_phone, send_email, reset_body, crop_max_square, is_admin
import os
from PIL import Image
import time
from dateutil import parser

# ---------------------------------
# ------- SETTING GLOBAL VARS -----
# ---------------------------------
user_schema = UserSchema()
users_schema = UserSchema(many=True)

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

image_schema = MediaSchema()
images_schema = MediaSchema(many=True)

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

# categories = list()
categories = Category.query.all()

back_mapper = dict()
front_mapper = dict()


def mapper():
    for x in categories:
        back_mapper.update({x.name.lower().capitalize(): x.id})
        front_mapper.update({x.id: x.name.lower().capitalize()})


mapper()


# serving some images
@app.route("/img/map-9.jpg", methods=["GET"])
def map_9():
    return send_from_directory("img", filename="map-9.jpg")


@app.route("/img/displace-circle.png", methods=["GET"])
def map_10():
    return send_from_directory("img", filename="displace-circle.png")


@app.route('/')
def home():
    session["key"] = "denis kiruku wambui"

    # get products from the database
    products = Product.query.all()
    product_dict = products_schema.dump(products)

    # name
    new_products = list()
    for product in product_dict:
        index = product["category"]
        product["category"] = front_mapper[int(index)]
        new_products.append(product)
        try:
            lookup = Media.query.filter_by(product_id=product["id"]).first()
            image = image_schema.dump(lookup)
            file = image_schema.dump(lookup)["file"]
            product["image"] = file
        except KeyError:
            file = "default.jpg"
            product["image"] = file
    return render_template("index.html", products=new_products, categories=categories)


@app.route('/product/<string:name>', methods=["GET", "POST"])
def product_item(name):
    # form
    form = CartForm()

    #  we are going  to get the name from the database
    # get images and file fron the database and sho them here
    product = Product.query.filter_by(name=name).first()
    media_lookup = Media.query.filter_by(product_id=product.id).all()
    # media_data
    lookup_data = product_schema.dump(product)
    media_data = images_schema.dump(media_lookup)
    images = list()
    for media in media_data:
        images.append(media['file'])
    lookup_data["images"] = images
    index = lookup_data["category"]
    lookup_data["category"] = front_mapper[int(index)]
    if request.method == "POST":
        if form.validate_on_submit():
            # user logged in <<DATA>>
            # try:
            user_id = current_user.id
            product = Product.query.filter_by(name=name).first()
            # when to book
            when = form.date.data
            when_datetime = parser.parse(when)
            lookup = Cart(product.id, user_id, when_datetime)
            db.session.add(lookup)
            db.session.commit()
            return redirect(url_for("cart"))
            flash("Item Added to cart Successfully", "success")

            # time.sleep(2)
            # except AttributeError:
            #     # require login
            #     return redirect(url_for("user_login", next="product_item", name=name))
        else:
            flash("Item Could be added to the cart", "Error")

    return render_template("work-single.html", product=lookup_data, form=form)


@app.route('/cart/view/<string:name>')
@login_required
def item_view(name):
    #  we are going  to get the name from the database
    # get images and file fron the database and sho them here
    lookup = Product.query.filter_by(name=name).first()
    media_lookup = Media.query.filter_by(product_id=lookup.id).all()
    # media_data
    lookup_data = product_schema.dump(lookup)
    media_data = images_schema.dump(media_lookup)
    images = list()
    for media in media_data:
        images.append(media['file'])
    lookup_data["images"] = images
    index = lookup_data["category"]
    lookup_data["category"] = front_mapper[int(index)]
    return render_template("cart_view.html", product=lookup_data)


@app.route("/admin/login", methods=["POST", 'GET'])
def login():
    # login = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for("products_all"))
    # loading the form
    login = LoginForm()
    # checking the form data status
    if login.validate_on_submit():
        user = User.query.filter_by(email=login.email.data).first()
        if user and bcrypt.check_password_hash(user.password, login.password.data):
            next_page = request.args.get("next")
            login_user(user)
            return redirect(next_page) if next_page else redirect(url_for('products_all'))
        else:
            flash("Login unsuccessful Please Check Email and Password", "danger")
    return render_template("login.html", form=login)


@app.route("/user/login", methods=["POST", 'GET'])
def user_login():
    if current_user.is_authenticated:
        return redirect(url_for("products_all"))

    # loading the form
    login = LoginForm()
    # checking the form data status
    if login.validate_on_submit():
        user = User.query.filter_by(email=login.email.data).first()
        if user and bcrypt.check_password_hash(user.password, login.password.data):
            next_page = request.args.get("next")
            login_user(user)
            return redirect(next_page) if next_page else redirect(url_for('products_all'))
        else:
            flash("Login unsuccessful Please Check Email and Password", "danger ")
    return render_template("login.html", form=login)


@app.route("/user/signup", methods=["POST", 'GET'])
def user_register():
    # if current_user.is_authenticated:
    #     return redirect(url_for("home"))

    # loading the form
    form = RegisterForm()
    # get the deatil  from the form
    firstname = form.firstname.data
    lastname = form.lastname.data
    email = form.email.data
    phone = form.phone.data
    password = form.password.data
    confirm_password = form.confirm_password.data
    print(firstname, lastname, phone, email, password, confirm_password)

    # checking the form data status
    if form.validate_on_submit():
        if password == confirm_password:
            # passwords match
            hashed_password = bcrypt.generate_password_hash(password)
            user = User(firstname, lastname, phone, email, hashed_password)
            db.session.add(user)
            db.session.commit()
        else:
            flash("Password do not match", "danger")
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            next_page = request.args.get("next")
            login_user(user)
            return redirect(next_page) if next_page else redirect(url_for('products_all'))
        else:
            flash("Login unsuccessful Please Check Email and Password", "danger")
    return render_template("signup.html", form=form)


@app.route("/admin/product/all")
@login_required
def products_all():
    # get products from the database
    products = Product.query.all()
    product_dict = products_schema.dump(products)
    # name
    new_products = list()
    for product in product_dict:
        index = product["category"]
        product["category"] = front_mapper[int(index)]
        new_products.append(product)
        try:
            lookup = Media.query.filter_by(product_id=product["id"]).first()
            image = image_schema.dump(lookup)
            file = image_schema.dump(lookup)["file"]
            product["image"] = file
        except KeyError:
            file = "default.jpg"
            product["image"] = file
    return render_template("manage_product.html", products=new_products, categories=categories)


@app.route("/test")
@login_required
def test():
    return render_template("withmenu.html")


@app.route("/admin/product/edit/<string:name>", methods=["POST", "GET"])
@login_required
def edit_project(name):
    lookup = Product.query.filter_by(name=name).first()
    form = ProductForm()
    if request.method == "POST":
        if form.validate_on_submit():
            lookup.name = form.title.data
            lookup.expires = form.expires.data
            lookup.price = form.price.data
            lookup.description = form.description.data
            lookup.category = int(back_mapper[form.category.data])

            lookup.active = True if form.active.data == "Active" else False
            db.session.commit()

            data = product_schema.dump(lookup)
            files = form.media.data
            filenames = []
            for file in files:
                filenames.append(file.filename)
                path = os.path.join(os.getcwd(), "mizimob", "static", "uploads", file.filename)

                # cropping the image
                file.save(path)

                im = Image.open(path)
                image = crop_max_square(im)
                image.save(path, quality=100)

                # added the database
                lookup = Media(data['id'], file.filename)
                db.session.add(lookup)
                db.session.commit()
            flash("Data Updated Sucessfully", "success")
        else:
            flash("Please Make sure all form field are valid", "warning")
    else:
        form.title.data = lookup.name
        form.expires.data = lookup.expires
        form.description.data = lookup.description
        form.active.data = lookup.active
        form.price.data = lookup.price
    return render_template("edit.html", form=form, name=name)


@app.route("/admin/category/add", methods=["POST", "GET"])
def add_category():
    form = CategoryForm()
    if request.method == "POST":
        if form.validate_on_submit():

            # getting data from the form
            name = form.name.data

            # adding to the database
            lookup = Category(name)
            db.session.add(lookup)
            db.session.commit()

            flash(f"Category {name} Added Successfully", "success")
        else:
            flash("Error! Name Might exist.", "error")

    return render_template("add_category.html", form=form)


@app.route('/cart', methods=['POST', "GET"])
@login_required
def cart():
    data = list()
    user = current_user
    data_ = Cart.query.filter_by(user_id=user.id).all()
    price = 0
    for item in data_:
        unformatted = item.when
        new = list()
        id = item.product_id
        product = Product.query.get(id)
        image = Media.query.filter_by(product_id=id).first()
        item.pretty_date = unformatted.strftime("%a, %d %b %y %I:%M")
        price = price + product.price
        new.append(item)
        new.append(product)
        new.append(image)
        data.append(new)

    orders = list()
    orders_ = Order.query.filter_by(user_id=user.id).all()
    for item in orders_:
        print(item)
        unformatted = parser.parse(item.when)
        print(unformatted)
        new = list()
        id = item.product_id
        product = Product.query.get(id)
        image = Media.query.filter_by(product_id=id).first()
        item.pretty_date = unformatted.strftime("%a, %d %b %y %I:%M")
        new.append(item)
        new.append(product)
        new.append(image)
        orders.append(new)

    return render_template("cart_posts.html", orders=data, user=current_user, total=price, odr= orders)


@app.route("/checkout", methods=["GET", "POST"])
@login_required
def checkout():
    data = list()
    user = current_user
    form = Checkout()

    data_ = Cart.query.filter_by(user_id=user.id).all()
    price = 0
    for item in data_:
        unformatted = item.when
        new = list()
        id = item.product_id
        product = Product.query.get(id)
        image = Media.query.filter_by(product_id=id).first()
        item.pretty_date = unformatted.strftime("%a, %d %b %y %I:%M")
        price = price + product.price
        new.append(item)
        new.append(product)
        new.append(image)
        data.append(new)
    return render_template("checkout.html", orders=data, user=current_user, total=price, form=form)


@app.route("/confirm/order", methods=["GET", "POST"])
@login_required
def order_confirmed():
    """Here we are going to add the item to the users order for the day and remove the fom the cart"""

    user = current_user
    data_ = Cart.query.filter_by(user_id=user.id).all()

    for item in data_:
        lookup = Order(item.product_id, item.user_id, item.when)
        db.session.add(lookup)
        db.session.commit()

        # remove order from the database
        cart_item = Cart.query.get(item.id)
        db.session.delete(cart_item)
        db.session.commit()

    # we are going to email the user
    flash("Order have been made. Please wait confirmation from mizimob", "success")

    return redirect(url_for("cart"))


@app.route("/db/seed", methods=["POST"])
def seeder():
    # user seed
    user = User("Admin", "Mode", "254719573310", "denniskiruku@gmail.com", bcrypt.generate_password_hash("1234"))
    db.session.add(user)
    try:
        #  category
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        return {"Error!": "DB Aleardy Seeded",
                "details": {
                    'user': user_schema.dump(user)
                }
                }, 500

    return {'user': user_schema.dump(user)}, 201


@app.route("/admin/product/add", methods=['POST', "GET"])
@login_required
def add():
    form = ProductForm()
    categories = Category.query.all()
    categories = categories_schema.dump(categories)
    # update_mapper
    mapper()
    if request.method == "POST":
        if form.validate_on_submit():
            title = form.title.data
            category = int(back_mapper[form.category.data])
            price = form.price.data
            description = form.description.data
            expires = form.expires.data
            active = True if form.active.data == "Active" else False
            print(title, description, category, price, expires, active)
            # data
            lookup = Product(title, description, category, price, expires, active)
            db.session.add(lookup)
            db.session.commit()

            # product schema data
            data = product_schema.dump(lookup)
            files = form.media.data
            filenames = []

            for file in files:
                filenames.append(file.filename)
                path = os.path.join(os.getcwd(), "mizimob", "static", "uploads", file.filename)
                file.save(path)

                # added the database
                lookup = Media(data['id'], file.filename)
                db.session.add(lookup)
                db.session.commit()

                # cropping the image
                im = Image.open(path)
                image = crop_max_square(im)
                image.save(path, quality=100)

            flash("form data submitted is valid", "success")
    else:
        flash("Error with the form", "warning")
    return render_template("add.html", form=form, categories=categories)


@app.route("/admin/orders/manage", methods=['POST', "GET"])
@login_required
def order():
    authorized(current_user, "add")
    # getting all the orders
    orders_lookup = Order.query.all()
    orders_data = orders_schema.dump(orders_lookup)
    for order in orders_lookup:
        order_ = list()
        lookup = Product.query.get(order.product_id)
        order_.append(order)
        order_.append(lookup)

    # for item in
    # get products from the database
    products = Product.query.all()
    product_dict = products_schema.dump(products)

    # name
    new_products = list()
    category_mapper = {"1": "events", "2": "title", "3": "rental"}
    for product in product_dict:
        index = product["category"]
        product["category"] = category_mapper[f"{index}"]
        new_products.append(product)
        try:
            lookup = Media.query.filter_by(product_id=product["id"]).first()
            image = image_schema.dump(lookup)
            file = image_schema.dump(lookup)["file"]
            product["image"] = file
        except KeyError:
            file = "default.jpg"
            product["image"] = file

    return render_template("manage_order.html", products=new_products, orders=orders_lookup)


@app.route("/logout", methods=["POST", "GET"])
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/test")
def test_():
    return render_template("test.html")


@app.route("/cart/<string:id>")
def cart_remove(id):
    if (id):
        item = Cart.query.get(id)
        if (item):
            db.session.delete(item)
            db.session.commit()
            flash(f"Item removed from cart", "info")
    return redirect(url_for("cart"))


def authorized(user, redirect_to):
    if not is_admin(user):
        return redirect(url_for(redirect_to))
