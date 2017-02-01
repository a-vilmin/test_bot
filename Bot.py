from flask import request, Flask
from os import environ

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    if request.method == "POST":
        print(request.data)
    else:
        print("Broke")

    return "success"
if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
