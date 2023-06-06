from user import *
from extensions import *
import pandas
from flask import Flask, current_app

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:0617@localhost:5432/nightstudy'

db.app = app
db.init_app(app)
migrate.init_app(app, db)
"""
with app.app_context():
    user = User.query.get(500)
    user.line_id = 'line500'
    user.name = '王小明'
    user.stu_id = '111000100'
    user.password = 'A123456789'
    user.vio_count = 0
    user.login_stat = False
    user.reserv_count = 0
    user.reserv_1_starttime = None
    user.reserv_1_endtime = None
    user.reserv_1_seat = None
    user.reserv_2_starttime = None
    user.reserv_2_endtime = None
    user.reserv_2_seat = None
    user.reserv_3_starttime = None
    user.reserv_3_endtime = None
    user.reserv_3_seat = None
    db.session.commit()
"""
# 把測試帳號(我自己)預約資料清空
with app.app_context():
    user = User.query.get(61)
    user.reserv_count = 0
    user.reserv_1_starttime = None
    user.reserv_1_endtime = None
    user.reserv_1_seat = None
    user.reserv_2_starttime = None
    user.reserv_2_endtime = None
    user.reserv_2_seat = None
    user.reserv_3_starttime = None
    user.reserv_3_endtime = None
    user.reserv_3_seat = None
    db.session.commit()

"""
with app.app_context():
    for i in range(500):
        user = User.query.get(i+1)
        user.reserv_count = 0
        db.session.commit()


with app.app_context():
    #@app.route("/insert")
    t_user = T_User.query.get(1)
    t_user.login_stat = False
    db.session.commit()


with app.app_context():
    df = pandas.read_excel('user_init.xlsx')
    user_list = df.values.tolist()
    for i in range(len(user_list)):
        #user = User(str(user_list[i][1]),str(user_list[i][2]),str(user_list[i][3]),str(user_list[i][4]),int(user_list[i][5]),bool(user_list[i][6]))
        #db.session.add(user)
        user = User.query.get(i+1)
        name = user.password
        password = user.stu_id
        stu_id = user.name

        user.name = name
        user.password = password
        user.stu_id = stu_id
        db.session.commit()
        #print(user_list[i][0],user_list[i][1],user_list[i][2],user_list[i][3],user_list[i][4],user_list[i][5],bool(user_list[i][6]))
        #print('success')
"""