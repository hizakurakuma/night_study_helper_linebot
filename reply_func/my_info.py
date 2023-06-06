from extensions import *
from user import *
from reserve import *
from line_bot_api import *
import datetime as dt

# 根據座位號碼seat_num，回傳座位所在區域
def seat_area(seat_num):
    seat_num = int(seat_num[1:])
    if(seat_num<80):
        return 'B'
    elif(seat_num<120):
        return 'C'
    elif(seat_num<160):
        return 'D'
    else:
        return 'E'

# 產生預約資訊的flex message
def reserv_info_message(seat_num,start_time,end_time,reserv_num=1):
    seatarea = seat_area(seat_num)
    start_time = start_time.strftime("%Y-%m-%d %H:%M")
    end_time = end_time.strftime("%Y-%m-%d %H:%M")
    true = True
    flex_message = FlexSendMessage(
        alt_text='您的預約資料',
        contents={
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": f"您的預約_{str(reserv_num)}",
                    "weight": "bold",
                    "size": "xl"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "lg",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "空間",
                            "color": "#aaaaaa",
                            "size": "sm",
                            "flex": 1
                        },
                        {
                            "type": "text",
                            "text": f"4F-夜讀區{seatarea}",
                            "wrap": true,
                            "color": "#666666",
                            "size": "sm",
                            "flex": 5
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "座位",
                            "color": "#aaaaaa",
                            "size": "sm",
                            "flex": 1
                        },
                        {
                            "type": "text",
                            "text": f"{seat_num}",
                            "wrap": true,
                            "color": "#666666",
                            "size": "sm",
                            "flex": 5
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "預約時間",
                            "color": "#aaaaaa",
                            "size": "sm",
                            "flex": 1
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": f"{start_time}~{end_time}",
                            "color": "#666666",
                            "size": "xs",
                            "flex": 1
                        }
                        ]
                    }
                    ]
                }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "action": {
                    "type": "postback",
                    "label": "取消預約",
                    "data": f"action=cancel_reserv&reserv={str(reserv_num)}",
                    "displayText": "取消預約"
                    }
                }
                ],
                "flex": 0
            }
            }
        )
    return flex_message

# 查看我的預約資訊
def my_reserv(event,profile,user,text_message):
    reply_lst = []
    #text_message = TextSendMessage(text=f'您好，{name}同學')
    reply_lst.append(text_message)
    reserv_count = user.reserv_count
    if(reserv_count == 0):
        text_message_2 = TextSendMessage(text='您目前沒有預約')
        reply_lst.append(text_message_2)
    else:
        if(user.reserv_1_seat != None):
            seat_num = user.reserv_1_seat
            start_time = user.reserv_1_starttime
            end_time = user.reserv_1_endtime
            flex_message = reserv_info_message(seat_num,start_time,end_time)
            reply_lst.append(flex_message)
        if(user.reserv_2_seat != None):
            seat_num = user.reserv_2_seat
            start_time = user.reserv_2_starttime
            end_time = user.reserv_2_endtime
            flex_message = reserv_info_message(seat_num,start_time,end_time,2)
            reply_lst.append(flex_message)
        if(user.reserv_3_seat != None):
            seat_num = user.reserv_3_seat
            start_time = user.reserv_3_starttime
            end_time = user.reserv_3_endtime
            flex_message = reserv_info_message(seat_num,start_time,end_time,3)
            reply_lst.append(flex_message)

    line_bot_api.reply_message(
        event.reply_token,
        reply_lst
    )