from mizimob import app
import eventlet.wsgi


if __name__ == '__main__':
    port = 7000
    # app.run(host="0.0.0.0",port=port,debug=True)
    eventlet.wsgi.server(eventlet.listen(('', port)), app)
