from extensions import*
from user import *
from line_bot_api import *

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:0617@localhost:5432/nightstudy'
#postgresql://admin:0617@localhost:5432/nightstudy
db.app = app
db.init_app(app)
migrate.init_app(app, db)

def reply_other(event,mode_id):
    if(mode_id == 1):
        text_message = TextSendMessage(
            text='更多功能陸續開發中~',
            quick_reply = QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="夜讀區地點", text="@地點")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="夜讀區開放時間", text="@開放時間")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="夜讀區使用規則", text="@規則")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="聯絡我們", text="@聯絡我們")
                    ),
                ]
            )
        )
    elif(mode_id == 2):
        item = []
        item.append(QuickReplyButton(action=MessageAction(label="測試1", text="@測試1")))
        item.append(QuickReplyButton(action=MessageAction(label="測試2", text="@測試2")))
        item.append(QuickReplyButton(action=MessageAction(label="測試3", text="@測試3")))
        text_message = TextSendMessage(
            text='測試頻道',
            quick_reply = QuickReply(
                items=item
            )
        )

    line_bot_api.reply_message(
        event.reply_token,
        text_message)