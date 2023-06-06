from extensions import *
from line_bot_api import *
from datetime import datetime

class Seat(db.Model):
    table_name = 'seat'
    id = db.Column(db.Integer, primary_key=True)
    seat_num = db.Column(db.String(50))
    day_1_00_00 = db.Column(db.String(50),default='0')
    day_1_00_30 = db.Column(db.String(50),default='0')
    day_1_01_00 = db.Column(db.String(50),default='0')
    day_1_01_30 = db.Column(db.String(50),default='0')
    day_1_02_00 = db.Column(db.String(50),default='0')
    day_1_02_30 = db.Column(db.String(50),default='0')
    day_1_03_00 = db.Column(db.String(50),default='0')
    day_1_03_30 = db.Column(db.String(50),default='0')
    day_1_04_00 = db.Column(db.String(50),default='0')
    day_1_04_30 = db.Column(db.String(50),default='0')
    day_1_05_00 = db.Column(db.String(50),default='0')
    day_1_05_30 = db.Column(db.String(50),default='0')
    day_1_06_00 = db.Column(db.String(50),default='0')
    day_1_06_30 = db.Column(db.String(50),default='0')
    day_1_07_00 = db.Column(db.String(50),default='0')
    day_1_07_30 = db.Column(db.String(50),default='0')
    day_1_08_00 = db.Column(db.String(50),default='0')
    day_1_08_30 = db.Column(db.String(50),default='0')
    day_1_17_00 = db.Column(db.String(50),default='0')
    day_1_17_30 = db.Column(db.String(50),default='0')
    day_1_18_00 = db.Column(db.String(50),default='0')
    day_1_18_30 = db.Column(db.String(50),default='0')
    day_1_19_00 = db.Column(db.String(50),default='0')
    day_1_19_30 = db.Column(db.String(50),default='0')
    day_1_20_00 = db.Column(db.String(50),default='0')
    day_1_20_30 = db.Column(db.String(50),default='0')
    day_1_21_00 = db.Column(db.String(50),default='0')
    day_1_21_30 = db.Column(db.String(50),default='0')
    day_1_22_00 = db.Column(db.String(50),default='0')
    day_1_22_30 = db.Column(db.String(50),default='0')
    day_1_23_00 = db.Column(db.String(50),default='0')
    day_1_23_30 = db.Column(db.String(50),default='0')

    day_2_00_00 = db.Column(db.String(50),default='0')
    day_2_00_30 = db.Column(db.String(50),default='0')
    day_2_01_00 = db.Column(db.String(50),default='0')
    day_2_01_30 = db.Column(db.String(50),default='0')
    day_2_02_00 = db.Column(db.String(50),default='0')
    day_2_02_30 = db.Column(db.String(50),default='0')
    day_2_03_00 = db.Column(db.String(50),default='0')
    day_2_03_30 = db.Column(db.String(50),default='0')
    day_2_04_00 = db.Column(db.String(50),default='0')
    day_2_04_30 = db.Column(db.String(50),default='0')
    day_2_05_00 = db.Column(db.String(50),default='0')
    day_2_05_30 = db.Column(db.String(50),default='0')
    day_2_06_00 = db.Column(db.String(50),default='0')
    day_2_06_30 = db.Column(db.String(50),default='0')
    day_2_07_00 = db.Column(db.String(50),default='0')
    day_2_07_30 = db.Column(db.String(50),default='0')
    day_2_08_00 = db.Column(db.String(50),default='0')
    day_2_08_30 = db.Column(db.String(50),default='0')
    day_2_17_00 = db.Column(db.String(50),default='0')
    day_2_17_30 = db.Column(db.String(50),default='0')
    day_2_18_00 = db.Column(db.String(50),default='0')
    day_2_18_30 = db.Column(db.String(50),default='0')
    day_2_19_00 = db.Column(db.String(50),default='0')
    day_2_19_30 = db.Column(db.String(50),default='0')
    day_2_20_00 = db.Column(db.String(50),default='0')
    day_2_20_30 = db.Column(db.String(50),default='0')
    day_2_21_00 = db.Column(db.String(50),default='0')
    day_2_21_30 = db.Column(db.String(50),default='0')
    day_2_22_00 = db.Column(db.String(50),default='0')
    day_2_22_30 = db.Column(db.String(50),default='0')
    day_2_23_00 = db.Column(db.String(50),default='0')
    day_2_23_30 = db.Column(db.String(50),default='0')

    day_3_00_00 = db.Column(db.String(50),default='0')
    day_3_00_30 = db.Column(db.String(50),default='0')
    day_3_01_00 = db.Column(db.String(50),default='0')
    day_3_01_30 = db.Column(db.String(50),default='0')
    day_3_02_00 = db.Column(db.String(50),default='0')
    day_3_02_30 = db.Column(db.String(50),default='0')
    day_3_03_00 = db.Column(db.String(50),default='0')
    day_3_03_30 = db.Column(db.String(50),default='0')
    day_3_04_00 = db.Column(db.String(50),default='0')
    day_3_04_30 = db.Column(db.String(50),default='0')
    day_3_05_00 = db.Column(db.String(50),default='0')
    day_3_05_30 = db.Column(db.String(50),default='0')
    day_3_06_00 = db.Column(db.String(50),default='0')
    day_3_06_30 = db.Column(db.String(50),default='0')
    day_3_07_00 = db.Column(db.String(50),default='0')
    day_3_07_30 = db.Column(db.String(50),default='0')
    day_3_08_00 = db.Column(db.String(50),default='0')
    day_3_08_30 = db.Column(db.String(50),default='0')
    day_3_17_00 = db.Column(db.String(50),default='0')
    day_3_17_30 = db.Column(db.String(50),default='0')
    day_3_18_00 = db.Column(db.String(50),default='0')
    day_3_18_30 = db.Column(db.String(50),default='0')
    day_3_19_00 = db.Column(db.String(50),default='0')
    day_3_19_30 = db.Column(db.String(50),default='0')
    day_3_20_00 = db.Column(db.String(50),default='0')
    day_3_20_30 = db.Column(db.String(50),default='0')
    day_3_21_00 = db.Column(db.String(50),default='0')
    day_3_21_30 = db.Column(db.String(50),default='0')
    day_3_22_00 = db.Column(db.String(50),default='0')
    day_3_22_30 = db.Column(db.String(50),default='0')
    day_3_23_00 = db.Column(db.String(50),default='0')
    day_3_23_30 = db.Column(db.String(50),default='0')

    day_4_00_00 = db.Column(db.String(50),default='0')
    day_4_00_30 = db.Column(db.String(50),default='0')
    day_4_01_00 = db.Column(db.String(50),default='0')
    day_4_01_30 = db.Column(db.String(50),default='0')
    day_4_02_00 = db.Column(db.String(50),default='0')
    day_4_02_30 = db.Column(db.String(50),default='0')
    day_4_03_00 = db.Column(db.String(50),default='0')
    day_4_03_30 = db.Column(db.String(50),default='0')
    day_4_04_00 = db.Column(db.String(50),default='0')
    day_4_04_30 = db.Column(db.String(50),default='0')
    day_4_05_00 = db.Column(db.String(50),default='0')
    day_4_05_30 = db.Column(db.String(50),default='0')
    day_4_06_00 = db.Column(db.String(50),default='0')
    day_4_06_30 = db.Column(db.String(50),default='0')
    day_4_07_00 = db.Column(db.String(50),default='0')
    day_4_07_30 = db.Column(db.String(50),default='0')
    day_4_08_00 = db.Column(db.String(50),default='0')
    day_4_08_30 = db.Column(db.String(50),default='0')
    day_4_17_00 = db.Column(db.String(50),default='0')
    day_4_17_30 = db.Column(db.String(50),default='0')
    day_4_18_00 = db.Column(db.String(50),default='0')
    day_4_18_30 = db.Column(db.String(50),default='0')
    day_4_19_00 = db.Column(db.String(50),default='0')
    day_4_19_30 = db.Column(db.String(50),default='0')
    day_4_20_00 = db.Column(db.String(50),default='0')
    day_4_20_30 = db.Column(db.String(50),default='0')
    day_4_21_00 = db.Column(db.String(50),default='0')
    day_4_21_30 = db.Column(db.String(50),default='0')
    day_4_22_00 = db.Column(db.String(50),default='0')
    day_4_22_30 = db.Column(db.String(50),default='0')
    day_4_23_00 = db.Column(db.String(50),default='0')
    day_4_23_30 = db.Column(db.String(50),default='0')

    day_5_00_00 = db.Column(db.String(50),default='0')
    day_5_00_30 = db.Column(db.String(50),default='0')
    day_5_01_00 = db.Column(db.String(50),default='0')
    day_5_01_30 = db.Column(db.String(50),default='0')
    day_5_02_00 = db.Column(db.String(50),default='0')
    day_5_02_30 = db.Column(db.String(50),default='0')
    day_5_03_00 = db.Column(db.String(50),default='0')
    day_5_03_30 = db.Column(db.String(50),default='0')
    day_5_04_00 = db.Column(db.String(50),default='0')
    day_5_04_30 = db.Column(db.String(50),default='0')
    day_5_05_00 = db.Column(db.String(50),default='0')
    day_5_05_30 = db.Column(db.String(50),default='0')
    day_5_06_00 = db.Column(db.String(50),default='0')
    day_5_06_30 = db.Column(db.String(50),default='0')
    day_5_07_00 = db.Column(db.String(50),default='0')
    day_5_07_30 = db.Column(db.String(50),default='0')
    day_5_08_00 = db.Column(db.String(50),default='0')
    day_5_08_30 = db.Column(db.String(50),default='0')
    day_5_17_00 = db.Column(db.String(50),default='0')
    day_5_17_30 = db.Column(db.String(50),default='0')
    day_5_18_00 = db.Column(db.String(50),default='0')
    day_5_18_30 = db.Column(db.String(50),default='0')
    day_5_19_00 = db.Column(db.String(50),default='0')
    day_5_19_30 = db.Column(db.String(50),default='0')
    day_5_20_00 = db.Column(db.String(50),default='0')
    day_5_20_30 = db.Column(db.String(50),default='0')
    day_5_21_00 = db.Column(db.String(50),default='0')
    day_5_21_30 = db.Column(db.String(50),default='0')
    day_5_22_00 = db.Column(db.String(50),default='0')
    day_5_22_30 = db.Column(db.String(50),default='0')
    day_5_23_00 = db.Column(db.String(50),default='0')
    day_5_23_30 = db.Column(db.String(50),default='0')

    def __init__(self,seat_num,stu_id,day,time):
        self.seat_num = seat_num
        if(day==1):
            if(time=='00:00'):
                self.day_1_00_00 = stu_id
            elif(time=='00:30'):
                self.day_1_00_30 = stu_id
            elif(time=='01:00'):
                self.day_1_01_00 = stu_id
            elif(time=='01:30'):
                self.day_1_01_30 = stu_id
            elif(time=='02:00'):
                self.day_1_02_00 = stu_id
            elif(time=='02:30'):
                self.day_1_02_30 = stu_id
            elif(time=='03:00'):
                self.day_1_03_00 = stu_id
            elif(time=='03:30'):
                self.day_1_03_30 = stu_id
            elif(time=='04:00'):
                self.day_1_04_00 = stu_id
            elif(time=='04:30'):
                self.day_1_04_30 = stu_id
            elif(time=='05:00'):
                self.day_1_05_00 = stu_id
            elif(time=='05:30'):
                self.day_1_05_30 = stu_id
            elif(time=='06:00'):
                self.day_1_06_00 = stu_id
            elif(time=='06:30'):
                self.day_1_06_30 = stu_id
            elif(time=='07:00'):
                self.day_1_07_00 = stu_id
            elif(time=='07:30'):
                self.day_1_07_30 = stu_id
            elif(time=='08:00'):
                self.day_1_08_00 = stu_id
            elif(time=='08:30'):
                self.day_1_08_30 = stu_id
            elif(time=='17:00'):
                self.day_1_17_00 = stu_id
            elif(time=='17:30'):
                self.day_1_17_30 = stu_id
            elif(time=='18:00'):
                self.day_1_18_00 = stu_id
            elif(time=='18:30'):
                self.day_1_18_30 = stu_id
            elif(time=='19:00'):
                self.day_1_19_00 = stu_id
            elif(time=='19:30'):
                self.day_1_19_30 = stu_id
            elif(time=='20:00'):
                self.day_1_20_00 = stu_id
            elif(time=='20:30'):
                self.day_1_20_30 = stu_id
            elif(time=='21:00'):
                self.day_1_21_00 = stu_id
            elif(time=='21:30'):
                self.day_1_21_30 = stu_id
            elif(time=='22:00'):
                self.day_1_22_00 = stu_id
            elif(time=='22:30'):
                self.day_1_22_30 = stu_id
            elif(time=='23:00'):
                self.day_1_23_00 = stu_id
            elif(time=='23:30'):
                self.day_1_23_30 = stu_id
        
        elif(day==2):
            if(time=='00:00'):
                self.day_2_00_00 = stu_id
            elif(time=='00:30'):
                self.day_2_00_30 = stu_id
            elif(time=='01:00'):
                self.day_2_01_00 = stu_id
            elif(time=='01:30'):
                self.day_2_01_30 = stu_id
            elif(time=='02:00'):
                self.day_2_02_00 = stu_id
            elif(time=='02:30'):
                self.day_2_02_30 = stu_id
            elif(time=='03:00'):
                self.day_2_03_00 = stu_id
            elif(time=='03:30'):
                self.day_2_03_30 = stu_id
            elif(time=='04:00'):
                self.day_2_04_00 = stu_id
            elif(time=='04:30'):
                self.day_2_04_30 = stu_id
            elif(time=='05:00'):
                self.day_2_05_00 = stu_id
            elif(time=='05:30'):
                self.day_2_05_30 = stu_id
            elif(time=='06:00'):
                self.day_2_06_00 = stu_id
            elif(time=='06:30'):
                self.day_2_06_30 = stu_id
            elif(time=='07:00'):
                self.day_2_07_00 = stu_id
            elif(time=='07:30'):
                self.day_2_07_30 = stu_id
            elif(time=='08:00'):
                self.day_2_08_00 = stu_id
            elif(time=='08:30'):
                self.day_2_08_30 = stu_id
            elif(time=='17:00'):
                self.day_2_17_00 = stu_id
            elif(time=='17:30'):
                self.day_2_17_30 = stu_id
            elif(time=='18:00'):
                self.day_2_18_00 = stu_id
            elif(time=='18:30'):
                self.day_2_18_30 = stu_id
            elif(time=='19:00'):
                self.day_2_19_00 = stu_id
            elif(time=='19:30'):
                self.day_2_19_30 = stu_id
            elif(time=='20:00'):
                self.day_2_20_00 = stu_id
            elif(time=='20:30'):
                self.day_2_20_30 = stu_id
            elif(time=='21:00'):
                self.day_2_21_00 = stu_id
            elif(time=='21:30'):
                self.day_2_21_30 = stu_id
            elif(time=='22:00'):
                self.day_2_22_00 = stu_id
            elif(time=='22:30'):
                self.day_2_22_30 = stu_id
            elif(time=='23:00'):
                self.day_2_23_00 = stu_id
            elif(time=='23:30'):
                self.day_2_23_30 = stu_id

        elif(day==3):
            if(time=='00:00'):
                self.day_3_00_00 = stu_id
            elif(time=='00:30'):
                self.day_3_00_30 = stu_id
            elif(time=='01:00'):
                self.day_3_01_00 = stu_id
            elif(time=='01:30'):
                self.day_3_01_30 = stu_id
            elif(time=='02:00'):
                self.day_3_02_00 = stu_id
            elif(time=='02:30'):
                self.day_3_02_30 = stu_id
            elif(time=='03:00'):
                self.day_3_03_00 = stu_id
            elif(time=='03:30'):
                self.day_3_03_30 = stu_id
            elif(time=='04:00'):
                self.day_3_04_00 = stu_id
            elif(time=='04:30'):
                self.day_3_04_30 = stu_id
            elif(time=='05:00'):
                self.day_3_05_00 = stu_id
            elif(time=='05:30'):
                self.day_3_05_30 = stu_id
            elif(time=='06:00'):
                self.day_3_06_00 = stu_id
            elif(time=='06:30'):
                self.day_3_06_30 = stu_id
            elif(time=='07:00'):
                self.day_3_07_00 = stu_id
            elif(time=='07:30'):
                self.day_3_07_30 = stu_id
            elif(time=='08:00'):
                self.day_3_08_00 = stu_id
            elif(time=='08:30'):
                self.day_3_08_30 = stu_id
            elif(time=='17:00'):
                self.day_3_17_00 = stu_id
            elif(time=='17:30'):
                self.day_3_17_30 = stu_id
            elif(time=='18:00'):
                self.day_3_18_00 = stu_id
            elif(time=='18:30'):
                self.day_3_18_30 = stu_id
            elif(time=='19:00'):
                self.day_3_19_00 = stu_id
            elif(time=='19:30'):
                self.day_3_19_30 = stu_id
            elif(time=='20:00'):
                self.day_3_20_00 = stu_id
            elif(time=='20:30'):
                self.day_3_20_30 = stu_id
            elif(time=='21:00'):
                self.day_3_21_00 = stu_id
            elif(time=='21:30'):
                self.day_3_21_30 = stu_id
            elif(time=='22:00'):
                self.day_3_22_00 = stu_id
            elif(time=='22:30'):
                self.day_3_22_30 = stu_id
            elif(time=='23:00'):
                self.day_3_23_00 = stu_id
            elif(time=='23:30'):
                self.day_3_23_30 = stu_id
        
        elif(day==4):
            if(time=='00:00'):
                self.day_4_00_00 = stu_id
            elif(time=='00:30'):
                self.day_4_00_30 = stu_id
            elif(time=='01:00'):
                self.day_4_01_00 = stu_id
            elif(time=='01:30'):
                self.day_4_01_30 = stu_id
            elif(time=='02:00'):
                self.day_4_02_00 = stu_id
            elif(time=='02:30'):
                self.day_4_02_30 = stu_id
            elif(time=='03:00'):
                self.day_4_03_00 = stu_id
            elif(time=='03:30'):
                self.day_4_03_30 = stu_id
            elif(time=='04:00'):
                self.day_4_04_00 = stu_id
            elif(time=='04:30'):
                self.day_4_04_30 = stu_id
            elif(time=='05:00'):
                self.day_4_05_00 = stu_id
            elif(time=='05:30'):
                self.day_4_05_30 = stu_id
            elif(time=='06:00'):
                self.day_4_06_00 = stu_id
            elif(time=='06:30'):
                self.day_4_06_30 = stu_id
            elif(time=='07:00'):
                self.day_4_07_00 = stu_id
            elif(time=='07:30'):
                self.day_4_07_30 = stu_id
            elif(time=='08:00'):
                self.day_4_08_00 = stu_id
            elif(time=='08:30'):
                self.day_4_08_30 = stu_id
            elif(time=='17:00'):
                self.day_4_17_00 = stu_id
            elif(time=='17:30'):
                self.day_4_17_30 = stu_id
            elif(time=='18:00'):
                self.day_4_18_00 = stu_id
            elif(time=='18:30'):
                self.day_4_18_30 = stu_id
            elif(time=='19:00'):
                self.day_4_19_00 = stu_id
            elif(time=='19:30'):
                self.day_4_19_30 = stu_id
            elif(time=='20:00'):
                self.day_4_20_00 = stu_id
            elif(time=='20:30'):
                self.day_4_20_30 = stu_id
            elif(time=='21:00'):
                self.day_4_21_00 = stu_id
            elif(time=='21:30'):
                self.day_4_21_30 = stu_id
            elif(time=='22:00'):
                self.day_4_22_00 = stu_id
            elif(time=='22:30'):
                self.day_4_22_30 = stu_id
            elif(time=='23:00'):
                self.day_4_23_00 = stu_id
            elif(time=='23:30'):
                self.day_4_23_30 = stu_id

        elif(day==5):
            if(time=='00:00'):
                self.day_5_00_00 = stu_id
            elif(time=='00:30'):
                self.day_5_00_30 = stu_id
            elif(time=='01:00'):
                self.day_5_01_00 = stu_id
            elif(time=='01:30'):
                self.day_5_01_30 = stu_id
            elif(time=='02:00'):
                self.day_5_02_00 = stu_id
            elif(time=='02:30'):
                self.day_5_02_30 = stu_id
            elif(time=='03:00'):
                self.day_5_03_00 = stu_id
            elif(time=='03:30'):
                self.day_5_03_30 = stu_id
            elif(time=='04:00'):
                self.day_5_04_00 = stu_id
            elif(time=='04:30'):
                self.day_5_04_30 = stu_id
            elif(time=='05:00'):
                self.day_5_05_00 = stu_id
            elif(time=='05:30'):
                self.day_5_05_30 = stu_id
            elif(time=='06:00'):
                self.day_5_06_00 = stu_id
            elif(time=='06:30'):
                self.day_5_06_30 = stu_id
            elif(time=='07:00'):
                self.day_5_07_00 = stu_id
            elif(time=='07:30'):
                self.day_5_07_30 = stu_id
            elif(time=='08:00'):
                self.day_5_08_00 = stu_id
            elif(time=='08:30'):
                self.day_5_08_30 = stu_id
            elif(time=='17:00'):
                self.day_5_17_00 = stu_id
            elif(time=='17:30'):
                self.day_5_17_30 = stu_id
            elif(time=='18:00'):
                self.day_5_18_00 = stu_id
            elif(time=='18:30'):
                self.day_5_18_30 = stu_id
            elif(time=='19:00'):
                self.day_5_19_00 = stu_id
            elif(time=='19:30'):
                self.day_5_19_30 = stu_id
            elif(time=='20:00'):
                self.day_5_20_00 = stu_id
            elif(time=='20:30'):
                self.day_5_20_30 = stu_id
            elif(time=='21:00'):
                self.day_5_21_00 = stu_id
            elif(time=='21:30'):
                self.day_5_21_30 = stu_id
            elif(time=='22:00'):
                self.day_5_22_00 = stu_id
            elif(time=='22:30'):
                self.day_5_22_30 = stu_id
            elif(time=='23:00'):
                self.day_5_23_00 = stu_id
            elif(time=='23:30'):
                self.day_5_23_30 = stu_id

    def get_result_dict(self):
        result = {'id':self.id,'seat_num':self.seat_num,'day_1_00_00':self.day_1_00_00,'day_1_00_30':self.day_1_00_30,'day_1_01_00':self.day_1_01_00,'day_1_01_30':self.day_1_01_30,'day_1_02_00':self.day_1_02_00,'day_1_02_30':self.day_1_02_30,'day_1_03_00':self.day_1_03_00,'day_1_03_30':self.day_1_03_30,'day_1_04_00':self.day_1_04_00,'day_1_04_30':self.day_1_04_30,'day_1_05_00':self.day_1_05_00,'day_1_05_30':self.day_1_05_30,'day_1_06_00':self.day_1_06_00,'day_1_06_30':self.day_1_06_30,'day_1_07_00':self.day_1_07_00,'day_1_07_30':self.day_1_07_30,'day_1_08_00':self.day_1_08_00,'day_1_08_30':self.day_1_08_30,\
            'day_1_17_00':self.day_1_17_00,'day_1_17_30':self.day_1_17_30,'day_1_18_00':self.day_1_18_00,'day_1_18_30':self.day_1_18_30,'day_1_19_00':self.day_1_19_00,'day_1_19_30':self.day_1_19_30,'day_1_20_00':self.day_1_20_00,'day_1_20_30':self.day_1_20_30,'day_1_21_00':self.day_1_21_00,'day_1_21_30':self.day_1_21_30,'day_1_22_00':self.day_1_22_00,'day_1_22_30':self.day_1_22_30,'day_1_23_00':self.day_1_23_00,'day_1_23_30':self.day_1_23_30,\
            'day_2_00_00':self.day_2_00_00,'day_2_00_30':self.day_2_00_30,'day_2_01_00':self.day_2_01_00,'day_2_01_30':self.day_2_01_30,'day_2_02_00':self.day_2_02_00,'day_2_02_30':self.day_2_02_30,'day_2_03_00':self.day_2_03_00,'day_2_03_30':self.day_2_03_30,'day_2_04_00':self.day_2_04_00,'day_2_04_30':self.day_2_04_30,'day_2_05_00':self.day_2_05_00,'day_2_05_30':self.day_2_05_30,'day_2_06_00':self.day_2_06_00,'day_2_06_30':self.day_2_06_30,'day_2_07_00':self.day_2_07_00,'day_2_07_30':self.day_2_07_30,'day_2_08_00':self.day_2_08_00,'day_2_08_30':self.day_2_08_30,\
            'day_2_17_00':self.day_2_17_00,'day_2_17_30':self.day_2_17_30,'day_2_18_00':self.day_2_18_00,'day_2_18_30':self.day_2_18_30,'day_2_19_00':self.day_2_19_00,'day_2_19_30':self.day_2_19_30,'day_2_20_00':self.day_2_20_00,'day_2_20_30':self.day_2_20_30,'day_2_21_00':self.day_2_21_00,'day_2_21_30':self.day_2_21_30,'day_2_22_00':self.day_2_22_00,'day_2_22_30':self.day_2_22_30,'day_2_23_00':self.day_2_23_00,'day_2_23_30':self.day_2_23_30,\
            'day_3_00_00':self.day_3_00_00,'day_3_00_30':self.day_3_00_30,'day_3_01_00':self.day_3_01_00,'day_3_01_30':self.day_3_01_30,'day_3_02_00':self.day_3_02_00,'day_3_02_30':self.day_3_02_30,'day_3_03_00':self.day_3_03_00,'day_3_03_30':self.day_3_03_30,'day_3_04_00':self.day_3_04_00,'day_3_04_30':self.day_3_04_30,'day_3_05_00':self.day_3_05_00,'day_3_05_30':self.day_3_05_30,'day_3_06_00':self.day_3_06_00,'day_3_06_30':self.day_3_06_30,'day_3_07_00':self.day_3_07_00,'day_3_07_30':self.day_3_07_30,'day_3_08_00':self.day_3_08_00,'day_3_08_30':self.day_3_08_30,\
            'day_3_17_00':self.day_3_17_00,'day_3_17_30':self.day_3_17_30,'day_3_18_00':self.day_3_18_00,'day_3_18_30':self.day_3_18_30,'day_3_19_00':self.day_3_19_00,'day_3_19_30':self.day_3_19_30,'day_3_20_00':self.day_3_20_00,'day_3_20_30':self.day_3_20_30,'day_3_21_00':self.day_3_21_00,'day_3_21_30':self.day_3_21_30,'day_3_22_00':self.day_3_22_00,'day_3_22_30':self.day_3_22_30,'day_3_23_00':self.day_3_23_00,'day_3_23_30':self.day_3_23_30,\
            'day_4_00_00':self.day_4_00_00,'day_4_00_30':self.day_4_00_30,'day_4_01_00':self.day_4_01_00,'day_4_01_30':self.day_4_01_30,'day_4_02_00':self.day_4_02_00,'day_4_02_30':self.day_4_02_30,'day_4_03_00':self.day_4_03_00,'day_4_03_30':self.day_4_03_30,'day_4_04_00':self.day_4_04_00,'day_4_04_30':self.day_4_04_30,'day_4_05_00':self.day_4_05_00,'day_4_05_30':self.day_4_05_30,'day_4_06_00':self.day_4_06_00,'day_4_06_30':self.day_4_06_30,'day_4_07_00':self.day_4_07_00,'day_4_07_30':self.day_4_07_30,'day_4_08_00':self.day_4_08_00,'day_4_08_30':self.day_4_08_30,\
            'day_4_17_00':self.day_4_17_00,'day_4_17_30':self.day_4_17_30,'day_4_18_00':self.day_4_18_00,'day_4_18_30':self.day_4_18_30,'day_4_19_00':self.day_4_19_00,'day_4_19_30':self.day_4_19_30,'day_4_20_00':self.day_4_20_00,'day_4_20_30':self.day_4_20_30,'day_4_21_00':self.day_4_21_00,'day_4_21_30':self.day_4_21_30,'day_4_22_00':self.day_4_22_00,'day_4_22_30':self.day_4_22_30,'day_4_23_00':self.day_4_23_00,'day_4_23_30':self.day_4_23_30,\
            'day_5_00_00':self.day_5_00_00,'day_5_00_30':self.day_5_00_30,'day_5_01_00':self.day_5_01_00,'day_5_01_30':self.day_5_01_30,'day_5_02_00':self.day_5_02_00,'day_5_02_30':self.day_5_02_30,'day_5_03_00':self.day_5_03_00,'day_5_03_30':self.day_5_03_30,'day_5_04_00':self.day_5_04_00,'day_5_04_30':self.day_5_04_30,'day_5_05_00':self.day_5_05_00,'day_5_05_30':self.day_5_05_30,'day_5_06_00':self.day_5_06_00,'day_5_06_30':self.day_5_06_30,'day_5_07_00':self.day_5_07_00,'day_5_07_30':self.day_5_07_30,'day_5_08_00':self.day_5_08_00,'day_5_08_30':self.day_5_08_30,\
            'day_5_17_00':self.day_5_17_00,'day_5_17_30':self.day_5_17_30,'day_5_18_00':self.day_5_18_00,'day_5_18_30':self.day_5_18_30,'day_5_19_00':self.day_5_19_00,'day_5_19_30':self.day_5_19_30,'day_5_20_00':self.day_5_20_00,'day_5_20_30':self.day_5_20_30,'day_5_21_00':self.day_5_21_00,'day_5_21_30':self.day_5_21_30,'day_5_22_00':self.day_5_22_00,'day_5_22_30':self.day_5_22_30,'day_5_23_00':self.day_5_23_00,'day_5_23_30':self.day_5_23_30}
        return result

    def get_result_lst(self):
        result = [self.id,self.seat_num,self.day_1_00_00,self.day_1_00_30,self.day_1_01_00,self.day_1_01_30,self.day_1_02_00,self.day_1_02_30,self.day_1_03_00,self.day_1_03_30,self.day_1_04_00,self.day_1_04_30,self.day_1_05_00,self.day_1_05_30,self.day_1_06_00,self.day_1_06_30,self.day_1_07_00,self.day_1_07_30,self.day_1_08_00,self.day_1_08_30,\
            self.day_1_17_00,self.day_1_17_30,self.day_1_18_00,self.day_1_18_30,self.day_1_19_00,self.day_1_19_30,self.day_1_20_00,self.day_1_20_30,self.day_1_21_00,self.day_1_21_30,self.day_1_22_00,self.day_1_22_30,self.day_1_23_00,self.day_1_23_30,\
            self.day_2_00_00,self.day_2_00_30,self.day_2_01_00,self.day_2_01_30,self.day_2_02_00,self.day_2_02_30,self.day_2_03_00,self.day_2_03_30,self.day_2_04_00,self.day_2_04_30,self.day_2_05_00,self.day_2_05_30,self.day_2_06_00,self.day_2_06_30,self.day_2_07_00,self.day_2_07_30,self.day_2_08_00,self.day_2_08_30,\
            self.day_2_17_00,self.day_2_17_30,self.day_2_18_00,self.day_2_18_30,self.day_2_19_00,self.day_2_19_30,self.day_2_20_00,self.day_2_20_30,self.day_2_21_00,self.day_2_21_30,self.day_2_22_00,self.day_2_22_30,self.day_2_23_00,self.day_2_23_30,\
            self.day_3_00_00,self.day_3_00_30,self.day_3_01_00,self.day_3_01_30,self.day_3_02_00,self.day_3_02_30,self.day_3_03_00,self.day_3_03_30,self.day_3_04_00,self.day_3_04_30,self.day_3_05_00,self.day_3_05_30,self.day_3_06_00,self.day_3_06_30,self.day_3_07_00,self.day_3_07_30,self.day_3_08_00,self.day_3_08_30,\
            self.day_3_17_00,self.day_3_17_30,self.day_3_18_00,self.day_3_18_30,self.day_3_19_00,self.day_3_19_30,self.day_3_20_00,self.day_3_20_30,self.day_3_21_00,self.day_3_21_30,self.day_3_22_00,self.day_3_22_30,self.day_3_23_00,self.day_3_23_30,\
            self.day_4_00_00,self.day_4_00_30,self.day_4_01_00,self.day_4_01_30,self.day_4_02_00,self.day_4_02_30,self.day_4_03_00,self.day_4_03_30,self.day_4_04_00,self.day_4_04_30,self.day_4_05_00,self.day_4_05_30,self.day_4_06_00,self.day_4_06_30,self.day_4_07_00,self.day_4_07_30,self.day_4_08_00,self.day_4_08_30,\
            self.day_4_17_00,self.day_4_17_30,self.day_4_18_00,self.day_4_18_30,self.day_4_19_00,self.day_4_19_30,self.day_4_20_00,self.day_4_20_30,self.day_4_21_00,self.day_4_21_30,self.day_4_22_00,self.day_4_22_30,self.day_4_23_00,self.day_4_23_30,\
            self.day_5_00_00,self.day_5_00_30,self.day_5_01_00,self.day_5_01_30,self.day_5_02_00,self.day_5_02_30,self.day_5_03_00,self.day_5_03_30,self.day_5_04_00,self.day_5_04_30,self.day_5_05_00,self.day_5_05_30,self.day_5_06_00,self.day_5_06_30,self.day_5_07_00,self.day_5_07_30,self.day_5_08_00,self.day_5_08_30,\
            self.day_5_17_00,self.day_5_17_30,self.day_5_18_00,self.day_5_18_30,self.day_5_19_00,self.day_5_19_30,self.day_5_20_00,self.day_5_20_30,self.day_5_21_00,self.day_5_21_30,self.day_5_22_00,self.day_5_22_30,self.day_5_23_00,self.day_5_23_30]
        return result


