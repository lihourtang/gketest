import os
from flask import Flask, jsonify
import requests


app = Flask(__name__)


@app.route('/', methods=['GET'])
def message1():
    message = 'message1 getting from endpoint /message1'
    return jsonify(message)

@app.route('/message2', methods=['GET'])
def message2():
    api = requests.get('http://localhost:5000/')
    message = api.json()
    return jsonify(message)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
    # app.run(port=5002, threaded=False)
    #app.run()
    #app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

    # Serve the app with gevent
    # http_server = WSGIServer(('',80), app)
    # http_server.serve_forever()