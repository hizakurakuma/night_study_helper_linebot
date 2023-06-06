from extensions import *
from user import *
from line_bot_api import *
import datetime as dt
#from datetime import date, datetime, time ,timedelta


def choose_date(event):
    quick_reply_buttons = []
    today = dt.datetime.today().date()

    for d in range(3):
        day = today + dt.timedelta(days=d)
        quick_reply_buttons.append(
            QuickReplyButton(
                action=PostbackAction(label=day.strftime("%m/%d"), text = "選擇 "+day.strftime("%m/%d") , data=f"action=choose_mode&date={day.strftime('%m/%d')}")
            )
        )

    text_message = TextSendMessage(
        text='請選擇日期',
        quick_reply=QuickReply(items=quick_reply_buttons)
    )
    line_bot_api.reply_message(
        event.reply_token,
        text_message
    )


def choose_mode(event,date):
    quick_reply_buttons = [
        QuickReplyButton(
        action=PostbackAction(label="選擇座位", text='先選擇座位',data=f"action=seat_mode&date={date}")),
        QuickReplyButton(
        action=PostbackAction(label="選擇時間", text ='先選擇時間',data=f"action=time_mode&date={date}"))
        ]
    text_message = TextSendMessage(
        text='請選擇模式',
        quick_reply=QuickReply(
            items=quick_reply_buttons
        )
    )
    line_bot_api.reply_message(
        event.reply_token,
        text_message
    )

#==================================================================================================#  
def choose_seat_area(event):
    data = dict(parse_qsl(event.postback.data))
    print("=============seat_area=============")
    print(data)
    quick_reply_buttons = [
        QuickReplyButton(
        action=PostbackAction(label="B區", text = "選擇 B區" ,data=f"action=B_area&date={data['date']}")),
        QuickReplyButton(
        action=PostbackAction(label="C區", text = "選擇 C區" ,data=f"action=C_area&date={data['date']}")),
        QuickReplyButton(
        action=PostbackAction(label="D區", text = "選擇 D區" , data=f"action=D_area&date={data['date']}")),
        QuickReplyButton(
        action=PostbackAction(label="E區", text = "選擇 E區" , data=f"action=E_area&date={data['date']}"))
        ]
    text_message = TextSendMessage(
        text='請選擇座位區域',
        quick_reply=QuickReply(
            items=quick_reply_buttons
        )
    )
    line_bot_api.reply_message(
        event.reply_token,
        text_message
    )


def choose_B_seat(event):
    data = dict(parse_qsl(event.postback.data))
    quick_reply_buttons = [
        QuickReplyButton(
        action=PostbackAction(label="M040", text = "選擇 M040" ,data=f"action=select_seat_time&date={data['date']}&seat=M040")),
        QuickReplyButton(
        action=PostbackAction(label="M041", text = "選擇 M041" ,data=f"action=select_seat_time&date={data['date']}&seat=M041")),
        QuickReplyButton(
        action=PostbackAction(label="M042", text = "選擇 M042" ,data=f"action=select_seat_time&date={data['date']}&seat=M042")),
        QuickReplyButton(
        action=PostbackAction(label="M043", text = "選擇 M043" ,data=f"action=select_seat_time&date={data['date']}&seat=M043")),
        QuickReplyButton(
        action=PostbackAction(label="M044", text = "選擇 M044" ,data=f"action=select_seat_time&date={data['date']}&seat=M044")),
        QuickReplyButton(
        action=PostbackAction(label="M045", text = "選擇 M045" ,data=f"action=select_seat_time&date={data['date']}&seat=M045")),
        QuickReplyButton(
        action=PostbackAction(label="M046", text = "選擇 M046" ,data=f"action=select_seat_time&date={data['date']}&seat=M046")),
        QuickReplyButton(
        action=PostbackAction(label="M047", text = "選擇 M047" ,data=f"action=select_seat_time&date={data['date']}&seat=M047")),
        QuickReplyButton(
        action=PostbackAction(label="M048", text = "選擇 M048" ,data=f"action=select_seat_time&date={data['date']}&seat=M048")),
        QuickReplyButton(
        action=PostbackAction(label="M049", text = "選擇 M049" ,data=f"action=select_seat_time&date={data['date']}&seat=M049")),
        QuickReplyButton(
        action=PostbackAction(label="M050", text = "選擇 M050" ,data=f"action=select_seat_time&date={data['date']}&seat=M050")),
        ]
    text_message = TextSendMessage(
        text='請選擇座位',
        quick_reply=QuickReply(
            items=quick_reply_buttons
        )
    )
    line_bot_api.reply_message(
        event.reply_token,
        text_message
    )