def commit_seatdate(seatdate_key,seat_num,stu_id):
    seat = Seat.query.filter(Seat.seat_num == seat_num).first()
    if(seatdate_key=='day_1_00_00'):
        seat.day_1_00_00 = stu_id
    elif(seatdate_key=='day_1_00_30'):
        seat.day_1_00_30 = stu_id
    elif(seatdate_key=='day_1_01_00'):
        seat.day_1_01_00 = stu_id
    elif(seatdate_key=='day_1_01_30'):
        seat.day_1_01_30 = stu_id
    elif(seatdate_key=='day_1_02_00'):
        seat.day_1_02_00 = stu_id
    elif(seatdate_key=='day_1_02_30'):
        seat.day_1_02_30 = stu_id
    elif(seatdate_key=='day_1_03_00'):
        seat.day_1_03_00 = stu_id
    elif(seatdate_key=='day_1_03_30'):
        seat.day_1_03_30 = stu_id
    elif(seatdate_key=='day_1_04_00'):
        seat.day_1_04_00 = stu_id
    elif(seatdate_key=='day_1_04_30'):
        seat.day_1_04_30 = stu_id
    elif(seatdate_key=='day_1_05_00'):
        seat.day_1_05_00 = stu_id
    elif(seatdate_key=='day_1_05_30'):
        seat.day_1_05_30 = stu_id
    elif(seatdate_key=='day_1_06_00'):
        seat.day_1_06_00 = stu_id
    elif(seatdate_key=='day_1_06_30'):
        seat.day_1_06_30 = stu_id
    elif(seatdate_key=='day_1_07_00'):
        seat.day_1_07_00 = stu_id
    elif(seatdate_key=='day_1_07_30'):
        seat.day_1_07_30 = stu_id
    elif(seatdate_key=='day_1_08_00'):
        seat.day_1_08_00 = stu_id
    elif(seatdate_key=='day_1_08_30'):
        seat.day_1_08_30 = stu_id
    elif(seatdate_key=='day_1_17_00'):
        seat.day_1_17_00 = stu_id
    elif(seatdate_key=='day_1_17_30'):
        seat.day_1_17_30 = stu_id
    elif(seatdate_key=='day_1_18_00'):
        seat.day_1_18_00 = stu_id
    elif(seatdate_key=='day_1_18_30'):
        seat.day_1_18_30 = stu_id
    elif(seatdate_key=='day_1_19_00'):
        seat.day_1_19_00 = stu_id
    elif(seatdate_key=='day_1_19_30'):
        seat.day_1_19_30 = stu_id
    elif(seatdate_key=='day_1_20_00'):
        seat.day_1_20_00 = stu_id
    elif(seatdate_key=='day_1_20_30'):
        seat.day_1_20_30 = stu_id
    elif(seatdate_key=='day_1_21_00'):
        seat.day_1_21_00 = stu_id
    elif(seatdate_key=='day_1_21_30'):
        seat.day_1_21_30 = stu_id
    elif(seatdate_key=='day_1_22_00'):
        seat.day_1_22_00 = stu_id
    elif(seatdate_key=='day_1_22_30'):
        seat.day_1_22_30 = stu_id
    elif(seatdate_key=='day_1_23_00'):
        seat.day_1_23_00 = stu_id
    elif(seatdate_key=='day_1_23_30'):
        seat.day_1_23_30 = stu_id
    elif(seatdate_key=='day_2_00_00'):
        seat.day_2_00_00 = stu_id
    elif(seatdate_key=='day_2_00_30'):
        seat.day_2_00_30 = stu_id
    elif(seatdate_key=='day_2_01_00'):
        seat.day_2_01_00 = stu_id
    elif(seatdate_key=='day_2_01_30'):
        seat.day_2_01_30 = stu_id
    elif(seatdate_key=='day_2_02_00'):
        seat.day_2_02_00 = stu_id
    elif(seatdate_key=='day_2_02_30'):
        seat.day_2_02_30 = stu_id
    elif(seatdate_key=='day_2_03_00'):
        seat.day_2_03_00 = stu_id
    elif(seatdate_key=='day_2_03_30'):
        seat.day_2_03_30 = stu_id
    elif(seatdate_key=='day_2_04_00'):
        seat.day_2_04_00 = stu_id
    elif(seatdate_key=='day_2_04_30'):
        seat.day_2_04_30 = stu_id
    elif(seatdate_key=='day_2_05_00'):
        seat.day_2_05_00 = stu_id
    elif(seatdate_key=='day_2_05_30'):
        seat.day_2_05_30 = stu_id
    elif(seatdate_key=='day_2_06_00'):
        seat.day_2_06_00 = stu_id
    elif(seatdate_key=='day_2_06_30'):
        seat.day_2_06_30 = stu_id
    elif(seatdate_key=='day_2_07_00'):
        seat.day_2_07_00 = stu_id
    elif(seatdate_key=='day_2_07_30'):
        seat.day_2_07_30 = stu_id
    elif(seatdate_key=='day_2_08_00'):
        seat.day_2_08_00 = stu_id
    elif(seatdate_key=='day_2_08_30'):
        seat.day_2_08_30 = stu_id
    elif(seatdate_key=='day_2_17_00'):
        seat.day_2_17_00 = stu_id
    elif(seatdate_key=='day_2_17_30'):
        seat.day_2_17_30 = stu_id
    elif(seatdate_key=='day_2_18_00'):
        seat.day_2_18_00 = stu_id
    elif(seatdate_key=='day_2_18_30'):
        seat.day_2_18_30 = stu_id
    elif(seatdate_key=='day_2_19_00'):
        seat.day_2_19_00 = stu_id
    elif(seatdate_key=='day_2_19_30'):
        seat.day_2_19_30 = stu_id
    elif(seatdate_key=='day_2_20_00'):
        seat.day_2_20_00 = stu_id
    elif(seatdate_key=='day_2_20_30'):
        seat.day_2_20_30 = stu_id
    elif(seatdate_key=='day_2_21_00'):
        seat.day_2_21_00 = stu_id
    elif(seatdate_key=='day_2_21_30'):
        seat.day_2_21_30 = stu_id
    elif(seatdate_key=='day_2_22_00'):
        seat.day_2_22_00 = stu_id
    elif(seatdate_key=='day_2_22_30'):
        seat.day_2_22_30 = stu_id
    elif(seatdate_key=='day_2_23_00'):
        seat.day_2_23_00 = stu_id
    elif(seatdate_key=='day_2_23_30'):
        seat.day_2_23_30 = stu_id
    elif(seatdate_key=='day_3_00_00'):
        seat.day_3_00_00 = stu_id
    elif(seatdate_key=='day_3_00_30'):
        seat.day_3_00_30 = stu_id
    elif(seatdate_key=='day_3_01_00'):
        seat.day_3_01_00 = stu_id
    elif(seatdate_key=='day_3_01_30'):
        seat.day_3_01_30 = stu_id
    elif(seatdate_key=='day_3_02_00'):
        seat.day_3_02_00 = stu_id
    elif(seatdate_key=='day_3_02_30'):
        seat.day_3_02_30 = stu_id
    elif(seatdate_key=='day_3_03_00'):
        seat.day_3_03_00 = stu_id
    elif(seatdate_key=='day_3_03_30'):
        seat.day_3_03_30 = stu_id
    elif(seatdate_key=='day_3_04_00'):
        seat.day_3_04_00 = stu_id
    elif(seatdate_key=='day_3_04_30'):
        seat.day_3_04_30 = stu_id
    elif(seatdate_key=='day_3_05_00'):
        seat.day_3_05_00 = stu_id   
    elif(seatdate_key=='day_3_05_30'):
        seat.day_3_05_30 = stu_id
    elif(seatdate_key=='day_3_06_00'):
        seat.day_3_06_00 = stu_id
    elif(seatdate_key=='day_3_06_30'):
        seat.day_3_06_30 = stu_id
    elif(seatdate_key=='day_3_07_00'):
        seat.day_3_07_00 = stu_id
    elif(seatdate_key=='day_3_07_30'):
        seat.day_3_07_30 = stu_id
    elif(seatdate_key=='day_3_08_00'):
        seat.day_3_08_00 = stu_id
    elif(seatdate_key=='day_3_08_30'):
        seat.day_3_08_30 = stu_id
    elif(seatdate_key=='day_3_17_00'):
        seat.day_3_17_00 = stu_id
    elif(seatdate_key=='day_3_17_30'):
        seat.day_3_17_30 = stu_id
    elif(seatdate_key=='day_3_18_00'):
        seat.day_3_18_00 = stu_id
    elif(seatdate_key=='day_3_18_30'):
        seat.day_3_18_30 = stu_id
    elif(seatdate_key=='day_3_19_00'):
        seat.day_3_19_00 = stu_id
    elif(seatdate_key=='day_3_19_30'):
        seat.day_3_19_30 = stu_id
    elif(seatdate_key=='day_3_20_00'):
        seat.day_3_20_00 = stu_id
    elif(seatdate_key=='day_3_20_30'):
        seat.day_3_20_30 = stu_id
    elif(seatdate_key=='day_3_21_00'):
        seat.day_3_21_00 = stu_id
    elif(seatdate_key=='day_3_21_30'):
        seat.day_3_21_30 = stu_id
    elif(seatdate_key=='day_3_22_00'):
        seat.day_3_22_00 = stu_id
    elif(seatdate_key=='day_3_22_30'):
        seat.day_3_22_30 = stu_id
    elif(seatdate_key=='day_3_23_00'):
        seat.day_3_23_00 = stu_id
    elif(seatdate_key=='day_3_23_30'):
        seat.day_3_23_30 = stu_id
    elif(seatdate_key=='day_4_00_00'): 
        seat.day_4_00_00 = stu_id
    elif(seatdate_key=='day_4_00_30'):
        seat.day_4_00_30 = stu_id
    elif(seatdate_key=='day_4_01_00'):
        seat.day_4_01_00 = stu_id
    elif(seatdate_key=='day_4_01_30'):
        seat.day_4_01_30 = stu_id
    elif(seatdate_key=='day_4_02_00'):
        seat.day_4_02_00 = stu_id
    elif(seatdate_key=='day_4_02_30'):
        seat.day_4_02_30 = stu_id
    elif(seatdate_key=='day_4_03_00'):
        seat.day_4_03_00 = stu_id
    elif(seatdate_key=='day_4_03_30'):
        seat.day_4_03_30 = stu_id
    elif(seatdate_key=='day_4_04_00'):
        seat.day_4_04_00 = stu_id
    elif(seatdate_key=='day_4_04_30'):
        seat.day_4_04_30 = stu_id
    elif(seatdate_key=='day_4_05_00'):
        seat.day_4_05_00 = stu_id
    elif(seatdate_key=='day_4_05_30'):
        seat.day_4_05_30 = stu_id
    elif(seatdate_key=='day_4_06_00'):
        seat.day_4_06_00 = stu_id
    elif(seatdate_key=='day_4_06_30'):
        seat.day_4_06_30 = stu_id
    elif(seatdate_key=='day_4_07_00'):
        seat.day_4_07_00 = stu_id
    elif(seatdate_key=='day_4_07_30'):
        seat.day_4_07_30 = stu_id
    elif(seatdate_key=='day_4_08_00'):
        seat.day_4_08_00 = stu_id
    elif(seatdate_key=='day_4_08_30'):
        seat.day_4_08_30 = stu_id
    elif(seatdate_key=='day_4_17_00'):
        seat.day_4_17_00 = stu_id
    elif(seatdate_key=='day_4_17_30'):
        seat.day_4_17_30 = stu_id
    elif(seatdate_key=='day_4_18_00'):
        seat.day_4_18_00 = stu_id
    elif(seatdate_key=='day_4_18_30'):
        seat.day_4_18_30 = stu_id
    elif(seatdate_key=='day_4_19_00'):
        seat.day_4_19_00 = stu_id
    elif(seatdate_key=='day_4_19_30'):
        seat.day_4_19_30 = stu_id
    elif(seatdate_key=='day_4_20_00'):
        seat.day_4_20_00 = stu_id
    elif(seatdate_key=='day_4_20_30'):
        seat.day_4_20_30 = stu_id
    elif(seatdate_key=='day_4_21_00'):
        seat.day_4_21_00 = stu_id
    elif(seatdate_key=='day_4_21_30'):
        seat.day_4_21_30 = stu_id
    elif(seatdate_key=='day_4_22_00'):
        seat.day_4_22_00 = stu_id
    elif(seatdate_key=='day_4_22_30'):
        seat.day_4_22_30 = stu_id
    elif(seatdate_key=='day_4_23_00'):
        seat.day_4_23_00 = stu_id
    elif(seatdate_key=='day_4_23_30'):
        seat.day_4_23_30 = stu_id
    elif(seatdate_key=='day_5_00_00'):
        seat.day_5_00_00 = stu_id
    elif(seatdate_key=='day_5_00_30'):
        seat.day_5_00_30 = stu_id
    elif(seatdate_key=='day_5_01_00'):
        seat.day_5_01_00 = stu_id
    elif(seatdate_key=='day_5_01_30'):
        seat.day_5_01_30 = stu_id
    elif(seatdate_key=='day_5_02_00'):
        seat.day_5_02_00 = stu_id
    elif(seatdate_key=='day_5_02_30'):
        seat.day_5_02_30 = stu_id
    elif(seatdate_key=='day_5_03_00'):
        seat.day_5_03_00 = stu_id
    elif(seatdate_key=='day_5_03_30'):
        seat.day_5_03_30 = stu_id
    elif(seatdate_key=='day_5_04_00'):
        seat.day_5_04_00 = stu_id
    elif(seatdate_key=='day_5_04_30'):
        seat.day_5_04_30 = stu_id
    elif(seatdate_key=='day_5_05_00'):
        seat.day_5_05_00 = stu_id
    elif(seatdate_key=='day_5_05_30'):
        seat.day_5_05_30 = stu_id
    elif(seatdate_key=='day_5_06_00'):
        seat.day_5_06_00 = stu_id
    elif(seatdate_key=='day_5_06_30'):
        seat.day_5_06_30 = stu_id
    elif(seatdate_key=='day_5_07_00'):
        seat.day_5_07_00 = stu_id
    elif(seatdate_key=='day_5_07_30'):
        seat.day_5_07_30 = stu_id
    elif(seatdate_key=='day_5_08_00'):
        seat.day_5_08_00 = stu_id
    elif(seatdate_key=='day_5_08_30'):
        seat.day_5_08_30 = stu_id
    elif(seatdate_key=='day_5_17_00'):
        seat.day_5_17_00 = stu_id
    elif(seatdate_key=='day_5_17_30'):
        seat.day_5_17_30 = stu_id
    elif(seatdate_key=='day_5_18_00'):
        seat.day_5_18_00 = stu_id
    elif(seatdate_key=='day_5_18_30'):
        seat.day_5_18_30 = stu_id
    elif(seatdate_key=='day_5_19_00'):
        seat.day_5_19_00 = stu_id
    elif(seatdate_key=='day_5_19_30'):
        seat.day_5_19_30 = stu_id
    elif(seatdate_key=='day_5_20_00'):
        seat.day_5_20_00 = stu_id
    elif(seatdate_key=='day_5_20_30'):
        seat.day_5_20_30 = stu_id
    elif(seatdate_key=='day_5_21_00'):
        seat.day_5_21_00 = stu_id
    elif(seatdate_key=='day_5_21_30'):
        seat.day_5_21_30 = stu_id
    elif(seatdate_key=='day_5_22_00'):
        seat.day_5_22_00 = stu_id
    elif(seatdate_key=='day_5_22_30'):
        seat.day_5_22_30 = stu_id
    elif(seatdate_key=='day_5_23_00'):
        seat.day_5_23_00 = stu_id
    elif(seatdate_key=='day_5_23_30'):
        seat.day_5_23_30 = stu_id
    db.session.commit()

