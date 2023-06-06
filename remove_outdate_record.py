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

#清除所有預約過期的紀錄
with app.app_context():
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