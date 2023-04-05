from flask import Flask,render_template,request
import datetime as dt
now=dt.datetime.now()
date=(str(now).split())[0]
app=Flask(__name__)

@app.route('/')
def hello_page():
    return render_template("index.html")

@app.route('/certificate',methods=['POST'])
def certificate():
    name=request.form["applicant_name"]
    organization=request.form['organization_name']
    signiture=request.form['signiture']
    return render_template("certificate.html",Date=date,certified_name=name,organization_name=organization,head_signiture=signiture)

if __name__=="__main__":
    app.run(debug=True,port=5000, host="0.0.0.0")
