from extensions import *
from user import *
from reserve import *
from line_bot_api import *
import datetime as dt
#from datetime import date, datetime, time ,timedelta

seat_lst = ['M040', 'M041', 'M042', 'M043', 'M044', 'M045', 'M046', 'M047', 'M048', 'M049', 'M050', 'M080', 'M081', 'M082', 'M083', 'M084', 'M085', 'M086', 'M087', 'M088', 'M089', 'M090', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M160', 'M161', 'M162', 'M163', 'M164', 'M165', 'M166', 'M167', 'M168', 'M169', 'M170']


def choose_date(event):
    quick_reply_buttons = []
    today = dt.date.today()
    day_1 = today

    for d in range(3):
        day = today + dt.timedelta(days=d)
        if(day.year == day_1.year):
            quick_reply_buttons.append(
            QuickReplyButton(
                action=PostbackAction(label=day.strftime("%m/%d"), text = "選擇 "+day.strftime("%m/%d") , data=f"action=time_mode&date={day.strftime('%Y-%m-%d')}")
            )
        )
        else:
            quick_reply_buttons.append(
                QuickReplyButton(
                    action=PostbackAction(label=day.strftime("%Y %m/%d"), text = "選擇 "+day.strftime("%Y %m/%d") , data=f"action=time_mode&date={day.strftime('%Y-%m-%d')}")
                )
            )
    quick_reply_buttons.append(
                QuickReplyButton(
                    action=PostbackAction(label='取消', text = '取消' ,data='action=cancel')
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
    #print(f"start_time_index={start_time_index}")

    if(start_time_index<8):
        choose_end_time1720(event,start_time_index,date)
    elif(start_time_index<14):
        choose_end_time2123(event,start_time_index,date)
    elif(start_time_index<24):
        choose_end_time0004(event,start_time_index,date)
    else:
        choose_end_time0508(event,start_time_index,date)

#=======================================#
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
                action=PostbackAction(label=t, text =f'選擇 {t}',data=f"action=choose_seat_area&date={date}&start_time={data['start_time']}&end_time={t}&next_day={False}"))
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
                action=PostbackAction(label=t, text = f'選擇 {t}',data=f"action=choose_seat_area&date={date}&start_time={data['start_time']}&end_time={t}&next_day={False}"))
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
    date_lst = date.split('-')
    date_next_dt = dt.date(int(date_lst[0]), int(date_lst[1]), int(date_lst[2])) + dt.timedelta(days=1)
    if(date_next_dt.year == int(date_lst[0])):
        date_next = date_next_dt.strftime("%m/%d")
    else:
        date_next = date_next_dt.strftime("%Y %m/%d")
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
                    action=PostbackAction(label=f'{date_next} {t}', text =f'選擇 {date_next} {t}',data=f"action=choose_seat_area&date={date}&start_time={data['start_time']}&end_time={t}&next_day={True}"))
            )
        else:
            quick_reply_buttons.append(
                QuickReplyButton(
                    action=PostbackAction(label=t, text = f'選擇 {t}',data=f"action=choose_seat_area&date={date}&start_time={data['start_time']}&end_time={t}&next_day={True}"))
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
    date_lst = date.split('-')
    date_next_dt = dt.date(int(date_lst[0]), int(date_lst[1]), int(date_lst[2])) + dt.timedelta(days=1)
    if(date_next_dt.year == int(date_lst[0])):
        date_next = date_next_dt.strftime("%m/%d")
    else:
        date_next = date_next_dt.strftime("%Y %m/%d")
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
                action=PostbackAction(label=t, text = f'選擇 {t}',data=f"action=choose_seat_area&date={date}&start_time={data['start_time']}&end_time={t}&next_day={True}"))
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
def check_time_length(event):
    data = dict(parse_qsl(event.postback.data))
    start_time_str = data.get('date')+' '+data.get('start_time')
    start_time_dt = dt.datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
    if(data.get('next_day') == 'True'):
        date_next = dt.date(start_time_dt.year, start_time_dt.month, start_time_dt.day) + dt.timedelta(days=1)
        date_next = date_next.strftime('%Y-%m-%d')
        end_time_str = date_next +' '+data.get('end_time')
    else:
        end_time_str = data.get('date') +' '+data.get('end_time')

    end_time_dt = dt.datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")
        
    delta = end_time_dt - start_time_dt
    delta_max = dt.timedelta(hours=8)
    
    if(delta<=delta_max):
        return True
    else:
        return False

