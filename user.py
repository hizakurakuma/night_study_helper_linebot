from extensions import db
import datetime

class T_User(db.Model):
    table_name = 't_user'
    id = db.Column(db.Integer, primary_key=True)
    line_id = db.Column(db.String(50), unique=True)
    display_name = db.Column(db.String(255))
    picturl_url = db.Column(db.String(255))
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())
    login_stat = db.Column(db.Boolean)
    
    def __init__(self, line_id, display_name, picturl_url):
        self.line_id = line_id
        self.display_name = display_name
        self.picturl_url = picturl_url
        self.login_stat = False


class User(db.Model):
    table_name = 'user'
    id = db.Column(db.Integer, primary_key=True)
    line_id = db.Column(db.String(50), unique=True)
    stu_id = db.Column(db.String(50))
    password = db.Column(db.String(50))
    name = db.Column(db.String(50))
    vio_count = db.Column(db.Integer)
    susp_stat = db.Column(db.Boolean)
    login_stat = db.Column(db.Boolean)
    reserv_1_starttime = db.Column(db.DateTime)
    reserv_1_endtime = db.Column(db.DateTime)
    reserv_2_starttime = db.Column(db.DateTime)
    reserv_2_endtime = db.Column(db.DateTime)
    reserv_3_starttime = db.Column(db.DateTime)
    reserv_3_endtime = db.Column(db.DateTime)
    reserv_count = db.Column(db.Integer,default=0)
    reserv_1_seat = db.Column(db.String(10))
    reserv_2_seat = db.Column(db.String(10))
    reserv_3_seat = db.Column(db.String(10))

    def __init__(self,line_id, name, stu_id,password,vio_count,susp_stat,login_stat,reserv_times,starttime,endtime):
        #id	line_id	stu_id	password	name	vio_count	susp_stat
        self.line_id = line_id
        self.name = name
        self.stu_id = stu_id
        self.password = password
        self.vio_count = 0
        self.susp_stat = False
        self.login_stat = False
        if(reserv_times == 1):
            self.reserv_1_starttime = starttime
            self.reserv_1_endtime = endtime
        elif(reserv_times == 2):
            self.reserv_2_starttime = starttime
            self.reserv_2_endtime = endtime
        elif(reserv_times == 3):
            self.reserv_3_starttime = starttime
            self.reserv_3_endtime = endtime

"""
t_user = T_User.query.filter(T_User.line_id == event.source.user_id).first()
if not t_user:
    profile = line_bot_api.get_profile(event.source.user_id)
    t_user = T_User(profile.user_id, profile.display_name, profile.picture_url)
    db.session.add(t_user)
    db.session.commit()
"""

reservation = db.relationship('Reservation', backref='user')

def check_reserv_outdate(user,endtime):
    today = datetime.datetime.now()
    if(endtime < today):
        return True
    else:
        return False
