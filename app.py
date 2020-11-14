from mizimob import app
import eventlet.wsgi


if __name__ == '__main__':
    app.run(host="localhost",port=7000,debug=True)
    # port = 8090
    # eventlet.wsgi.server(eventlet.listen(('', port)), app)