def clear_selected_time_record(seatdate_key,seat_num):
    seat = Seat.query.filter_by(seat_num=seat_num).first()
    if(seatdate_key=='day_1_00_00'):
        seat.day_1_00_00 =  '0'
    elif(seatdate_key=='day_1_00_30'):
        seat.day_1_00_30 =  '0'
    elif(seatdate_key=='day_1_01_00'):
        seat.day_1_01_00 =  '0'
    elif(seatdate_key=='day_1_01_30'):
        seat.day_1_01_30 =  '0'
    elif(seatdate_key=='day_1_02_00'):
        seat.day_1_02_00 =  '0'
    elif(seatdate_key=='day_1_02_30'):
        seat.day_1_02_30 =  '0'
    elif(seatdate_key=='day_1_03_00'):
        seat.day_1_03_00 =  '0'
    elif(seatdate_key=='day_1_03_30'):
        seat.day_1_03_30 =  '0'
    elif(seatdate_key=='day_1_04_00'):
        seat.day_1_04_00 =  '0'
    elif(seatdate_key=='day_1_04_30'):
        seat.day_1_04_30 =  '0'
    elif(seatdate_key=='day_1_05_00'):
        seat.day_1_05_00 =  '0'
    elif(seatdate_key=='day_1_05_30'):
        seat.day_1_05_30 =  '0'
    elif(seatdate_key=='day_1_06_00'):
        seat.day_1_06_00 =  '0'
    elif(seatdate_key=='day_1_06_30'):
        seat.day_1_06_30 =  '0'
    elif(seatdate_key=='day_1_07_00'):
        seat.day_1_07_00 =  '0'
    elif(seatdate_key=='day_1_07_30'):
        seat.day_1_07_30 =  '0'
    elif(seatdate_key=='day_1_08_00'):
        seat.day_1_08_00 =  '0'
    elif(seatdate_key=='day_1_08_30'):
        seat.day_1_08_30 =  '0'
    elif(seatdate_key=='day_1_17_00'):
        seat.day_1_17_00 =  '0'
    elif(seatdate_key=='day_1_17_30'):
        seat.day_1_17_30 =  '0'
    elif(seatdate_key=='day_1_18_00'):
        seat.day_1_18_00 =  '0'
    elif(seatdate_key=='day_1_18_30'):
        seat.day_1_18_30 =  '0'
    elif(seatdate_key=='day_1_19_00'):
        seat.day_1_19_00 =  '0'
    elif(seatdate_key=='day_1_19_30'):
        seat.day_1_19_30 =  '0'
    elif(seatdate_key=='day_1_20_00'):
        seat.day_1_20_00 =  '0'
    elif(seatdate_key=='day_1_20_30'):
        seat.day_1_20_30 =  '0'
    elif(seatdate_key=='day_1_21_00'):
        seat.day_1_21_00 =  '0'
    elif(seatdate_key=='day_1_21_30'):
        seat.day_1_21_30 =  '0'
    elif(seatdate_key=='day_1_22_00'):
        seat.day_1_22_00 =  '0'
    elif(seatdate_key=='day_1_22_30'):
        seat.day_1_22_30 =  '0'
    elif(seatdate_key=='day_1_23_00'):
        seat.day_1_23_00 =  '0'
    elif(seatdate_key=='day_1_23_30'):
        seat.day_1_23_30 =  '0'
    elif(seatdate_key=='day_2_00_00'):
        seat.day_2_00_00 =  '0'
    elif(seatdate_key=='day_2_00_30'):
        seat.day_2_00_30 =  '0'
    elif(seatdate_key=='day_2_01_00'):
        seat.day_2_01_00 =  '0'
    elif(seatdate_key=='day_2_01_30'):
        seat.day_2_01_30 =  '0'
    elif(seatdate_key=='day_2_02_00'):
        seat.day_2_02_00 =  '0'
    elif(seatdate_key=='day_2_02_30'):
        seat.day_2_02_30 =  '0'
    elif(seatdate_key=='day_2_03_00'):
        seat.day_2_03_00 =  '0'
    elif(seatdate_key=='day_2_03_30'):
        seat.day_2_03_30 =  '0'
    elif(seatdate_key=='day_2_04_00'):
        seat.day_2_04_00 =  '0'
    elif(seatdate_key=='day_2_04_30'):
        seat.day_2_04_30 =  '0'
    elif(seatdate_key=='day_2_05_00'):
        seat.day_2_05_00 =  '0'
    elif(seatdate_key=='day_2_05_30'):
        seat.day_2_05_30 =  '0'
    elif(seatdate_key=='day_2_06_00'):
        seat.day_2_06_00 =  '0'
    elif(seatdate_key=='day_2_06_30'):
        seat.day_2_06_30 =  '0'
    elif(seatdate_key=='day_2_07_00'):
        seat.day_2_07_00 =  '0'
    elif(seatdate_key=='day_2_07_30'):
        seat.day_2_07_30 =  '0'
    elif(seatdate_key=='day_2_08_00'):
        seat.day_2_08_00 =  '0'
    elif(seatdate_key=='day_2_08_30'):
        seat.day_2_08_30 =  '0'
    elif(seatdate_key=='day_2_17_00'):
        seat.day_2_17_00 =  '0'
    elif(seatdate_key=='day_2_17_30'):
        seat.day_2_17_30 =  '0'
    elif(seatdate_key=='day_2_18_00'):
        seat.day_2_18_00 =  '0'
    elif(seatdate_key=='day_2_18_30'):
        seat.day_2_18_30 =  '0'
    elif(seatdate_key=='day_2_19_00'):
        seat.day_2_19_00 =  '0'
    elif(seatdate_key=='day_2_19_30'):
        seat.day_2_19_30 =  '0'
    elif(seatdate_key=='day_2_20_00'):
        seat.day_2_20_00 =  '0'
    elif(seatdate_key=='day_2_20_30'):
        seat.day_2_20_30 =  '0'
    elif(seatdate_key=='day_2_21_00'):
        seat.day_2_21_00 =  '0'
    elif(seatdate_key=='day_2_21_30'):
        seat.day_2_21_30 =  '0'
    elif(seatdate_key=='day_2_22_00'):
        seat.day_2_22_00 =  '0'
    elif(seatdate_key=='day_2_22_30'):
        seat.day_2_22_30 =  '0'
    elif(seatdate_key=='day_2_23_00'):
        seat.day_2_23_00 =  '0'
    elif(seatdate_key=='day_2_23_30'):
        seat.day_2_23_30 =  '0'
    elif(seatdate_key=='day_3_00_00'):
        seat.day_3_00_00 =  '0'
    elif(seatdate_key=='day_3_00_30'):
        seat.day_3_00_30 =  '0'
    elif(seatdate_key=='day_3_01_00'):
        seat.day_3_01_00 =  '0'
    elif(seatdate_key=='day_3_01_30'):
        seat.day_3_01_30 =  '0'
    elif(seatdate_key=='day_3_02_00'):
        seat.day_3_02_00 =  '0'
    elif(seatdate_key=='day_3_02_30'):
        seat.day_3_02_30 =  '0'
    elif(seatdate_key=='day_3_03_00'):
        seat.day_3_03_00 =  '0'
    elif(seatdate_key=='day_3_03_30'):
        seat.day_3_03_30 =  '0'
    elif(seatdate_key=='day_3_04_00'):
        seat.day_3_04_00 =  '0'
    elif(seatdate_key=='day_3_04_30'):
        seat.day_3_04_30 =  '0'
    elif(seatdate_key=='day_3_05_00'):
        seat.day_3_05_00 =  '0'   
    elif(seatdate_key=='day_3_05_30'):
        seat.day_3_05_30 =  '0'
    elif(seatdate_key=='day_3_06_00'):
        seat.day_3_06_00 =  '0'
    elif(seatdate_key=='day_3_06_30'):
        seat.day_3_06_30 =  '0'
    elif(seatdate_key=='day_3_07_00'):
        seat.day_3_07_00 =  '0'
    elif(seatdate_key=='day_3_07_30'):
        seat.day_3_07_30 =  '0'
    elif(seatdate_key=='day_3_08_00'):
        seat.day_3_08_00 =  '0'
    elif(seatdate_key=='day_3_08_30'):
        seat.day_3_08_30 =  '0'
    elif(seatdate_key=='day_3_17_00'):
        seat.day_3_17_00 =  '0'
    elif(seatdate_key=='day_3_17_30'):
        seat.day_3_17_30 =  '0'
    elif(seatdate_key=='day_3_18_00'):
        seat.day_3_18_00 =  '0'
    elif(seatdate_key=='day_3_18_30'):
        seat.day_3_18_30 =  '0'
    elif(seatdate_key=='day_3_19_00'):
        seat.day_3_19_00 =  '0'
    elif(seatdate_key=='day_3_19_30'):
        seat.day_3_19_30 =  '0'
    elif(seatdate_key=='day_3_20_00'):
        seat.day_3_20_00 =  '0'
    elif(seatdate_key=='day_3_20_30'):
        seat.day_3_20_30 =  '0'
    elif(seatdate_key=='day_3_21_00'):
        seat.day_3_21_00 =  '0'
    elif(seatdate_key=='day_3_21_30'):
        seat.day_3_21_30 =  '0'
    elif(seatdate_key=='day_3_22_00'):
        seat.day_3_22_00 =  '0'
    elif(seatdate_key=='day_3_22_30'):
        seat.day_3_22_30 =  '0'
    elif(seatdate_key=='day_3_23_00'):
        seat.day_3_23_00 =  '0'
    elif(seatdate_key=='day_3_23_30'):
        seat.day_3_23_30 =  '0'
    elif(seatdate_key=='day_4_00_00'): 
        seat.day_4_00_00 =  '0'
    elif(seatdate_key=='day_4_00_30'):
        seat.day_4_00_30 =  '0'
    elif(seatdate_key=='day_4_01_00'):
        seat.day_4_01_00 =  '0'
    elif(seatdate_key=='day_4_01_30'):
        seat.day_4_01_30 =  '0'
    elif(seatdate_key=='day_4_02_00'):
        seat.day_4_02_00 =  '0'
    elif(seatdate_key=='day_4_02_30'):
        seat.day_4_02_30 =  '0'
    elif(seatdate_key=='day_4_03_00'):
        seat.day_4_03_00 =  '0'
    elif(seatdate_key=='day_4_03_30'):
        seat.day_4_03_30 =  '0'
    elif(seatdate_key=='day_4_04_00'):
        seat.day_4_04_00 =  '0'
    elif(seatdate_key=='day_4_04_30'):
        seat.day_4_04_30 =  '0'
    elif(seatdate_key=='day_4_05_00'):
        seat.day_4_05_00 =  '0'
    elif(seatdate_key=='day_4_05_30'):
        seat.day_4_05_30 =  '0'
    elif(seatdate_key=='day_4_06_00'):
        seat.day_4_06_00 =  '0'
    elif(seatdate_key=='day_4_06_30'):
        seat.day_4_06_30 =  '0'
    elif(seatdate_key=='day_4_07_00'):
        seat.day_4_07_00 =  '0'
    elif(seatdate_key=='day_4_07_30'):
        seat.day_4_07_30 =  '0'
    elif(seatdate_key=='day_4_08_00'):
        seat.day_4_08_00 =  '0'
    elif(seatdate_key=='day_4_08_30'):
        seat.day_4_08_30 =  '0'
    elif(seatdate_key=='day_4_17_00'):
        seat.day_4_17_00 =  '0'
    elif(seatdate_key=='day_4_17_30'):
        seat.day_4_17_30 =  '0'
    elif(seatdate_key=='day_4_18_00'):
        seat.day_4_18_00 =  '0'
    elif(seatdate_key=='day_4_18_30'):
        seat.day_4_18_30 =  '0'
    elif(seatdate_key=='day_4_19_00'):
        seat.day_4_19_00 =  '0'
    elif(seatdate_key=='day_4_19_30'):
        seat.day_4_19_30 =  '0'
    elif(seatdate_key=='day_4_20_00'):
        seat.day_4_20_00 =  '0'
    elif(seatdate_key=='day_4_20_30'):
        seat.day_4_20_30 =  '0'
    elif(seatdate_key=='day_4_21_00'):
        seat.day_4_21_00 =  '0'
    elif(seatdate_key=='day_4_21_30'):
        seat.day_4_21_30 =  '0'
    elif(seatdate_key=='day_4_22_00'):
        seat.day_4_22_00 =  '0'
    elif(seatdate_key=='day_4_22_30'):
        seat.day_4_22_30 =  '0'
    elif(seatdate_key=='day_4_23_00'):
        seat.day_4_23_00 =  '0'
    elif(seatdate_key=='day_4_23_30'):
        seat.day_4_23_30 =  '0'
    elif(seatdate_key=='day_5_00_00'):
        seat.day_5_00_00 =  '0'
    elif(seatdate_key=='day_5_00_30'):
        seat.day_5_00_30 =  '0'
    elif(seatdate_key=='day_5_01_00'):
        seat.day_5_01_00 =  '0'
    elif(seatdate_key=='day_5_01_30'):
        seat.day_5_01_30 =  '0'
    elif(seatdate_key=='day_5_02_00'):
        seat.day_5_02_00 =  '0'
    elif(seatdate_key=='day_5_02_30'):
        seat.day_5_02_30 =  '0'
    elif(seatdate_key=='day_5_03_00'):
        seat.day_5_03_00 =  '0'
    elif(seatdate_key=='day_5_03_30'):
        seat.day_5_03_30 =  '0'
    elif(seatdate_key=='day_5_04_00'):
        seat.day_5_04_00 =  '0'
    elif(seatdate_key=='day_5_04_30'):
        seat.day_5_04_30 =  '0'
    elif(seatdate_key=='day_5_05_00'):
        seat.day_5_05_00 =  '0'
    elif(seatdate_key=='day_5_05_30'):
        seat.day_5_05_30 =  '0'
    elif(seatdate_key=='day_5_06_00'):
        seat.day_5_06_00 =  '0'
    elif(seatdate_key=='day_5_06_30'):
        seat.day_5_06_30 =  '0'
    elif(seatdate_key=='day_5_07_00'):
        seat.day_5_07_00 =  '0'
    elif(seatdate_key=='day_5_07_30'):
        seat.day_5_07_30 =  '0'
    elif(seatdate_key=='day_5_08_00'):
        seat.day_5_08_00 =  '0'
    elif(seatdate_key=='day_5_08_30'):
        seat.day_5_08_30 =  '0'
    elif(seatdate_key=='day_5_17_00'):
        seat.day_5_17_00 =  '0'
    elif(seatdate_key=='day_5_17_30'):
        seat.day_5_17_30 =  '0'
    elif(seatdate_key=='day_5_18_00'):
        seat.day_5_18_00 =  '0'
    elif(seatdate_key=='day_5_18_30'):
        seat.day_5_18_30 =  '0'
    elif(seatdate_key=='day_5_19_00'):
        seat.day_5_19_00 =  '0'
    elif(seatdate_key=='day_5_19_30'):
        seat.day_5_19_30 =  '0'
    elif(seatdate_key=='day_5_20_00'):
        seat.day_5_20_00 =  '0'
    elif(seatdate_key=='day_5_20_30'):
        seat.day_5_20_30 =  '0'
    elif(seatdate_key=='day_5_21_00'):
        seat.day_5_21_00 =  '0'
    elif(seatdate_key=='day_5_21_30'):
        seat.day_5_21_30 =  '0'
    elif(seatdate_key=='day_5_22_00'):
        seat.day_5_22_00 =  '0'
    elif(seatdate_key=='day_5_22_30'):
        seat.day_5_22_30 =  '0'
    elif(seatdate_key=='day_5_23_00'):
        seat.day_5_23_00 =  '0'
    elif(seatdate_key=='day_5_23_30'):
        seat.day_5_23_30 =  '0'
    db.session.commit()

