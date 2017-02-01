from flask import request, Flask

app = Flask(__name__)


@app.route('/data', methods=['POST'])
def data():
    if request.method == "POST":
        print(request.data)
    else:
        print("Broke")

    return "success"
if __name__ == '__main__':
    app.run()
