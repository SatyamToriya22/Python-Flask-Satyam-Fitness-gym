from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/gym_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
db=SQLAlchemy(app)


class joiningform_tb(db.Model):

    snum=db.Column(db.Integer ,primary_key=True)
    name=db.Column(db.String(30) ,unique=False,nullable=True)
    age=db.Column(db.String(10) ,nullable=True)
    gender=db.Column(db.String(10) ,nullable=True)
    locality=db.Column(db.String(30) ,nullable=True)
    contact=db.Column(db.String(13) ,unique=True)

class contactus_tb(db.Model):

    snum=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),unique=False,nullable=True)
    email=db.Column(db.String(30),unique=True,nullable=True)
    message=db.Column(db.String(120),nullable=True)
    
@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/joinUs', methods=['GET','POST'])
def join_form():

    if request.method=='POST':

        name=request.form.get('name')
        age=request.form.get('age')
        gender=request.form.get('gender')
        locality=request.form.get('locality')
        contact_num=request.form.get('contact')

        entry=joiningform_tb(name=name,age=age,gender=gender,locality=locality,contact=contact_num)

        db.session.add(entry)
        db.session.commit()
    if request.method == "POST":
        name=request.form.get('name')
        if name!="":
            return render_template('submitted.html')
    return render_template('joining_form.html')

@app.route('/aboutUs')
def aboutUs():
    return render_template('aboutus.html')

@app.route('/gallery')
def gallery():
    imgs=['img/im1.jpg','img/im2.jpg','img/im3.jpg','img/im4.jpg','img/im5.jpg','img/im6.jpg','img/im7.jpg','img/im8.jpg','img/im9.jpg','img/im10.jpg','img/im11.jpg','img/im12.jpg','img/im13.jpg','img/im14.jpg','img/im15.jpg','img/im16.jpg','img/im17.jpg','img/im18.jpg','img/im19.jpg','img/im20.jpg','img/im21.jpg','img/im22.jpg','img/im23.jpg','img/im24.jpg']
    return render_template('gallery.html',imgs=imgs)

@app.route('/contactUs', methods=["GET","POST"])
def contactUs():
    if request.method=="POST":
        name=request.form.get('name')
        email=request.form.get('email')
        message=request.form.get('message')

        entry=contactus_tb(name=name,email=email,message=message)

        db.session.add(entry)
        db.session.commit()
    if request.method == "POST":
        name=request.form.get('name')
        if name!="":
            return render_template('request_submit.html')
    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True)