def clear_all_time_record(seat):
    seat.day_1_00_00 = '0'
    seat.day_1_00_30 = '0'
    seat.day_1_01_00 = '0'
    seat.day_1_01_30 = '0'
    seat.day_1_02_00 = '0'
    seat.day_1_02_30 = '0'
    seat.day_1_03_00 = '0'
    seat.day_1_03_30 = '0'
    seat.day_1_04_00 = '0'
    seat.day_1_04_30 = '0'
    seat.day_1_05_00 = '0'
    seat.day_1_05_30 = '0'
    seat.day_1_06_00 = '0'
    seat.day_1_06_30 = '0'
    seat.day_1_07_00 = '0'
    seat.day_1_07_30 = '0'
    seat.day_1_08_00 = '0'
    seat.day_1_08_30 = '0'
    seat.day_1_17_00 = '0'
    seat.day_1_17_30 = '0'
    seat.day_1_18_00 = '0'
    seat.day_1_18_30 = '0'
    seat.day_1_19_00 = '0'
    seat.day_1_19_30 = '0'
    seat.day_1_20_00 = '0'
    seat.day_1_20_30 = '0'
    seat.day_1_21_00 = '0'
    seat.day_1_21_30 = '0'
    seat.day_1_22_00 = '0'
    seat.day_1_22_30 = '0'
    seat.day_1_23_00 = '0'
    seat.day_1_23_30 = '0'
    seat.day_2_00_00 = '0'
    seat.day_2_00_30 = '0'
    seat.day_2_01_00 = '0'
    seat.day_2_01_30 = '0'
    seat.day_2_02_00 = '0'
    seat.day_2_02_30 = '0'
    seat.day_2_03_00 = '0'
    seat.day_2_03_30 = '0'
    seat.day_2_04_00 = '0'
    seat.day_2_04_30 = '0'
    seat.day_2_05_00 = '0'
    seat.day_2_05_30 = '0'
    seat.day_2_06_00 = '0'
    seat.day_2_06_30 = '0'
    seat.day_2_07_00 = '0'
    seat.day_2_07_30 = '0'
    seat.day_2_08_00 = '0'
    seat.day_2_08_30 = '0'
    seat.day_2_17_00 = '0'
    seat.day_2_17_30 = '0'
    seat.day_2_18_00 = '0'
    seat.day_2_18_30 = '0'
    seat.day_2_19_00 = '0'
    seat.day_2_19_30 = '0'
    seat.day_2_20_00 = '0'
    seat.day_2_20_30 = '0'
    seat.day_2_21_00 = '0'
    seat.day_2_21_30 = '0'
    seat.day_2_22_00 = '0'
    seat.day_2_22_30 = '0'
    seat.day_2_23_00 = '0'
    seat.day_2_23_30 = '0'
    seat.day_3_00_00 = '0'
    seat.day_3_00_30 = '0'
    seat.day_3_01_00 = '0'
    seat.day_3_01_30 = '0'
    seat.day_3_02_00 = '0'
    seat.day_3_02_30 = '0'
    seat.day_3_03_00 = '0'
    seat.day_3_03_30 = '0'
    seat.day_3_04_00 = '0'
    seat.day_3_04_30 = '0'
    seat.day_3_05_00 = '0'   
    seat.day_3_05_30 = '0'
    seat.day_3_06_00 = '0'
    seat.day_3_06_30 = '0'
    seat.day_3_07_00 = '0'
    seat.day_3_07_30 = '0'
    seat.day_3_08_00 = '0'
    seat.day_3_08_30 = '0'
    seat.day_3_17_00 = '0'
    seat.day_3_17_30 = '0'
    seat.day_3_18_00 = '0'
    seat.day_3_18_30 = '0'
    seat.day_3_19_00 = '0'
    seat.day_3_19_30 = '0'
    seat.day_3_20_00 = '0'
    seat.day_3_20_30 = '0'
    seat.day_3_21_00 = '0'
    seat.day_3_21_30 = '0'
    seat.day_3_22_00 = '0'
    seat.day_3_22_30 = '0'
    seat.day_3_23_00 = '0'
    seat.day_3_23_30 = '0'
    seat.day_4_00_00 = '0'
    seat.day_4_00_30 = '0'
    seat.day_4_01_00 = '0'
    seat.day_4_01_30 = '0'
    seat.day_4_02_00 = '0'
    seat.day_4_02_30 = '0'
    seat.day_4_03_00 = '0'
    seat.day_4_03_30 = '0'
    seat.day_4_04_00 = '0'
    seat.day_4_04_30 = '0'
    seat.day_4_05_00 = '0'
    seat.day_4_05_30 = '0'
    seat.day_4_06_00 = '0'
    seat.day_4_06_30 = '0'
    seat.day_4_07_00 = '0'
    seat.day_4_07_30 = '0'
    seat.day_4_08_00 = '0'
    seat.day_4_08_30 = '0'
    seat.day_4_17_00 = '0'
    seat.day_4_17_30 = '0'
    seat.day_4_18_00 = '0'
    seat.day_4_18_30 = '0'
    seat.day_4_19_00 = '0'
    seat.day_4_19_30 = '0'
    seat.day_4_20_00 = '0'
    seat.day_4_20_30 = '0'
    seat.day_4_21_00 = '0'
    seat.day_4_21_30 = '0'
    seat.day_4_22_00 = '0'
    seat.day_4_22_30 = '0'
    seat.day_4_23_00 = '0'
    seat.day_4_23_30 = '0'
    seat.day_5_00_00 = '0'
    seat.day_5_00_30 = '0'
    seat.day_5_01_00 = '0'
    seat.day_5_01_30 = '0'
    seat.day_5_02_00 = '0'
    seat.day_5_02_30 = '0'
    seat.day_5_03_00 = '0'
    seat.day_5_03_30 = '0'
    seat.day_5_04_00 = '0'
    seat.day_5_04_30 = '0'
    seat.day_5_05_00 = '0'
    seat.day_5_05_30 = '0'
    seat.day_5_06_00 = '0'
    seat.day_5_06_30 = '0'
    seat.day_5_07_00 = '0'
    seat.day_5_07_30 = '0'
    seat.day_5_08_00 = '0'
    seat.day_5_08_30 = '0'
    seat.day_5_17_00 = '0'
    seat.day_5_17_30 = '0'
    seat.day_5_18_00 = '0'
    seat.day_5_18_30 = '0'
    seat.day_5_19_00 = '0'
    seat.day_5_19_30 = '0'
    seat.day_5_20_00 = '0'
    seat.day_5_20_30 = '0'
    seat.day_5_21_00 = '0'
    seat.day_5_21_30 = '0'
    seat.day_5_22_00 = '0'
    seat.day_5_22_30 = '0'
    seat.day_5_23_00 = '0'
    seat.day_5_23_30 = '0'

