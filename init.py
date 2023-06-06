from user import *
from reserve import *
from extensions import *
import pandas
from flask import Flask, current_app
#from config import Config

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:0617@localhost:5432/nightstudy'

db.app = app
db.init_app(app)
migrate.init_app(app, db)

seat_lst = ['M040', 'M041', 'M042', 'M043', 'M044', 'M045', 'M046', 'M047', 'M048', 'M049', 'M050', 'M080', 'M081', 'M082', 'M083', 'M084', 'M085', 'M086', 'M087', 'M088', 'M089', 'M090', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M160', 'M161', 'M162', 'M163', 'M164', 'M165', 'M166', 'M167', 'M168', 'M169', 'M170']

with app.app_context():
    for i in range(1,501):
        user = User.query.get(i)
        if((user.line_id)[:4] == 'line'):
            break
        t_user = T_User.query.filter(T_User.line_id == user.line_id).first()
        t_user.login_stat = False
        user.line_id = f'line{i:03d}'
        user.login_stat = False
        user.vio_count = 0
        user.suspend_stat = False
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

    for i in trange(len(seat_lst)):
        seat = Seat.query.get(i+1)
        clear_all_day1_record(seat)
        clear_all_day2_record(seat)
        clear_all_day3_record(seat)
        clear_all_day4_record(seat)
        clear_all_day5_record(seat)
        db.session.commit()