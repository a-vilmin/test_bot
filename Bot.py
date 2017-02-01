from flask import request, Flask
from os import environ
import json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    if request.method == "POST":
        data = request.data
        print(type(data))
    return "success"
if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