def choose_C_seat(event):
    data = dict(parse_qsl(event.postback.data))
    quick_reply_buttons = [
        QuickReplyButton(
        action=PostbackAction(label="M080", text = "選擇 M080" ,data=f"action=select_seat_time&date={data['date']}&seat=M080")),
        QuickReplyButton(
        action=PostbackAction(label="M081", text = "選擇 M081" ,data=f"action=select_seat_time&date={data['date']}&seat=M081")),
        QuickReplyButton(
        action=PostbackAction(label="M082", text = "選擇 M082" ,data=f"action=select_seat_time&date={data['date']}&seat=M082")),
        QuickReplyButton(
        action=PostbackAction(label="M083", text = "選擇 M083" ,data=f"action=select_seat_time&date={data['date']}&seat=M083")),
        QuickReplyButton(
        action=PostbackAction(label="M084", text = "選擇 M084" ,data=f"action=select_seat_time&date={data['date']}&seat=M084")),
        QuickReplyButton(
        action=PostbackAction(label="M085", text = "選擇 M085" ,data=f"action=select_seat_time&date={data['date']}&seat=M085")),
        QuickReplyButton(
        action=PostbackAction(label="M086", text = "選擇 M086" ,data=f"action=select_seat_time&date={data['date']}&seat=M086")),
        QuickReplyButton(
        action=PostbackAction(label="M087", text = "選擇 M087" ,data=f"action=select_seat_time&date={data['date']}&seat=M087")),
        QuickReplyButton(
        action=PostbackAction(label="M088", text = "選擇 M088" ,data=f"action=select_seat_time&date={data['date']}&seat=M088")),
        QuickReplyButton(
        action=PostbackAction(label="M089", text = "選擇 M089" ,data=f"action=select_seat_time&date={data['date']}&seat=M089")),
        QuickReplyButton(
        action=PostbackAction(label="M090", text = "選擇 M090" ,data=f"action=select_seat_time&date={data['date']}&seat=M090")),
        ]
    text_message = TextSendMessage(
        text='請選擇座位',
        quick_reply=QuickReply(
            items=quick_reply_buttons
        )
    )
    line_bot_api.reply_message(
        event.reply_token,
        text_message
    )

def choose_D_seat(event):
    data = dict(parse_qsl(event.postback.data))
    quick_reply_buttons = [
        QuickReplyButton(
        action=PostbackAction(label="M120", text = "選擇 M120" ,data=f"action=select_seat_time&date={data['date']}&seat=M120")),
        QuickReplyButton(
        action=PostbackAction(label="M121", text = "選擇 M121" ,data=f"action=select_seat_time&date={data['date']}&seat=M121")),
        QuickReplyButton(
        action=PostbackAction(label="M122", text = "選擇 M122" ,data=f"action=select_seat_time&date={data['date']}&seat=M122")),
        QuickReplyButton(
        action=PostbackAction(label="M123", text = "選擇 M123" ,data=f"action=select_seat_time&date={data['date']}&seat=M123")),
        QuickReplyButton(
        action=PostbackAction(label="M124", text = "選擇 M124" ,data=f"action=select_seat_time&date={data['date']}&seat=M124")),
        QuickReplyButton(
        action=PostbackAction(label="M125", text = "選擇 M125" ,data=f"action=select_seat_time&date={data['date']}&seat=M125")),
        QuickReplyButton(
        action=PostbackAction(label="M126", text = "選擇 M126" ,data=f"action=select_seat_time&date={data['date']}&seat=M126")),
        QuickReplyButton(
        action=PostbackAction(label="M127", text = "選擇 M127" ,data=f"action=select_seat_time&date={data['date']}&seat=M127")),
        QuickReplyButton(
        action=PostbackAction(label="M128", text = "選擇 M128" ,data=f"action=select_seat_time&date={data['date']}&seat=M128")),
        QuickReplyButton(
        action=PostbackAction(label="M129", text = "選擇 M129" ,data=f"action=select_seat_time&date={data['date']}&seat=M129")),
        QuickReplyButton(
        action=PostbackAction(label="M130", text = "選擇 M130" ,data=f"action=select_seat_time&date={data['date']}&seat=M130")),
        ]
    text_message = TextSendMessage(
        text='請選擇座位',
        quick_reply=QuickReply(
            items=quick_reply_buttons
        )
    )
    line_bot_api.reply_message(
        event.reply_token,
        text_message
    )

