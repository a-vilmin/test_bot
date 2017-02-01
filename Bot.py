from flask import request, Flask
from os import environ
import json
import requests

# globals
app = Flask(__name__)
bot_id = environ['BOT_ID']


def bot_commands(info):
    if info['text'].startswith('HEY BOT'):
        body = {"bot_id": bot_id,
                "text": "Roll Armchair, " + info['name'] + "!!"}
        requests.post("https://api.groupme.com/v3/bots/post", body)


@app.route('/', methods=['POST'])
def index():
    if request.method == "POST":
        data = json.loads(request.data.decode("utf-8"))
        bot_commands(data)

    return "success"
if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
