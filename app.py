import os
import socket
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
app = Flask(__name__)
line_bot_api = LineBotApi(
    'BQ0lKrBs7Kzbcc18PqYkOlb4cQBrB7B/h+QhevWmoVE+cn0fqhoOVEQmrhrsKxtNiDGc6rBLZ7DRBBUxOMy+en1BENrZZM1Nvonz8YFkJpTAd2VvL3oydN4BY57MXNmnExIpEfBSZ24wjXxvKdJPPwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5a06f27c2bdd14a4d27292223d488528')


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    app.run()