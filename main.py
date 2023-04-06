from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    url = request.args.get('url')
    if not url:
        return 'Please provide a URL parameter', 400

    response = requests.get(url + path, params=request.args)
    headers = dict(response.headers)
    headers['Access-Control-Allow-Origin'] = '*'
    return response.content, response.status_code, headers
