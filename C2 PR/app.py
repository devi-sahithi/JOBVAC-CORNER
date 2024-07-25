import mimetypes
from flask import Flask, redirect,render_template,request,flash, url_for
from flask_mysqldb import MySQL
from flask_mail import Mail,Message
from datetime import date
import os
from werkzeug.utils import secure_filename


app=Flask(__name__)
app.config['SECRET_KEY'] = 'secret' 


app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '7951'
app.config['MYSQL_DB'] = 'jobvac_db'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)



app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'karumanchi.saimurari@gmail.com'
app.config['MAIL_PASSWORD'] = 'dewayonsdictoajz'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail=Mail(app)


UPLOAD_FOLDER = os.path.join(app.root_path, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def send_mail(name,receiver,messagess,file_path):
                    
                    msg = Message(subject='Applying for a job!', sender='karumanchi.saimurari@gmail.com', recipients=[receiver])
                    msg.body = messagess
                    with open(file_path, 'rb') as fp:
                        msg.attach(os.path.basename(file_path), 'application/pdf', fp.read())
                    mail.send(msg)
    
@app.route("/")
def index():
    return render_template("index.html")

def get_details():
    cur = mysql.connection.cursor()
    cur.execute(''' call all_jobs''')
    rec = cur.fetchall()
    print(rec)
    cur.close()

    return rec
@app.route("/browse")
def browse():
    
    jobs=get_details()
    
    return render_template("browse.html",jobs=jobs)

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/apply_job")
def apply_job():
    return render_template("apply.html")

@app.route("/user_login")
def user_login():
    return render_template("userlogin.html  ")

@app.route("/user_signup")
def user_signup():
    return render_template("user_signup.html")

@app.route("/rec_login")
def reclogin():
    return render_template("reclogin.html")

@app.route("/post_job")
def post():
    return render_template("reclogin.html")

@app.route("/r_signup")
def r_signup():
    return render_template("rec_signup.html")
    
@app.route("/rec_signup",methods=['GET', 'POST'])
def add_rec():
    if request.method == 'POST':
        id=request.form.get("cid")
        cname=request.form.get("company")
        recname=request.form.get("fullname")
        mob=request.form.get("phone")
        mail=request.form.get("email")
        psd=request.form.get("password")
        try:
            cur = mysql.connection.cursor()
            cur.callproc('add_recruiter',(id,cname,recname,mob,mail,psd))
            mysql.connection.commit()
            return "added succesfully"
            
    
        except mysql.connection.Error as err:
            return f"Error: {err}" 
        
@app.route("/login_rec",methods=['GET','POST'])
def login_rec():
    if request.method == 'POST':
        mail=request.form.get("un")
        psd=request.form.get("password")
        try:
            cur = mysql.connection.cursor()
            cur.execute('''call all_recruiter''')
            rec_det = cur.fetchall()
            for i in rec_det:
                if(i['rec_mail']==mail and i['rec_password']==psd):
                    global com
                    com=i['company_name']
                    return render_template("post.html")
                    #send_mail()
                    #return "posted Succesfully!"
            return 'Login Failed'
            
    
        except mysql.connection.Error as err:
            return f"Error: {err}" 
    
@app.route("/job_post",methods=['POST','GET'])
def job_post():
    if request.method=='POST':
        jid=int(request.form.get("id"))
        jtitle=request.form.get("title")
        jloc=request.form.get("loc")
        jdes=request.form.get("desc")
        jsal=request.form.get("sal")
        jqual=request.form.get("qua")
        today=date.today()
        rec_id=request.form.get("rec_id")
        try:
            cur = mysql.connection.cursor()
            cur.callproc('add_job',(jid,jtitle,com,jdes,jsal,today,jloc,jqual,rec_id))
            mysql.connection.commit()
            return "posted succesfully"
            
    
        except mysql.connection.Error as err:
            return f"Error: {err}" 
            

#upload_folder = os.path.join(os.getcwd(), 'uploads')  # Get the full path to the "uploads" directory


@app.route("/send",methods=['POST','GET'])
def send():
    if request.method=='POST':
        id=int(request.form.get("jid"))
        name=request.form.get("fn")
        mail=request.form.get("email")
        num=request.form.get("phon")
        print(request.files)
        
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file=request.files["file"]
        print(file)
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        msgs=request.form.get("coverletter")
        try:
            
            cur = mysql.connection.cursor()
            r_mail=cur.callproc('rec_email',[id])
            r=cur.fetchall()
            r1=list(r)
            print(r1)
            r2=r1[0]['rec_mail']
        except mysql.connection.Error as err:
            return f"Error: {err}"
        if file:
            
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            send_mail(name,r2,msgs,file_path);
            flash('File sent successfully','success')
            
            return "Applied Succesfully"
            
            
            
            
            
            ''' 
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            send_mail(name,r2,msg,file_path);
            flash('File sent successfully')
            return "Application sent succesfully"  
        
          '''
         
        
        

if __name__=='__main__':
    app.run(debug=True)