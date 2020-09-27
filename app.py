from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:root@127.0.0.1/height'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://ldklajzppxolzg:32816290376100e5df90d2c0d21891f6caf780ba711a7774390c4ce65688d98d@ec2-100-25-100-81.compute-1.amazonaws.com:5432/de4v03a0r24pk?sslmode=require'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)

    def __init__(self, email_,height_):
        self.email_=email_
        self.height_=height_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form["height_name"]
        
        if db.session.query(Data).filter(Data.email_==email).count() == 0:
            data=Data(email,height)
            db.session.add(data)
            db.session.commit()
            avg_height=round(db.session.query(func.avg(Data.height_)).scalar(),1)
            count=db.session.query(Data.height_).count()
            send_email(email, height, avg_height, count)
            return render_template("success.html")
    return render_template('index.html', text=" Mail ID already used !")


if __name__=='__main__':
    app.debg=True
    app.run()