def check_double_booking(event,profile):
    data = dict(parse_qsl(event.postback.data))
    start_time_str = data.get('date')+' '+data.get('start_time')
    start_time_dt = dt.datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
    if(data.get('next_day') == 'True'):
        date_next = dt.date(start_time_dt.year, start_time_dt.month, start_time_dt.day) + dt.timedelta(days=1)
        date_next = date_next.strftime('%Y-%m-%d')
        end_time_str = date_next +' '+data.get('end_time')
    else:
        end_time_str = data.get('date') +' '+data.get('end_time')
    end_time_dt = dt.datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")
    user = User.query.filter(User.line_id == profile.user_id).first()
    if(user.reserv_count == 0):
        return True
    else:
        if(user.reserv_1_seat != None):
            if(user.reserv_1_starttime <= start_time_dt <= user.reserv_1_endtime):
                return False
            elif(user.reserv_1_starttime<= end_time_dt <= user.reserv_1_endtime):
                return False
            else:
                return True
        elif(user.reserv_2_seat != None):
            if(user.reserv_2_starttime<= start_time_dt <= user.reserv_2_endtime):
                return False
            elif(user.reserv_2_starttime<= end_time_dt <= user.reserv_2_endtime):
                return False
            else:
                return True
        elif(user.reserv_3_seat != None):
            if(user.reserv_3_starttime<= start_time_dt <= user.reserv_3_endtime):
                return False
            elif(user.reserv_3_starttime<= end_time_dt <= user.reserv_3_endtime):
                return False
            else:
                return True
        else:
            return True
        
#==================================================================================================#  

