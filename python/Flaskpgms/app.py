from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")
@app.route('/home')
def home():
    return 'home page'

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact_us')
def contact_us():
    return render_template("contact_us.html")

@app.route('/send',methods=['POST','GET'])
def send():
    if (request.method=='POST'):
        getName=request.form['name']
        getemail=request.form['email']
        getmob=request.form['mobile_no']
        getsub=request.form['msg_subject']
        getcontent=request.form['msg_content']
        return render_template("result.html",passName=getName,passEmail=getemail)
        


if (__name__ == '__main__'):
   app.run(debug=True)