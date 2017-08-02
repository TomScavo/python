from flask import Flask, redirect, render_template, request, session, url_for
import csv
app = Flask(__name__)

@app.route('/')
@app.route('/Index.html')
@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route('/Music.html')
def cs50():
    return render_template('Music.html')

@app.route("/Video.html")
def Video():
    return render_template('Video.html')

@app.route("/aboutZAYN.html")
@app.route("/AboutZAYN.html")
def AboutZAYN():
    return render_template("AboutZAYN.html")

@app.route("/Photos.html")
def Music():
    return render_template("Photos.html")

@app.route("/TRY.html")
def TRY():
    return render_template('TRY.html')

@app.route("/Taylor Swift.html")
def taylor():
    return render_template('Taylor Swift.html')

@app.route('/Taylor.mp4')
def Taylor_video():
    return app.send_static_file('TaylorSwiftLive2015.mp4')

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == 'POST':
        if request.form["name"]=='' or request.form["password"]=='' or len(request.form["password"])<6:
            return render_template("failure.html")
        with open('user.csv',newline='') as f:
            reader = csv.reader(f)
            s=''
            for row in reader:
                for c in row:
                    if c==",":
                        break
                    s='%s%s'%(s,c)
                if s==request.form["name"]:
                    return render_template("failure_logn.html")
        f.close()
    name=request.form["name"]
    password=request.form["password"]
    file =open("user.csv","a")
    writer=csv.writer(file)
    writer.writerow((name,password))
    file.close()
    return render_template("success.html")

@app.route("/Register.html")
def Register1():
    return render_template("Register.html")

@app.route('/LognIn.html')
def request_logn():
    return render_template('LognIn.html')

@app.route('/LognIn',methods=["GET","POST"])
def LognIn():
    if request.method=="POST":
        if request.form["name"]=="" or request.form["password"]=="" or len(request.form["password"])<6:
            return render_template("failure_logn.html")
        with open('user.csv',newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if row==[request.form["name"], request.form["password"]]:
                    return render_template("107.html")

    return render_template("failure_logn.html")
if __name__=='__main__':
    app.run(host="192.168.191.1",port=80)