def choose_seat_area(event):
    data = dict(parse_qsl(event.postback.data))
    #print("=============seat_area=============")
    #print(data)
    quick_reply_buttons = [
        QuickReplyButton(
        action=PostbackAction(label="B區", text = "選擇 B區" ,data=f"action=B_area&date={data['date']}&start_time={data['start_time']}&end_time={data['end_time']}&next_day={data['next_day']}")),
        QuickReplyButton(
        action=PostbackAction(label="C區", text = "選擇 C區" ,data=f"action=C_area&date={data['date']}&start_time={data['start_time']}&end_time={data['end_time']}&next_day={data['next_day']}")),
        QuickReplyButton(
        action=PostbackAction(label="D區", text = "選擇 D區" , data=f"action=D_area&date={data['date']}&start_time={data['start_time']}&end_time={data['end_time']}&next_day={data['next_day']}")),
        QuickReplyButton(
        action=PostbackAction(label="E區", text = "選擇 E區" , data=f"action=E_area&date={data['date']}&start_time={data['start_time']}&end_time={data['end_time']}&next_day={data['next_day']}"))
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
#=======================================#
seat_key_lst = ['id', 'seat_num', 'day_1_00_00', 'day_1_00_30', 'day_1_01_00', 'day_1_01_30', 'day_1_02_00', 'day_1_02_30', 'day_1_03_00', 'day_1_03_30', 'day_1_04_00', 'day_1_04_30', 'day_1_05_00', 'day_1_05_30', 'day_1_06_00', 'day_1_06_30', 'day_1_07_00', 'day_1_07_30', 'day_1_08_00', 'day_1_08_30', 'day_1_17_00', 'day_1_17_30', 'day_1_18_00', 'day_1_18_30', 'day_1_19_00', 'day_1_19_30', 'day_1_20_00', 'day_1_20_30', 'day_1_21_00', 'day_1_21_30', 'day_1_22_00', 'day_1_22_30', 'day_1_23_00', 'day_1_23_30', 'day_2_00_00', 'day_2_00_30', 'day_2_01_00', 'day_2_01_30', 'day_2_02_00', 'day_2_02_30', 'day_2_03_00', 'day_2_03_30', 'day_2_04_00', 'day_2_04_30', 'day_2_05_00', 'day_2_05_30', 'day_2_06_00', 'day_2_06_30', 'day_2_07_00', 'day_2_07_30', 'day_2_08_00', 'day_2_08_30', 'day_2_17_00', 'day_2_17_30', 'day_2_18_00', 'day_2_18_30', 'day_2_19_00', 'day_2_19_30', 'day_2_20_00', 'day_2_20_30', 'day_2_21_00', 'day_2_21_30', 'day_2_22_00', 'day_2_22_30', 'day_2_23_00', 'day_2_23_30', 'day_3_00_00', 'day_3_00_30', 'day_3_01_00', 'day_3_01_30', 'day_3_02_00', 'day_3_02_30', 'day_3_03_00', 'day_3_03_30', 'day_3_04_00', 'day_3_04_30', 'day_3_05_00', 'day_3_05_30', 'day_3_06_00', 'day_3_06_30', 'day_3_07_00', 'day_3_07_30', 'day_3_08_00', 'day_3_08_30', 'day_3_17_00', 'day_3_17_30', 'day_3_18_00', 'day_3_18_30', 'day_3_19_00', 'day_3_19_30', 'day_3_20_00', 'day_3_20_30', 'day_3_21_00', 'day_3_21_30', 'day_3_22_00', 'day_3_22_30', 'day_3_23_00', 'day_3_23_30', 'day_4_00_00', 'day_4_00_30', 'day_4_01_00', 'day_4_01_30', 'day_4_02_00', 'day_4_02_30', 'day_4_03_00', 'day_4_03_30', 'day_4_04_00', 'day_4_04_30', 'day_4_05_00', 'day_4_05_30', 'day_4_06_00', 'day_4_06_30', 'day_4_07_00', 'day_4_07_30', 'day_4_08_00', 'day_4_08_30', 'day_4_17_00', 'day_4_17_30', 'day_4_18_00', 'day_4_18_30', 'day_4_19_00', 'day_4_19_30', 'day_4_20_00', 'day_4_20_30', 'day_4_21_00', 'day_4_21_30', 'day_4_22_00', 'day_4_22_30', 'day_4_23_00', 'day_4_23_30', 'day_5_00_00', 'day_5_00_30', 'day_5_01_00', 'day_5_01_30', 'day_5_02_00', 'day_5_02_30', 'day_5_03_00', 'day_5_03_30', 'day_5_04_00', 'day_5_04_30', 'day_5_05_00', 'day_5_05_30', 'day_5_06_00', 'day_5_06_30', 'day_5_07_00', 'day_5_07_30', 'day_5_08_00', 'day_5_08_30', 'day_5_17_00', 'day_5_17_30', 'day_5_18_00', 'day_5_18_30', 'day_5_19_00', 'day_5_19_30', 'day_5_20_00', 'day_5_20_30', 'day_5_21_00', 'day_5_21_30', 'day_5_22_00', 'day_5_22_30', 'day_5_23_00', 'day_5_23_30']
seat_key_lst_2 =['id', 'seat_num', 'day_1_00_29', 'day_1_00_59', 'day_1_01_29', 'day_1_01_59', 'day_1_02_29', 'day_1_02_59', 'day_1_03_29', 'day_1_03_59', 'day_1_04_29', 'day_1_04_59', 'day_1_05_29', 'day_1_05_59', 'day_1_06_29', 'day_1_06_59', 'day_1_07_29', 'day_1_07_59', 'day_1_08_29', 'day_1_08_59', 'day_1_17_29', 'day_1_17_59', 'day_1_18_29', 'day_1_18_59', 'day_1_19_29', 'day_1_19_59', 'day_1_20_29', 'day_1_20_59', 'day_1_21_29', 'day_1_21_59', 'day_1_22_29', 'day_1_22_59', 'day_1_23_29', 'day_1_23_59', 'day_2_00_29', 'day_2_00_59', 'day_2_01_29', 'day_2_01_59', 'day_2_02_29', 'day_2_02_59', 'day_2_03_29', 'day_2_03_59', 'day_2_04_29', 'day_2_04_59', 'day_2_05_29', 'day_2_05_59', 'day_2_06_29', 'day_2_06_59', 'day_2_07_29', 'day_2_07_59', 'day_2_08_29', 'day_2_08_59', 'day_2_17_29', 'day_2_17_59', 'day_2_18_29', 'day_2_18_59', 'day_2_19_29', 'day_2_19_59', 'day_2_20_29', 'day_2_20_59', 'day_2_21_29', 'day_2_21_59', 'day_2_22_29', 'day_2_22_59', 'day_2_23_29', 'day_2_23_59', 'day_3_00_29', 'day_3_00_59', 'day_3_01_29', 'day_3_01_59', 'day_3_02_29', 'day_3_02_59', 'day_3_03_29', 'day_3_03_59', 'day_3_04_29', 'day_3_04_59', 'day_3_05_29', 'day_3_05_59', 'day_3_06_29', 'day_3_06_59', 'day_3_07_29', 'day_3_07_59', 'day_3_08_29', 'day_3_08_59', 'day_3_17_29', 'day_3_17_59', 'day_3_18_29', 'day_3_18_59', 'day_3_19_29', 'day_3_19_59', 'day_3_20_29', 'day_3_20_59', 'day_3_21_29', 'day_3_21_59', 'day_3_22_29', 'day_3_22_59', 'day_3_23_29', 'day_3_23_59', 'day_4_00_29', 'day_4_00_59', 'day_4_01_29', 'day_4_01_59', 'day_4_02_29', 'day_4_02_59', 'day_4_03_29', 'day_4_03_59', 'day_4_04_29', 'day_4_04_59', 'day_4_05_29', 'day_4_05_59', 'day_4_06_29', 'day_4_06_59', 'day_4_07_29', 'day_4_07_59', 'day_4_08_29', 'day_4_08_59', 'day_4_17_29', 'day_4_17_59', 'day_4_18_29', 'day_4_18_59', 'day_4_19_29', 'day_4_19_59', 'day_4_20_29', 'day_4_20_59', 'day_4_21_29', 'day_4_21_59', 'day_4_22_29', 'day_4_22_59', 'day_4_23_29', 'day_4_23_59', 'day_5_00_29', 'day_5_00_59', 'day_5_01_29', 'day_5_01_59', 'day_5_02_29', 'day_5_02_59', 'day_5_03_29', 'day_5_03_59', 'day_5_04_29', 'day_5_04_59', 'day_5_05_29', 'day_5_05_59', 'day_5_06_29', 'day_5_06_59', 'day_5_07_29', 'day_5_07_59', 'day_5_08_29', 'day_5_08_59', 'day_5_17_29', 'day_5_17_59', 'day_5_18_29', 'day_5_18_59', 'day_5_19_29', 'day_5_19_59', 'day_5_20_29', 'day_5_20_59', 'day_5_21_29', 'day_5_21_59', 'day_5_22_29', 'day_5_22_59', 'day_5_23_29', 'day_5_23_59']

def check_seat(event,seat_id):
    data = dict(parse_qsl(event.postback.data))
    day_select = dt.datetime.strptime(data.get('date'), "%Y-%m-%d")
    today = dt.date.today()
    if(day_select.date() == today):
        day_start = 1
    elif(day_select.date() == today + dt.timedelta(days=1)):
        day_start = 2
    elif(day_select.date() == today + dt.timedelta(days=2)):
        day_start = 3
    else:
        day_start = 4
    if(data.get('next_day') == 'True'):
        day_end = day_start + 1
    else:
        day_end = day_start
    start_time_key = f"day_{day_start}_{data.get('start_time').replace(':','_')}"
    end_time_key = f"day_{day_end}_{data.get('end_time').replace(':','_')}"

    seat = Seat.query.get(seat_id)
    seat_result = seat.get_result_lst()
    for i in range(seat_key_lst.index(start_time_key),seat_key_lst_2.index(end_time_key)+1):
        if(seat_result[i] != '0'):
            return False

    return True


# Seat __init__(self,seat_num,stu_id,day=1,time='00:00'):
def choose_B_seat(event):
    data = dict(parse_qsl(event.postback.data))
    count = 0
    quick_reply_buttons = []
    for i in range(1,12):
        if(check_seat(event,i)):
            quick_reply_buttons.append(
            QuickReplyButton(
            action=PostbackAction(label=f"M{39+i:03d}", text = f"選擇 M{39+i:03d}" ,data=f"action=comfirm_reserv&date={data['date']}&start_time={data['start_time']}&end_time={data['end_time']}&next_day={data['next_day']}&seat=M{39+i:03d}")))
            count += 1

    quick_reply_buttons.append(
        QuickReplyButton(
        action=PostbackAction(label="回上一步", text = "回上一步" ,data=f"action=choose_seat_area&date={data['date']}&start_time={data['start_time']}&end_time={data['end_time']}&next_day={data['next_day']}")))
    if(count == 0):
        text_message = TextSendMessage(
            text=f'抱歉，您所選擇的時間B區已無座位',
            quick_reply=QuickReply(items=quick_reply_buttons)
        )
    else:
        text_message = TextSendMessage(
            text=f'請選擇B區座位',
            quick_reply=QuickReply(items=quick_reply_buttons)
        )

    line_bot_api.reply_message(
        event.reply_token,
        text_message
    )

def choose_C_seat(event):
    data = dict(parse_qsl(event.postback.data))
    count = 0
    quick_reply_buttons = []
    for i in range(1,12):
        if(check_seat(event,i+11)):
            quick_reply_buttons.append(
            QuickReplyButton(
            action=PostbackAction(label=f"M{79+i:03d}", text = f"選擇 M{79+i:03d}" ,data=f"action=comfirm_reserv&date={data['date']}&start_time={data['start_time']}&end_time={data['end_time']}&next_day={data['next_day']}&seat=M{79+i:03d}")))
            count += 1

    quick_reply_buttons.append(
        QuickReplyButton(
        action=PostbackAction(label="回上一步", text = "回上一步" ,data=f"action=choose_seat_area&date={data['date']}&start_time={data['start_time']}&end_time={data['end_time']}&next_day={data['next_day']}")))
    if(count == 0):
        text_message = TextSendMessage(
            text=f'抱歉，您所選擇的時間C區已無座位',
            quick_reply=QuickReply(items=quick_reply_buttons)
        )
    else:
        text_message = TextSendMessage(
            text=f'請選擇C區座位',
            quick_reply=QuickReply(items=quick_reply_buttons)
        )

    line_bot_api.reply_message(
        event.reply_token,
        text_message
    )

def choose_D_seat(event):
    data = dict(parse_qsl(event.postback.data))
    count = 0
    quick_reply_buttons = []
    for i in range(1,12):
        if(check_seat(event,i+22)):
            quick_reply_buttons.append(
            QuickReplyButton(
            action=PostbackAction(label=f"M{119+i:03d}", text = f"選擇 M{119+i:03d}" ,data=f"action=comfirm_reserv&date={data['date']}&start_time={data['start_time']}&end_time={data['end_time']}&next_day={data['next_day']}&seat=M{119+i:03d}")))
            count += 1

    quick_reply_buttons.append(
        QuickReplyButton(
        action=PostbackAction(label="回上一步", text = "回上一步" ,data=f"action=choose_seat_area&date={data['date']}&start_time={data['start_time']}&end_time={data['end_time']}&next_day={data['next_day']}")))
    if(count == 0):
        text_message = TextSendMessage(
            text=f'抱歉，您所選擇的時間D區已無座位',
            quick_reply=QuickReply(items=quick_reply_buttons)
        )
    else:
        text_message = TextSendMessage(
            text=f'請選擇D區座位',
            quick_reply=QuickReply(items=quick_reply_buttons)
        )

    line_bot_api.reply_message(
        event.reply_token,
        text_message
    )

def choose_E_seat(event):
    data = dict(parse_qsl(event.postback.data))
    count = 0
    quick_reply_buttons = []
    for i in range(1,12):
        if(check_seat(event,i+33)):
            quick_reply_buttons.append(
            QuickReplyButton(
            action=PostbackAction(label=f"M{159+i:03d}", text = f"選擇 M{159+i:03d}" ,data=f"action=comfirm_reserv&date={data['date']}&start_time={data['start_time']}&end_time={data['end_time']}&next_day={data['next_day']}&seat=M{159+i:03d}")))
            count += 1

    quick_reply_buttons.append(
        QuickReplyButton(
        action=PostbackAction(label="回上一步", text = "回上一步" ,data=f"action=choose_seat_area&date={data['date']}&start_time={data['start_time']}&end_time={data['end_time']}&next_day={data['next_day']}")))
    if(count == 0):
        text_message = TextSendMessage(
            text=f'抱歉，您所選擇的時間E區已無座位',
            quick_reply=QuickReply(items=quick_reply_buttons)
        )
    else:
        text_message = TextSendMessage(
            text=f'請選擇E區座位',
            quick_reply=QuickReply(items=quick_reply_buttons)
        )

    line_bot_api.reply_message(
        event.reply_token,
        text_message
    )
#==================================================================================================#
def confirm_reserv(event):
    data = dict(parse_qsl(event.postback.data))
    profile = line_bot_api.get_profile(event.source.user_id)
    user = User.query.filter(User.line_id == profile.user_id).first()
    stu_id = user.stu_id
    name = user.name

    if(int(data['seat'][1:])<80):
        seat_area = 'B'
    elif(int(data['seat'][1:])<120):
        seat_area = 'C'
    elif(int(data['seat'][1:])<160):
        seat_area = 'D'
    else:
        seat_area = 'E'
    start_time_str = data.get('date')+' '+data.get('start_time')
    start_time_dt = dt.datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
    if(data.get('next_day') == 'True'):
        date_next = dt.date(start_time_dt.year, start_time_dt.month, start_time_dt.day) + dt.timedelta(days=1)
        date_next = date_next.strftime('%Y-%m-%d')
        end_time_str = date_next +' '+data.get('end_time')
    else:
        end_time_str = data.get('date') +' '+data.get('end_time')
    end_time_dt = dt.datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")
    text_message = TextSendMessage(text='請確認您的預約資訊')
    confirm_template_message = TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
            text=f'姓名: {name}\n學號: {stu_id}\n空間區域: 4F-夜讀區{seat_area}\n座位: {data["seat"]}\n預約時間:\n    {start_time_str}~\n    {end_time_str}',
            actions=[
                PostbackAction(
                    label='送出預約',
                    display_text='送出預約',
                    data=f"action=commit_reserv&date={data['date']}&start_time={data['start_time']}&end_time={data['end_time']}&next_day={data['next_day']}&seat={data['seat']}"
                ),
                MessageAction(
                    label='取消',
                    text='取消'
                )
            ]
        )
    )
    line_bot_api.reply_message(
        event.reply_token,
        [text_message,confirm_template_message]
    )

