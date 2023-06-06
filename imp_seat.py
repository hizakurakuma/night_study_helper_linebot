﻿from user import *
from reserve import *
from extensions import *
import pandas
from flask import Flask, current_app

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:0617@localhost:5432/nightstudy'

db.app = app
db.init_app(app)
migrate.init_app(app, db)
with app.app_context():
    seat_lst = ['M040', 'M041', 'M042', 'M043', 'M044', 'M045', 'M046', 'M047', 'M048', 'M049', 'M050', 'M080', 'M081', 'M082', 'M083', 'M084', 'M085', 'M086', 'M087', 'M088', 'M089', 'M090', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M160', 'M161', 'M162', 'M163', 'M164', 'M165', 'M166', 'M167', 'M168', 'M169', 'M170']
    for i in range(len(seat_lst)):
        seat = Seat.query.get(i+1)
        clear_all_time_record(seat)
        db.session.commit()
"""
with app.app_context():
    seat = Seat.query.get(6)
    seat.day_3_22_00 ='0'
    seat.day_3_22_30 ='0'
    seat.day_3_23_00 ='0'
    seat.day_3_23_30 ='0'
    db.session.commit()
"""
#__init__(self,seat_num,stu_id,day,time)
"""
with app.app_context():
    seat_lst = ['M040', 'M041', 'M042', 'M043', 'M044', 'M045', 'M046', 'M047', 'M048', 'M049', 'M050', 'M080', 'M081', 'M082', 'M083', 'M084', 'M085', 'M086', 'M087', 'M088', 'M089', 'M090', 'M120', 'M121', 'M122', 'M123', 'M124', 'M125', 'M126', 'M127', 'M128', 'M129', 'M130', 'M160', 'M161', 'M162', 'M163', 'M164', 'M165', 'M166', 'M167', 'M168', 'M169', 'M170']
    for i in range(len(seat_lst)):
        seat = Seat.query.get(i+1)
        seat.seat_num = seat_lst[i]
        db.session.commit()
"""
"""
with app.app_context():
    for i in range(len(seat_lst)):
        seat = Seat(seat_lst[i],None,None,None)
        db.session.add(seat)
        db.session.commit()
        print('success')
"""