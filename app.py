from mizimob import app
import eventlet.wsgi


if __name__ == '__main__':
    app.run()
    # port = 8090
    # eventlet.wsgi.server(eventlet.listen(('', port)), app)