#==================================================================================================#
def get_time_key(date='2023-06-06',start_time='00:00',end_time='23:59',next_day='False'):
    start_time_str = date+' '+start_time
    start_time_dt = dt.datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
    if(next_day == 'True'):
        date_next = dt.date(start_time_dt.year, start_time_dt.month, start_time_dt.day) + dt.timedelta(days=1)
        date_next = date_next.strftime('%Y-%m-%d')
        end_time_str = date_next +' '+end_time
    else:
        end_time_str = date +' '+end_time
    end_time_dt = dt.datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")

    day_select = dt.datetime.strptime(date, "%Y-%m-%d")
    today = dt.date.today()
    if(day_select.date() == today):
        day_start = 1
    elif(day_select.date() == today + dt.timedelta(days=1)):
        day_start = 2
    elif(day_select.date() == today + dt.timedelta(days=2)):
        day_start = 3
    else:
        day_start = 4
    if(next_day == 'True'):
        day_end = day_start + 1
    else:
        day_end = day_start

    
    start_time_key = f"day_{day_start}_{start_time.replace(':','_')}"
    end_time_key = f"day_{day_end}_{end_time.replace(':','_')}"
    return start_time_key, end_time_key

def fill_in_seat(user, date='2023-06-06',start_time='00:00',end_time='23:59',next_day='False',seat_num='M040'):
    start_time_str = date+' '+start_time
    start_time_dt = dt.datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
    if(next_day == 'True'):
        date_next = dt.date(start_time_dt.year, start_time_dt.month, start_time_dt.day) + dt.timedelta(days=1)
        date_next = date_next.strftime('%Y-%m-%d')
        end_time_str = date_next +' '+end_time
    else:
        end_time_str = date +' '+end_time
    end_time_dt = dt.datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")
    if(user.reserv_1_seat == None):
        user.reserv_1_seat = seat_num
        user.reserv_1_starttime = start_time_dt
        user.reserv_1_endtime = end_time_dt
    elif(user.reserv_2_seat == None):
        user.reserv_2_seat = seat_num
        user.reserv_2_starttime = start_time_dt
        user.reserv_2_endtime = end_time_dt
    elif(user.reserv_3_seat == None):
        user.reserv_3_seat = seat_num
        user.reserv_3_starttime = start_time_dt
        user.reserv_3_endtime = end_time_dt