def clear_all_day1_record(seat):
    seat.day_1_00_00 = '0'
    seat.day_1_00_30 = '0'
    seat.day_1_01_00 = '0'
    seat.day_1_01_30 = '0'
    seat.day_1_02_00 = '0'
    seat.day_1_02_30 = '0'
    seat.day_1_03_00 = '0'
    seat.day_1_03_30 = '0'
    seat.day_1_04_00 = '0'
    seat.day_1_04_30 = '0'
    seat.day_1_05_00 = '0'
    seat.day_1_05_30 = '0'
    seat.day_1_06_00 = '0'
    seat.day_1_06_30 = '0'
    seat.day_1_07_00 = '0'
    seat.day_1_07_30 = '0'
    seat.day_1_08_00 = '0'
    seat.day_1_08_30 = '0'
    seat.day_1_17_00 = '0'
    seat.day_1_17_30 = '0'
    seat.day_1_18_00 = '0'
    seat.day_1_18_30 = '0'
    seat.day_1_19_00 = '0'
    seat.day_1_19_30 = '0'
    seat.day_1_20_00 = '0'
    seat.day_1_20_30 = '0'
    seat.day_1_21_00 = '0'
    seat.day_1_21_30 = '0'
    seat.day_1_22_00 = '0'
    seat.day_1_22_30 = '0'
    seat.day_1_23_00 = '0'
    seat.day_1_23_30 = '0'

