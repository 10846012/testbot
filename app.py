from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi('c9U4RITsjcLHDX14yfulJar4huzOEVHoiGBzjb1df3rNvE1humv+HoobUT0BoXYWfgtQTKIJhKaOq3+7ererZS0z+t23f1TvNMbTym9WZiF9Qxs7zICPwudGi9By1v9rumuCgXdxDX7dySQ+5RtSFgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('8ae0e5241c8b31b78b8361a25711d527')

line_bot_api.push_message('Uf5b29d10f1347f1ce7d0f256d3f1b4fd', TextSendMessage(text='你可以開始了'))


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
    line_bot_api.reply_message(event.reply_token,message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)