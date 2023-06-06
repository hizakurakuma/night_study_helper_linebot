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


with app.app_context():
    df = pandas.read_excel('user_init.xlsx')
    user_list = df.values.tolist()
    for i in range(len(user_list)):
        user = User(str(user_list[i][1]),str(user_list[i][2]),str(user_list[i][3]),str(user_list[i][4]),int(user_list[i][5]),bool(user_list[i][6]))
        db.session.add(user)
        db.session.commit()
        #print(user_list[i][0],user_list[i][1],user_list[i][2],user_list[i][3],user_list[i][4],user_list[i][5],bool(user_list[i][6]))
        #print('success')