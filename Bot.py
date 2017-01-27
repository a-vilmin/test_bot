from flask import request

@app.route('/', methods=['GET'])

def index():
    if request.method == 'GET':
        print(request.data)
    else:
        print("Broke")
