from flask import Flask, render_template


app = Flask(__name__)


#  import routes
from mizimob.routes import main