def move_to_next_day(seat):
    seat.day_1_00_00 = seat.day_2_00_00
    seat.day_1_00_30 = seat.day_2_00_30
    seat.day_1_01_00 = seat.day_2_01_00
    seat.day_1_01_30 = seat.day_2_01_30
    seat.day_1_02_00 = seat.day_2_02_00
    seat.day_1_02_30 = seat.day_2_02_30
    seat.day_1_03_00 = seat.day_2_03_00
    seat.day_1_03_30 = seat.day_2_03_30
    seat.day_1_04_00 = seat.day_2_04_00
    seat.day_1_04_30 = seat.day_2_04_30
    seat.day_1_05_00 = seat.day_2_05_00
    seat.day_1_05_30 = seat.day_2_05_30
    seat.day_1_06_00 = seat.day_2_06_00
    seat.day_1_06_30 = seat.day_2_06_30
    seat.day_1_07_00 = seat.day_2_07_00
    seat.day_1_07_30 = seat.day_2_07_30
    seat.day_1_08_00 = seat.day_2_08_00
    seat.day_1_08_30 = seat.day_2_08_30
    seat.day_1_17_00 = seat.day_2_17_00
    seat.day_1_17_30 = seat.day_2_17_30
    seat.day_1_18_00 = seat.day_2_18_00
    seat.day_1_18_30 = seat.day_2_18_30
    seat.day_1_19_00 = seat.day_2_19_00
    seat.day_1_19_30 = seat.day_2_19_30
    seat.day_1_20_00 = seat.day_2_20_00
    seat.day_1_20_30 = seat.day_2_20_30
    seat.day_1_21_00 = seat.day_2_21_00
    seat.day_1_21_30 = seat.day_2_21_30
    seat.day_1_22_00 = seat.day_2_22_00
    seat.day_1_22_30 = seat.day_2_22_30
    seat.day_1_23_00 = seat.day_2_23_00
    seat.day_1_23_30 = seat.day_2_23_30

    seat.day_2_00_00 = seat.day_3_00_00
    seat.day_2_00_30 = seat.day_3_00_30
    seat.day_2_01_00 = seat.day_3_01_00
    seat.day_2_01_30 = seat.day_3_01_30
    seat.day_2_02_00 = seat.day_3_02_00
    seat.day_2_02_30 = seat.day_3_02_30
    seat.day_2_03_00 = seat.day_3_03_00
    seat.day_2_03_30 = seat.day_3_03_30
    seat.day_2_04_00 = seat.day_3_04_00
    seat.day_2_04_30 = seat.day_3_04_30
    seat.day_2_05_00 = seat.day_3_05_00
    seat.day_2_05_30 = seat.day_3_05_30
    seat.day_2_06_00 = seat.day_3_06_00
    seat.day_2_06_30 = seat.day_3_06_30
    seat.day_2_07_00 = seat.day_3_07_00
    seat.day_2_07_30 = seat.day_3_07_30
    seat.day_2_08_00 = seat.day_3_08_00
    seat.day_2_08_30 = seat.day_3_08_30
    seat.day_2_17_00 = seat.day_3_17_00
    seat.day_2_17_30 = seat.day_3_17_30
    seat.day_2_18_00 = seat.day_3_18_00
    seat.day_2_18_30 = seat.day_3_18_30
    seat.day_2_19_00 = seat.day_3_19_00
    seat.day_2_19_30 = seat.day_3_19_30
    seat.day_2_20_00 = seat.day_3_20_00
    seat.day_2_20_30 = seat.day_3_20_30
    seat.day_2_21_00 = seat.day_3_21_00
    seat.day_2_21_30 = seat.day_3_21_30
    seat.day_2_22_00 = seat.day_3_22_00
    seat.day_2_22_30 = seat.day_3_22_30
    seat.day_2_23_00 = seat.day_3_23_00
    seat.day_2_23_30 = seat.day_3_23_30

    seat.day_3_00_00 = seat.day_4_00_00
    seat.day_3_00_30 = seat.day_4_00_30
    seat.day_3_01_00 = seat.day_4_01_00
    seat.day_3_01_30 = seat.day_4_01_30
    seat.day_3_02_00 = seat.day_4_02_00
    seat.day_3_02_30 = seat.day_4_02_30
    seat.day_3_03_00 = seat.day_4_03_00
    seat.day_3_03_30 = seat.day_4_03_30
    seat.day_3_04_00 = seat.day_4_04_00
    seat.day_3_04_30 = seat.day_4_04_30
    seat.day_3_05_00 = seat.day_4_05_00
    seat.day_3_05_30 = seat.day_4_05_30
    seat.day_3_06_00 = seat.day_4_06_00
    seat.day_3_06_30 = seat.day_4_06_30
    seat.day_3_07_00 = seat.day_4_07_00
    seat.day_3_07_30 = seat.day_4_07_30
    seat.day_3_08_00 = seat.day_4_08_00
    seat.day_3_08_30 = seat.day_4_08_30
    seat.day_3_17_00 = seat.day_4_17_00
    seat.day_3_17_30 = seat.day_4_17_30
    seat.day_3_18_00 = seat.day_4_18_00
    seat.day_3_18_30 = seat.day_4_18_30
    seat.day_3_19_00 = seat.day_4_19_00
    seat.day_3_19_30 = seat.day_4_19_30
    seat.day_3_20_00 = seat.day_4_20_00
    seat.day_3_20_30 = seat.day_4_20_30
    seat.day_3_21_00 = seat.day_4_21_00
    seat.day_3_21_30 = seat.day_4_21_30
    seat.day_3_22_00 = seat.day_4_22_00
    seat.day_3_22_30 = seat.day_4_22_30
    seat.day_3_23_00 = seat.day_4_23_00
    seat.day_3_23_30 = seat.day_4_23_30

    seat.day_4_00_00 = seat.day_5_00_00
    seat.day_4_00_30 = seat.day_5_00_30
    seat.day_4_01_00 = seat.day_5_01_00
    seat.day_4_01_30 = seat.day_5_01_30
    seat.day_4_02_00 = seat.day_5_02_00
    seat.day_4_02_30 = seat.day_5_02_30
    seat.day_4_03_00 = seat.day_5_03_00
    seat.day_4_03_30 = seat.day_5_03_30
    seat.day_4_04_00 = seat.day_5_04_00
    seat.day_4_04_30 = seat.day_5_04_30
    seat.day_4_05_00 = seat.day_5_05_00
    seat.day_4_05_30 = seat.day_5_05_30
    seat.day_4_06_00 = seat.day_5_06_00
    seat.day_4_06_30 = seat.day_5_06_30
    seat.day_4_07_00 = seat.day_5_07_00
    seat.day_4_07_30 = seat.day_5_07_30
    seat.day_4_08_00 = seat.day_5_08_00
    seat.day_4_08_30 = seat.day_5_08_30
    seat.day_4_17_00 = seat.day_5_17_00
    seat.day_4_17_30 = seat.day_5_17_30
    seat.day_4_18_00 = seat.day_5_18_00
    seat.day_4_18_30 = seat.day_5_18_30
    seat.day_4_19_00 = seat.day_5_19_00
    seat.day_4_19_30 = seat.day_5_19_30
    seat.day_4_20_00 = seat.day_5_20_00
    seat.day_4_20_30 = seat.day_5_20_30
    seat.day_4_21_00 = seat.day_5_21_00
    seat.day_4_21_30 = seat.day_5_21_30
    seat.day_4_22_00 = seat.day_5_22_00
    seat.day_4_22_30 = seat.day_5_22_30
    seat.day_4_23_00 = seat.day_5_23_00
    seat.day_4_23_30 = seat.day_5_23_30

