from extensions import *
from user import *
from line_bot_api import *

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:0617@localhost:5432/nightstudy'
#postgresql://admin:0617@localhost:5432/nightstudy
db.app = app
db.init_app(app)
migrate.init_app(app, db)

def verify_user(stu_id,password):
        user = User.query.filter(User.stu_id == str(stu_id)).first()
        if not user:
            return 'stu_id_dne'
        else:
            if user.password == password:
                return 'success'
            else:
                return 'pwd_err'

def reply_login(event,profile,t_user):
    user = User.query.filter(User.line_id == profile.user_id).first()
    if not user:
        text_message= TextSendMessage(text="初次使用，請先依格式輸入：\n@user:您的學號,您的密碼\n(密碼預設為身份證字號，首字大寫)\n\n例:@user:111000101,A123456789")
        text_message_2 = TextSendMessage(text="可複製以下範本更改輸入")
        text_message_3 = TextSendMessage(text="@user:學號,密碼")
        line_bot_api.reply_message(
            event.reply_token,
            [text_message,text_message_2,text_message_3])
    else:
        text_message= TextSendMessage(text="您已登入")
        line_bot_api.reply_message(
            event.reply_token,
            text_message)


def reply_user(event,message_text,profile,t_user):
    if t_user.login_stat == True:
        text_message= TextSendMessage(text="您已登入")
        line_bot_api.reply_message(
            event.reply_token,
            text_message)
    else:
        try:
            account = message_text[6:].split(',')
            print(account[0],account[1])
            verify = verify_user(account[0],account[1])
            try:
                if(verify == 'stu_id_dne'):
                    text_message= TextSendMessage(text="學號不存在")
                    line_bot_api.reply_message(
                        event.reply_token,
                        text_message)
                elif(verify == 'pwd_err'):
                    text_message= TextSendMessage(text="密碼錯誤")
                    line_bot_api.reply_message(
                        event.reply_token,
                        text_message)
                else:
                    t_user.login_stat = True
                    user = User.query.filter(User.stu_id == account[0]).first()
                    if((user.line_id)[:4] != 'line'):
                        text_message= TextSendMessage(text="此學號已綁定其他line帳號")
                        line_bot_api.reply_message(
                            event.reply_token,
                            text_message)
                    else:
                        user.line_id = profile.user_id
                        user.login_stat = True
                        db.session.commit()
                        text_message= TextSendMessage(text="登入成功")
                        line_bot_api.reply_message(
                            event.reply_token,
                            text_message)
            except:
                text_message= TextSendMessage(text="輸入格式錯誤")
                line_bot_api.reply_message(
                    event.reply_token,
                    text_message)
        except:
            text_message= TextSendMessage(text="輸入格式錯誤")
            line_bot_api.reply_message(
                event.reply_token,
                text_message)