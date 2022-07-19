import imp
from flask import Flask, request, abort

from linebot import(
    LineBotApi, WebhookHandler
)
from linebot.exceptions import(
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi('Qyhe26E0HX1jWuaLBVtzS7Ht9l0aQmVAJyPRusrdH5neD2TgmK7/gmWr5u/x7gB7I6Im9ZDmyKLuoesbs4SuX7qICy9DPHU/uC/tCiXn+zD2tHBycfzv2a9ubv9kaCujEp2oHhQ/glucsGVa4pWmBwdB04t89/1O/w1cDnyilFU=')

handler = WebhookHandler('60e245179221aff23806ad009848031e')

line_bot_api.push_message('Uf5b29d10f1347f1ce7d0f256d3f1b4fd',TextSendMessage(text='開始'))

@app.route('/callback', methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info('Request body: ' + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host= '0.0.0.0' , port=port)