def commit_reserv(event):
    data = dict(parse_qsl(event.postback.data))
    profile = line_bot_api.get_profile(event.source.user_id)
    user = User.query.filter(User.line_id == profile.user_id).first()
    stu_id = user.stu_id
    seat_num = data['seat']
    seat = Seat.query.filter(Seat.seat_num == seat_num).first()
    #fill_in_seat(user, date='2023-06-06',start_time='00:00',end_time='23:59',next_day='False',seat_num='M040')
    fill_in_seat(user,data['date'],data['start_time'],data['end_time'],data['next_day'],seat_num)
    user.reserv_count += 1
    db.session.commit()
    start_time_key, end_time_key = get_time_key(data['date'],data['start_time'],data['end_time'],data['next_day'])
    

    for i in range(seat_key_lst.index(start_time_key),seat_key_lst_2.index(end_time_key)+1):
        commit_seatdate(seat_key_lst[i],seat_num,stu_id)
        
    text_message = TextSendMessage(text='預約成功')
    line_bot_api.reply_message(
        event.reply_token,
        text_message
    )

def get_myformat_time(user_starttime,user_endtime):
    date = user_starttime.strftime("%Y-%m-%d")
    start_time = (user_starttime).strftime("%H:%M")
    end_time = (user_endtime).strftime("%H:%M")
    if(user_starttime.date() == user_endtime.date()):
        next_day = 'False'
    else:
        next_day = 'True'
    return date,start_time,end_time,next_day