def clear_all_day5_record(seat):
    seat.day_5_00_00 = '0'
    seat.day_5_00_30 = '0'
    seat.day_5_01_00 = '0'
    seat.day_5_01_30 = '0'
    seat.day_5_02_00 = '0'
    seat.day_5_02_30 = '0'
    seat.day_5_03_00 = '0'
    seat.day_5_03_30 = '0'
    seat.day_5_04_00 = '0'
    seat.day_5_04_30 = '0'
    seat.day_5_05_00 = '0'
    seat.day_5_05_30 = '0'
    seat.day_5_06_00 = '0'
    seat.day_5_06_30 = '0'
    seat.day_5_07_00 = '0'
    seat.day_5_07_30 = '0'
    seat.day_5_08_00 = '0'
    seat.day_5_08_30 = '0'
    seat.day_5_17_00 = '0'
    seat.day_5_17_30 = '0'
    seat.day_5_18_00 = '0'
    seat.day_5_18_30 = '0'
    seat.day_5_19_00 = '0'
    seat.day_5_19_30 = '0'
    seat.day_5_20_00 = '0'
    seat.day_5_20_30 = '0'
    seat.day_5_21_00 = '0'
    seat.day_5_21_30 = '0'
    seat.day_5_22_00 = '0'
    seat.day_5_22_30 = '0'
    seat.day_5_23_00 = '0'
    seat.day_5_23_30 = '0'
            
