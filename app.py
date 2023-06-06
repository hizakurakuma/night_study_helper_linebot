#==================================================================================================#

# 以下是自定義的module #

# extensions為 預先匯入flask,flask sqlalchemy,flask_migrate函式庫的module，詳見extensions.py
# extensions定義 db = SQLAlchemy(), migrate = Migrate()，詳見extensions.py
from extensions import * 

# user為 使用者資料庫相關的module，詳見user.py
# reserve為 預約資料庫相關的module，詳見reserve.py
from user import *
from reserve import *

# reply_func下為 匯入所有回覆關鍵字對應功能函式的module，詳見reply_func\__init__.py
from reply_func.basic_reply import * # @關於、@常見問題、@使用說明、@開放時間、@規則、@聯絡我們的回覆函式放這裡
from reply_func.other_reply import * # @其他 回覆函式放這裡
from reply_func.login import * # @登入、檢查登入的回覆函式放這裡
#from reply_func.reserv_func import *
from reply_func.reserv_func_v2 import * # @預約 相關的回覆及功能函式放這裡
from reply_func.my_info import * # @我的 回覆函式及功能放這裡

from line_bot_api import * # line_bot_api相關的tokens及官方SDK放這裡，詳見line_bot_api.py

#==================================================================================================#
# 以下是flask的基本設定 #
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:0617@localhost:5432/nightstudy'
db.app = app
db.init_app(app)
migrate.init_app(app, db)


mode_id = 1 #開啟"@其他"的測試通道用

#==================================================================================================#

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

#==================================================================================================#
# 以下是line bot處理使用者發送訊息(MessageEvent)的大區塊 #
#==================================================================================================#
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message_text = str(event.message.text)

    profile = line_bot_api.get_profile(event.source.user_id)

    print(f'{profile.display_name}: {message_text}')

    t_user = T_User.query.filter(T_User.line_id == profile.user_id).first()
    if not t_user:
        t_user = T_User(profile.user_id, profile.display_name, profile.picture_url)
        db.session.add(t_user)
        db.session.commit()
    
    # 以下區塊 判斷使用者輸入的關鍵字訊息

    if (message_text == '@關於'):
        reply_about(event) # 關於reply_about詳見reply_func/basic_reply.py

    #=======================================#

    elif(message_text == '@預約'):
        if t_user.login_stat == False:
            text_message= TextSendMessage(text="請先至選單點選登入")
            line_bot_api.reply_message(
                event.reply_token,
                text_message)

        else:
            user = User.query.filter(User.line_id == profile.user_id).first()
            reserv_count = user.reserv_count
            if(reserv_count > 2):
                text_message= TextSendMessage(text="⚠️\n    您已預約滿三筆\n    無法再預約")
                line_bot_api.reply_message(
                    event.reply_token,
                    text_message)
            else:
                choose_date(event) # 預約choose_date詳見reply_func/reserv_func_v2.py
    
    elif(message_text == '@取消預約'):
        if t_user.login_stat == False:
            text_message= TextSendMessage(text="請先至選單點選登入")
            line_bot_api.reply_message(
                event.reply_token,
                text_message)
                
        else:
            user = User.query.filter(User.line_id == profile.user_id).first()
            reserv_count = user.reserv_count
            if(reserv_count == 0):
                text_message = TextSendMessage(text='您目前沒有預約')
                line_bot_api.reply_message(
                    event.reply_token,
                    text_message)
            else:
                text_message = TextSendMessage(text='請選擇要取消的預約')
                my_reserv(event,profile,user,text_message)

    # 用戶個人資訊和預約資料
    elif(message_text == '@我的'):
        if t_user.login_stat == False:
            text_message= TextSendMessage(text="請先至選單點選登入")
            line_bot_api.reply_message(
                event.reply_token,
                text_message)
        else:
            user = User.query.filter(User.line_id == profile.user_id).first()
            text_message = TextSendMessage(text=f'您好，{user.name}同學')
            my_reserv(event,profile,user,text_message) # 關於my_reserv詳見reply_func/my_info.py
    #=======================================#

    # 判斷登入狀態，若未登入則切至@user登入
    elif (message_text == '@登入'):
        reply_login(event,profile,t_user) # 關於reply_login詳見reply_func/login.py

    # 登入檢查學號密碼功能
    elif (message_text[0:6] == '@user:'):
        reply_user(event,message_text,profile,t_user) # 關於reply_user詳見reply_func/login.py

    #=======================================#
    # 其他功能和測試功能放置處
    elif(message_text == '@其他'):
        reply_other(event,mode_id)

    # 包含我的email和客訴google表單
    elif(message_text == '@聯絡我們'):
        reply_contact(event)

    # 夜讀區所在地點
    elif(message_text == '@地點'):
        reply_location(event)

    # 夜讀區開放時間
    elif(message_text == '@開放時間'):
        reply_openinghours(event)
    
    # 夜讀區規則
    elif(message_text == '@規則'):
        reply_rule(event)

    # 使用說明
    elif(message_text == '@使用說明'):
        reply_instruction(event)

    # 常見問題
    elif(message_text == '@常見問題'):
        reply_faq(event)
    