def cancel_reserv(event,user):
    data = dict(parse_qsl(event.postback.data))
    reserv_num = data.get('reserv')
    if(reserv_num == '1'):
        #date_time = now.strftime("%Y-%m-%d, %H:%M:%S")
        seat_num = user.reserv_1_seat
        date,start_time,end_time,next_day = get_myformat_time(user.reserv_1_starttime,user.reserv_1_endtime)
        start_time_key, end_time_key =get_time_key(date,start_time,end_time,next_day)
        
        for i in range(seat_key_lst.index(start_time_key),seat_key_lst_2.index(end_time_key)+1):
            clear_selected_time_record(seat_key_lst[i],seat_num)
        
        user.reserv_1_seat = None
        user.reserv_1_starttime = None
        user.reserv_1_endtime = None
        db.session.commit()

    elif(reserv_num == '2'):
        seat_num = user.reserv_2_seat
        date,start_time,end_time,next_day = get_myformat_time(user.reserv_2_starttime,user.reserv_2_endtime)
        start_time_key, end_time_key =get_time_key(date,start_time,end_time,next_day)
        
        for i in range(seat_key_lst.index(start_time_key),seat_key_lst_2.index(end_time_key)+1):
            clear_selected_time_record(seat_key_lst[i],seat_num)
        
        user.reserv_2_seat = None
        user.reserv_2_starttime = None
        user.reserv_2_endtime = None
        db.session.commit()

    elif(reserv_num == '3'):
        seat_num = user.reserv_3_seat
        date,start_time,end_time,next_day = get_myformat_time(user.reserv_3_starttime,user.reserv_3_endtime)
        start_time_key, end_time_key =get_time_key(date,start_time,end_time,next_day)
        for i in range(seat_key_lst.index(start_time_key),seat_key_lst_2.index(end_time_key)+1):
            clear_selected_time_record(seat_key_lst[i],seat_num)

        user.reserv_3_seat = None
        user.reserv_3_starttime = None
        user.reserv_3_endtime = None
        db.session.commit()
    user.reserv_count -= 1
    db.session.commit()
    text_message = TextSendMessage(text='取消預約成功')
    line_bot_api.reply_message(
        event.reply_token,
        text_message
    )