def choose_E_seat(event):
    data = dict(parse_qsl(event.postback.data))
    quick_reply_buttons = [
        QuickReplyButton(
        action=PostbackAction(label="M160", text = "選擇 M160" ,data=f"action=select_seat_time&date={data['date']}&seat=M160")),
        QuickReplyButton(
        action=PostbackAction(label="M161", text = "選擇 M161" ,data=f"action=select_seat_time&date={data['date']}&seat=M161")),
        QuickReplyButton(
        action=PostbackAction(label="M162", text = "選擇 M162" ,data=f"action=select_seat_time&date={data['date']}&seat=M162")),
        QuickReplyButton(
        action=PostbackAction(label="M163", text = "選擇 M163" ,data=f"action=select_seat_time&date={data['date']}&seat=M163")),
        QuickReplyButton(
        action=PostbackAction(label="M164", text = "選擇 M164" ,data=f"action=select_seat_time&date={data['date']}&seat=M164")),
        QuickReplyButton(
        action=PostbackAction(label="M165", text = "選擇 M165" ,data=f"action=select_seat_time&date={data['date']}&seat=M165")),
        QuickReplyButton(
        action=PostbackAction(label="M166", text = "選擇 M166" ,data=f"action=select_seat_time&date={data['date']}&seat=M166")),
        QuickReplyButton(
        action=PostbackAction(label="M167", text = "選擇 M167" ,data=f"action=select_seat_time&date={data['date']}&seat=M167")),
        QuickReplyButton(
        action=PostbackAction(label="M168", text = "選擇 M168" ,data=f"action=select_seat_time&date={data['date']}&seat=M168")),
        QuickReplyButton(
        action=PostbackAction(label="M169", text = "選擇 M169" ,data=f"action=select_seat_time&date={data['date']}&seat=M169")),
        QuickReplyButton(
        action=PostbackAction(label="M170", text = "選擇 M170" ,data=f"action=select_seat_time&date={data['date']}&seat=M170")),
        ]
    text_message = TextSendMessage(
        text='請選擇座位',
        quick_reply=QuickReply(
            items=quick_reply_buttons
        )
    )
    line_bot_api.reply_message(
        event.reply_token,
        text_message
    )

#==================================================================================================#  
def choose_start_time1720(event):
    data = dict(parse_qsl(event.postback.data))
    quick_reply_buttons = []
    for t in range(17,21):
        quick_reply_buttons.append(
            QuickReplyButton(
                action=PostbackAction(label=f"{t}:00", text = f"選擇 {t}:00",data=f"action=choose_end_time&date={data['date']}&start_time={t}:00"))
        )
        quick_reply_buttons.append(
            QuickReplyButton(
                action=PostbackAction(label=f"{t}:30", text = f"選擇 {t}:30",data=f"action=choose_end_time&date={data['date']}&start_time={t}:30"))
        )

    quick_reply_buttons.append(
            QuickReplyButton(
                action=PostbackAction(label="下一頁", data=f"action=choose_start_time2123&date={data['date']}"))
        )
    text_message = TextSendMessage(
        text='請選擇開始時間\n(17:00~20:30)',
        quick_reply=QuickReply(items=quick_reply_buttons)
    )
    line_bot_api.reply_message(
        event.reply_token,
        text_message
    )