#==================================================================================================# 
# 以下是line bot處理使用者點擊按鈕等PostbackEvent的大區塊 #
#==================================================================================================#
@handler.add(PostbackEvent)
def handle_postback(event):
    data = dict(parse_qsl(event.postback.data))
    profile = line_bot_api.get_profile(event.source.user_id)
    #print(data)

    # 原本設計要有兩種模式(seat_mode跟time_mode)，但後來因為時間關係，只做了一種(time_mode)
    """
    if data.get('action') == "choose_mode":
        date = data.get('date')
        choose_mode(event,date)
    """
    #=======================================#
    # 以下為選擇開始時間的區塊
    # 由choose_date(event)的Postback(action=time_mode)而來
    if data.get('action') == 'time_mode':
        choose_start_time1720(event) # 預約choose_start_time1720詳見reply_func/reserv_func_v2.py

    elif data.get('action') == 'choose_start_time2123':
        choose_start_time2123(event)
    #=======================================#
    # 以下為選擇結束時間的區塊
    elif data.get('action') == 'choose_end_time':
        choose_end_time(event)

    elif data.get('action') == 'choose_end_time2123':
        choose_end_time2123(event,data.get("start_time_index"),data.get('date'))

    elif data.get('action') == 'choose_end_time0004':
        choose_end_time0004(event,data.get("start_time_index"),data.get('date'))

    elif data.get('action') == 'choose_end_time0508':
        choose_end_time0508(event,data.get("start_time_index"),data.get('date'))
    #=======================================#
    
    # 由choose_date(event)的Postback(action=choose_seat_area)來
    elif data.get('action') == 'choose_seat_area':
        #print(f"check_time_length(event)={check_time_length(event)}")
        #print(f"check_double_booking(event,profile)={check_double_booking(event,profile)}")

        if(check_time_length(event) and check_double_booking(event,profile)): # 檢查預約時間長度和是否有重複預約
            # 選擇要預約的座位區域
            choose_seat_area(event) # 預約choose_seat_area詳見reply_func/reserv_func_v2.py

        elif(check_time_length(event) == False):
            text_message = TextSendMessage(text='⚠️單次預約不得超過8小時!')
            text_message_2 = TextSendMessage(text='請重新預約!')
            line_bot_api.reply_message(
                event.reply_token,
                [text_message,text_message_2])
        
        elif(check_double_booking(event,profile) == False):
            text_message = TextSendMessage(text='⚠️您該時段已有預約!')
            line_bot_api.reply_message(
                event.reply_token,
                text_message)

    

    #=======================================#
    # 由choose_seat_area(event)的Postback(action=choose_B_seat等等)而來           
    # 關於choose_B_seat()、choose_C_seat()、choose_D_seat()、choose_E_seat()，詳見reply_func/reserv_func_v2.py

    elif data.get('action') == 'B_area':
        choose_B_seat(event) 
    elif data.get('action') == 'C_area':
        choose_C_seat(event)
    elif data.get('action') == 'D_area':
        choose_D_seat(event)
    elif data.get('action') == 'E_area':
        choose_E_seat(event)

    
    
    #=======================================#
    elif data.get('action') == 'comfirm_reserv':
        confirm_reserv(event)
    
    elif data.get('action') == 'commit_reserv':
        commit_reserv(event)
    
    elif data.get('action') == 'cancel_reserv':
        user = User.query.filter(User.line_id == profile.user_id).first()
        cancel_reserv(event,user)

    #print(f"action: {data.get('action')}")
    #print(f"date: {data.get('date')}")



if __name__ == "__main__":
    app.run()