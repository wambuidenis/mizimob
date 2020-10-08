from flask import Flask, render_template
import eventlet.wsgi

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("layout.html")


@app.route('/item')
def item():
    return render_template("work-single.html")


if __name__ == '__main__':
    # app.run(port=8090)
    port = 8090
    eventlet.wsgi.server(eventlet.listen(('', port)), app)