def choose_start_time2123(event):
    data = dict(parse_qsl(event.postback.data))
    quick_reply_buttons = []
    for t in range(21,24):
        quick_reply_buttons.append(
            QuickReplyButton(
                action=PostbackAction(label=f"{t}:00", text = f"選擇 {t}:00",data=f"action=choose_end_time&date={data['date']}&start_time={t}:00"))
        )
        quick_reply_buttons.append(
            QuickReplyButton(
                action=PostbackAction(label=f"{t}:30", text = f"選擇 {t}:30",data=f"action=choose_end_time&date={data['date']}&start_time={t}:30"))
        )
    text_message = TextSendMessage(
        text='請選擇開始時間\n(21:00~23:30)',
        quick_reply=QuickReply(items=quick_reply_buttons)
    )
    line_bot_api.reply_message(
        event.reply_token,
        text_message
    )

def choose_end_time(event):
    data = dict(parse_qsl(event.postback.data))
    date = data.get('date')
    start_time = data['start_time']
    start_time_find = ['17:00','17:30','18:00','18:30','19:00','19:30','20:00','20:30','21:00','21:30','22:00'\
        ,'22:30','23:00','23:30','00:00','00:30','01:00','01:30','02:00','02:30','03:00','03:30','04:00',\
            '04:30','05:00','05:30','06:00','06:30','07:00','07:30','08:00','08:30']
    start_time_index = start_time_find.index(start_time)
    print(f"start_time_index={start_time_index}")

    if(start_time_index<8):
        choose_end_time1720(event,start_time_index,date)
    elif(start_time_index<14):
        choose_end_time2123(event,start_time_index,date)
    elif(start_time_index<24):
        choose_end_time0004(event,start_time_index,date)
    else:
        choose_end_time0508(event,start_time_index,date)

    
def choose_end_time1720(event,start_time_index,date):
    data = dict(parse_qsl(event.postback.data))
    end_time_all = ['17:29','17:59','18:29','18:59','19:29','19:59','20:29','20:59','21:29','21:59','22:29'\
        ,'22:59','23:29','23:59','00:29','00:59','01:29','01:59','02:29','02:59','03:29','03:59','04:29',\
            '04:59','05:29','05:59','06:29','06:59','07:29','07:59','08:29','08:59']
    endtime = end_time_all[start_time_index:8]
    quick_reply_buttons = []
    for t in endtime:
        quick_reply_buttons.append(
            QuickReplyButton(
                action=PostbackAction(label=t, text =f'選擇 {t}',data=f"action=choose_avail_seat&date={date}&start_time={data['start_time']}&end_time={t}&next_day={False}"))
        )
    quick_reply_buttons.append(
            QuickReplyButton(
                action=PostbackAction(label="下一頁", data=f"action=choose_end_time2123&date={date}&start_time={data['start_time']}&start_time_index={start_time_index}&next_day={False}"))
        )
    text_message = TextSendMessage(
        text='請選擇結束時間\n(17:29~20:59)',
        quick_reply=QuickReply(items=quick_reply_buttons)
    )
    line_bot_api.reply_message(
        event.reply_token,
        text_message
    )
#=======================================#
def choose_end_time2123(event,start_time_index,date):
    data = dict(parse_qsl(event.postback.data))
    end_time_all = ['17:29','17:59','18:29','18:59','19:29','19:59','20:29','20:59','21:29','21:59','22:29'\
        ,'22:59','23:29','23:59','00:29','00:59','01:29','01:59','02:29','02:59','03:29','03:59','04:29',\
            '04:59','05:29','05:59','06:29','06:59','07:29','07:59','08:29','08:59']
    if(int(start_time_index)<8):
        begin_index = 8
    else:
        begin_index = int(start_time_index)
    endtime = end_time_all[begin_index:14]
    quick_reply_buttons = []
    for t in endtime:
        quick_reply_buttons.append(
            QuickReplyButton(
                action=PostbackAction(label=t, text = f'選擇 {t}',data=f"action=choose_avail_seat&date={date}&start_time={data['start_time']}&end_time={t}&next_day={False}"))
        )
    quick_reply_buttons.append(
            QuickReplyButton(
                action=PostbackAction(label="下一頁", data=f"action=choose_end_time0004&date={date}&start_time={data['start_time']}&start_time_index={start_time_index}&next_day={True}"))
        )
    text_message = TextSendMessage(
        text='請選擇結束時間\n(21:29~23:59)',
        quick_reply=QuickReply(items=quick_reply_buttons)
    )
    line_bot_api.reply_message(
        event.reply_token,
        text_message
    )

