from flask import Flask, request, abort
from extensions import db, migrate
from user import *
from line_bot_api import *

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:0617@localhost:5432/nightstudy'
#postgresql://admin:0617@localhost:5432/nightstudy
db.app = app
db.init_app(app)
migrate.init_app(app, db)

# reply_other 在 reply_func\other_reply.py，不在這裡
# 這裡新增的功能，記得到 reply_func\other_reply.py 的reply_other()去新增QuickReplyButton

def reply_about(event):
    emoji = [
        {
            "index": 11,
            "productId": "5ac1bfd5040ab15980c9b435",
            "emojiId": "103"
        }
    ]
    text_message = TextSendMessage(text='歡迎使用夜讀區小幫手 $',emojis=emoji)
    text_message_2 = TextSendMessage(
            text='請選擇您想了解的項目：',
            quick_reply = QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="使用說明", text="@使用說明")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="常見問題", text="@常見問題")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="聯絡我們", text="@聯絡我們")
                    ),
                ]
            )
        )

    line_bot_api.reply_message(
        event.reply_token,
        [text_message,text_message_2])

def reply_openinghours(event):
    text_message = TextSendMessage(
            text='    🕰️開放時間🕰️\n每日17:00 ~ 隔日9:00\n國定假日及投票日不開放',
    )
    line_bot_api.reply_message(
        event.reply_token,
        text_message)

def reply_rule(event):
    text_message = TextSendMessage(
        text = '以下為夜讀區使用須知，請詳閱'
    )
    text_message_1 = TextSendMessage(
            text='https://www.lib.nthu.edu.tw/use/policies/policy13.html',
    )
    line_bot_api.reply_message(
        event.reply_token,
        [text_message,text_message_1])

def reply_contact(event):
    emoji = [
            {
                "index": 0,
                "productId": "5ac1bfd5040ab15980c9b435",
                "emojiId": "009"
            }
        ]
    text_message = TextSendMessage(text='$歡迎反饋遇到的問題：\n\n| Email |\ntc.chang@gapp.nthu.edu.tw\n\n| Google表單 |\nhttps://forms.gle/9n4MBkYuXV8eNb2u7 ',emojis=emoji)
    line_bot_api.reply_message(
        event.reply_token,
        text_message)

def reply_location(event):
    location_message = LocationSendMessage(
        title='清大圖書館(總圖)——夜讀區',
        address='新竹市光復路二段101號四樓',
        latitude=24.7953159,
        longitude=120.992523
    )
    emoji = [
        {
                "index":0,
                "productId": "5ac1bfd5040ab15980c9b435",
                "emojiId": "089"
        }
    ]
    text_message = TextSendMessage(text='$注意：\n請搭乘路易莎對面的電梯，而非圖書館內電梯上樓',emojis=emoji)
    #24.7953159,120.992523
    line_bot_api.reply_message(
        event.reply_token,
        [location_message,text_message])

def reply_faq(event):
    text_message = TextSendMessage(
        text = '開發者:'
    )
    text_message_1 = TextSendMessage(
        text = '老實說\n因為使用者只有我一個人\n所以我也不知道有什麼問題😳'
    )
    text_message_3 = TextSendMessage(
        text = '如果有遇到任何問題歡迎聯絡我們😊'
    )
    text_message_2 = TextSendMessage(
        text = '不過有幾點要說明一下：\n\n\
1.這個小幫手是示範而已，不會預約到"真正"圖書館的夜讀區\n\n\
如果有預約"真正"夜讀區的需求，請走\nhttps://libsms.lib.nthu.edu.tw/build/\n\n\
2.因為我們沒有伺服器\n所有程式都是在我的筆電運行\n所以有時候反應會有延遲，需要耐心等一下😗\n\n\
3.同上，因為沒有伺服器\n有時候bot沒反應，是因為我的筆電沒開機😖\n\n\
4.還有一種可能是\n清、大、網、路、太、爛\n\n\
以上 '
    )
    line_bot_api.reply_message(
        event.reply_token,
        [text_message,text_message_1,text_message_2,text_message_3])

def reply_instruction(event):
    text_message = TextSendMessage(
        text = '開發者有點懶\n所以沒有寫使用說明😳'
    )
    text_message_1 = TextSendMessage(
        text = '但是我們有做一個簡單的使用教學影片👍\n\n[網址之後會放上來，大概]'
    )
    line_bot_api.reply_message(
        event.reply_token,
        [text_message,text_message_1])