def clear_all_day2_record(seat):
    seat.day_2_00_00 = '0'
    seat.day_2_00_30 = '0'
    seat.day_2_01_00 = '0'
    seat.day_2_01_30 = '0'
    seat.day_2_02_00 = '0'
    seat.day_2_02_30 = '0'
    seat.day_2_03_00 = '0'
    seat.day_2_03_30 = '0'
    seat.day_2_04_00 = '0'
    seat.day_2_04_30 = '0'
    seat.day_2_05_00 = '0'
    seat.day_2_05_30 = '0'
    seat.day_2_06_00 = '0'
    seat.day_2_06_30 = '0'
    seat.day_2_07_00 = '0'
    seat.day_2_07_30 = '0'
    seat.day_2_08_00 = '0'
    seat.day_2_08_30 = '0'
    seat.day_2_17_00 = '0'
    seat.day_2_17_30 = '0'
    seat.day_2_18_00 = '0'
    seat.day_2_18_30 = '0'
    seat.day_2_19_00 = '0'
    seat.day_2_19_30 = '0'
    seat.day_2_20_00 = '0'
    seat.day_2_20_30 = '0'
    seat.day_2_21_00 = '0'
    seat.day_2_21_30 = '0'
    seat.day_2_22_00 = '0'
    seat.day_2_22_30 = '0'
    seat.day_2_23_00 = '0'
    seat.day_2_23_30 = '0'

def clear_all_day3_record(seat):
    seat.day_3_00_00 = '0'
    seat.day_3_00_30 = '0'
    seat.day_3_01_00 = '0'
    seat.day_3_01_30 = '0'
    seat.day_3_02_00 = '0'
    seat.day_3_02_30 = '0'
    seat.day_3_03_00 = '0'
    seat.day_3_03_30 = '0'
    seat.day_3_04_00 = '0'
    seat.day_3_04_30 = '0'
    seat.day_3_05_00 = '0'
    seat.day_3_05_30 = '0'
    seat.day_3_06_00 = '0'
    seat.day_3_06_30 = '0'
    seat.day_3_07_00 = '0'
    seat.day_3_07_30 = '0'
    seat.day_3_08_00 = '0'
    seat.day_3_08_30 = '0'
    seat.day_3_17_00 = '0'
    seat.day_3_17_30 = '0'
    seat.day_3_18_00 = '0'
    seat.day_3_18_30 = '0'
    seat.day_3_19_00 = '0'
    seat.day_3_19_30 = '0'
    seat.day_3_20_00 = '0'
    seat.day_3_20_30 = '0'
    seat.day_3_21_00 = '0'
    seat.day_3_21_30 = '0'
    seat.day_3_22_00 = '0'
    seat.day_3_22_30 = '0'
    seat.day_3_23_00 = '0'
    seat.day_3_23_30 = '0'

def clear_all_day4_record(seat):
    seat.day_4_00_00 = '0'
    seat.day_4_00_30 = '0'
    seat.day_4_01_00 = '0'
    seat.day_4_01_30 = '0'
    seat.day_4_02_00 = '0'
    seat.day_4_02_30 = '0'
    seat.day_4_03_00 = '0'
    seat.day_4_03_30 = '0'
    seat.day_4_04_00 = '0'
    seat.day_4_04_30 = '0'
    seat.day_4_05_00 = '0'
    seat.day_4_05_30 = '0'
    seat.day_4_06_00 = '0'
    seat.day_4_06_30 = '0'
    seat.day_4_07_00 = '0'
    seat.day_4_07_30 = '0'
    seat.day_4_08_00 = '0'
    seat.day_4_08_30 = '0'
    seat.day_4_17_00 = '0'
    seat.day_4_17_30 = '0'
    seat.day_4_18_00 = '0'
    seat.day_4_18_30 = '0'
    seat.day_4_19_00 = '0'
    seat.day_4_19_30 = '0'
    seat.day_4_20_00 = '0'
    seat.day_4_20_30 = '0'
    seat.day_4_21_00 = '0'
    seat.day_4_21_30 = '0'
    seat.day_4_22_00 = '0'
    seat.day_4_22_30 = '0'
    seat.day_4_23_00 = '0'
    seat.day_4_23_30 = '0'