def choose_end_time0004(event,start_time_index,date):
    data = dict(parse_qsl(event.postback.data))
    date_lst = date.split('/')
    year = dt.datetime.now().year
    date_next = dt.date(year, int(date_lst[0]), int(date_lst[0])) + dt.timedelta(days=1)
    date_next = date_next.strftime("%m/%d")
    end_time_all = ['17:29','17:59','18:29','18:59','19:29','19:59','20:29','20:59','21:29','21:59','22:29'\
        ,'22:59','23:29','23:59','00:29','00:59','01:29','01:59','02:29','02:59','03:29','03:59','04:29',\
            '04:59','05:29','05:59','06:29','06:59','07:29','07:59','08:29','08:59']
    if(int(start_time_index)<14):
        begin_index = 14
    else:
        begin_index = int(start_time_index)
    endtime = end_time_all[begin_index:24]
    quick_reply_buttons = []
    for t in endtime:
        if(t=='00:29'):
            quick_reply_buttons.append(
                QuickReplyButton(
                    action=PostbackAction(label=f'{date_next} {t}', text =f'選擇 {date_next} {t}',data=f"action=choose_avail_seat&date={date_next}&start_time={data['start_time']}&end_time={t}&next_day={True}"))
            )
        else:
            quick_reply_buttons.append(
                QuickReplyButton(
                    action=PostbackAction(label=t, text = f'選擇 {t}',data=f"action=choose_avail_seat&date={date}&start_time={data['start_time']}&end_time={t}&next_day={True}"))
            )
    quick_reply_buttons.append(
            QuickReplyButton(
                action=PostbackAction(label="下一頁", data=f"action=choose_end_time0508&date={date}&start_time={data['start_time']}&start_time_index={start_time_index}&next_day={True}"))
        )
    text_message = TextSendMessage(
        text=f'請選擇結束時間\n({date_next} 00:29~04:59)',
        quick_reply=QuickReply(items=quick_reply_buttons)
    )
    line_bot_api.reply_message(
        event.reply_token,
        text_message
    )

def choose_end_time0508(event,start_time_index,date):
    data = dict(parse_qsl(event.postback.data))
    year = dt.datetime.now().year
    date_next = date(year, int(date.split('/')[0]), int(date.split('/')[1])) + dt.timedelta(days=1)
    date_next = date_next.strftime("%m/%d")
    end_time_all = ['17:29','17:59','18:29','18:59','19:29','19:59','20:29','20:59','21:29','21:59','22:29'\
        ,'22:59','23:29','23:59','00:29','00:59','01:29','01:59','02:29','02:59','03:29','03:59','04:29',\
            '04:59','05:29','05:59','06:29','06:59','07:29','07:59','08:29','08:59']
    if(int(start_time_index)<24):
        begin_index = 24
    else:
        begin_index = int(start_time_index)
    endtime = end_time_all[begin_index:]
    quick_reply_buttons = []
    for t in endtime:
        quick_reply_buttons.append(
            QuickReplyButton(
                action=PostbackAction(label=t, text = f'選擇 {t}',data=f"action=choose_avail_seat&date={date}&start_time={data['start_time']}&end_time={t}&next_day={True}"))
        )
    text_message = TextSendMessage(
        text=f'請選擇結束時間\n({date_next} 05:29~08:59)',
        quick_reply=QuickReply(items=quick_reply_buttons)
    )
    line_bot_api.reply_message(
        event.reply_token,
        text_message
    )
#=======================================#
def choose_avail_seat(event):
    pass