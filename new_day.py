from user import *
from reserve import *
from extensions import *
from flask import Flask, current_app

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:0617@localhost:5432/nightstudy'

db.app = app
db.init_app(app)
migrate.init_app(app, db)

#換日清除所有座位的day1紀錄，將day2~day5紀錄往前移一天，並清除day5紀錄
with app.app_context():
    seat_lst = ['M040', 'M041', 'M042', 'M043', 'M044', 'M045', 'M046', 'M047', 'M048', 'M049', 'M050', 'M080', 'M081', 'M082', 'M083', 'M084', 'M085', 'M086', 'M087', 'M088', 'M089', 'M090', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M160', 'M161', 'M162', 'M163', 'M164', 'M165', 'M166', 'M167', 'M168', 'M169', 'M170']
    for i in range(len(seat_lst)):
        seat = Seat.query.get(i+1)
        clear_all_day1_record(seat) #清除所有座位的day1紀錄 #關於clear_all_day1_record，詳見reserve.py
        move_to_next_day(seat) #將day2~day5紀錄往前移一天 #關於move_to_next_day，詳見reserve.py
        clear_all_day5_record(seat) #清除day5紀錄 #關於clear_all_day5_record，詳見reserve.py
        db.session.commit()

#清除所有預約過期的紀錄
    for i in range(500):
        user = User.query.get(i+1)
        if(user.reserv_count != 0):
            if(user.reserv_1_seat != None): #如果使用者有預約紀錄_1，則檢查該預約是否過期
                if(check_reserv_outdate(user,endtime = user.reserv_1_endtime)): #如果預約已過期，則清除該預約紀錄
                    #關於check_reserv_outdate，請見user.py
                    user.reserv_1_seat = None
                    user.reserv_1_starttime = None
                    user.reserv_1_endtime = None
                    user.reserv_count -= 1
            if(user.reserv_2_seat != None): #如果使用者有預約紀錄_2，則檢查該預約是否過期
                if(check_reserv_outdate(user,endtime = user.reserv_2_endtime)):
                    user.reserv_2_seat = None
                    user.reserv_2_starttime = None
                    user.reserv_2_endtime = None
                    user.reserv_count -= 1
            if(user.reserv_3_seat != None):#如果使用者有預約紀錄_3，則檢查該預約是否過期
                if(check_reserv_outdate(user,endtime = user.reserv_3_endtime)):
                    user.reserv_3_seat = None
                    user.reserv_3_starttime = None
                    user.reserv_3_endtime = None
                    user.reserv_count -= 1
        db.session.commit()