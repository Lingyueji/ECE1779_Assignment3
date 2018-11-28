from flask import render_template, url_for, redirect, request,session
from app import webapp

webapp.secret_key = '\x80\xa9s*\x12\xc7x\xa9d\x1f(\x03\xbeHJ:\x9f\xf0!\xb1a\xaa\x0f\xee'
@webapp.route('/login',methods=['POST','GET'])
@webapp.route('/',methods=['POST','GET'])
def login():
    return render_template("login.html")

@webapp.route('/logout',methods=['POST'])
def logout():
    session.pop('uName', None)
    return render_template("login.html")

@webapp.route('/login_submit',methods=['POST'])
def loginsubmit():
    if request.form['username'] != '' and request.form['password'] != '':
        uName = request.form['username']
        uPass = request.form['password']
        #Temporarily hard code.
        if uName == 'admin' and uPass == 'admin':
            session['uName'] = uName
            return displayPosition()
        return render_template("login.html", err='Username and password doesn not match!')
    return render_template("login.html",err='Please provide username and password!')

@webapp.route('/main_page',methods=['POST'])
def displayPosition():
    list = [{'jobTitle': 'C++ developer', 'positionID': 'jjjjjj',
             'managerID': '1082dd38-f284-11e8-8aeb-f40f242190e7'},
            {'jobTitle': 'math tutor', 'positionID': 'sadwaere',
             'managerID': '1082dd38-f284-11e8-8aeb-f40f242190e7'},
            {'jobTitle': 'junior java developer', 'positionID': 'sajijiwe',
             'managerID': '1082dd38-f284-11e8-8aeb-f40f242190e7'}]
    jobTitle = []
    managerID = []
    positionID = []
    for row in list:
        jobTitle.append(row['jobTitle'])
        managerID.append(row['managerID'])
        positionID.append(row['positionID'])
    return render_template("/main.html", positions=jobTitle, mID=managerID, pID=positionID, uName=session['uName'])


@webapp.route('/view/<mID>/<pID>', methods=['POST'])
def view(mID, pID):
    list = [{'positionID': 'be9aa298-f2c2-11e8-a4d7-f40f242190e7', 'resume': 'https://s3.amazonaws.com/resume-bucket-a3/JiayiZhao Resume .pdf', 'candidateEmail': 'jiay.zhao@mail.utoronto.ca', 'skills': {'Agile': '0', 'java': '2', 'MySQL': '2'}, 'candidatePhone': '6476710301', 'candidateID': '74f92f06-f2ca-11e8-967b-f40f242190e7'}, {'positionID': 'be9aa298-f2c2-11e8-a4d7-f40f242190e7', 'resume': 'https://s3.amazonaws.com/resume-bucket-a3/JiayiZhao Resume .pdf', 'candidateEmail': 'jiay.zhao@mail.utoronto.ca', 'skills': {'Agile': '0', 'java': '2', 'MySQL': '2'}, 'candidatePhone': '6476710301', 'candidateID': '212ac87e-f2d1-11e8-abb8-f40f242190e7'}, {'positionID': 'be9aa298-f2c2-11e8-a4d7-f40f242190e7', 'resume': 'https://s3.amazonaws.com/resume-bucket-a3/JiayiZhao Resume .pdf', 'candidateEmail': 'jiay.zhao@mail.utoronto.ca', 'skills': {'Agile': '0', 'java': '2', 'MySQL': '2'}, 'candidatePhone': '6476710301', 'candidateID': '06b344ba-f2d1-11e8-90c0-f40f242190e7'}, {'positionID': 'be9aa298-f2c2-11e8-a4d7-f40f242190e7', 'resume': 'https://s3.amazonaws.com/resume-bucket-a3/JiayiZhao Resume .pdf', 'candidateEmail': 'jiay.zhao@mail.utoronto.ca', 'skills': {'Agile': '0', 'java': '2', 'MySQL': '2'}, 'candidatePhone': '6476710301', 'candidateID': 'bbc3721a-f2d0-11e8-9a0a-f40f242190e7'}]
    skill_freq = []
    emails = []
    phones = []
    resumes = []
    for row in list:
        skill_freq.append(row['skills'])
        emails.append(row['candidateEmail'])
        phones.append(row['candidatePhone'])
        resumes.append(row['resume'])
    print(emails)
    return render_template("/view.html", skill_freq=skill_freq, emails=emails, mID=mID, pID=pID, phones=phones,resumes=resumes)

@webapp.route('/upload/<mID>/<pID>', methods=['POST'])
def directToUpload(mID, pID):
    return render_template("/upload.html", mID=mID, pID=pID)

@webapp.route('/add/<mID>', methods=['POST'])
def addNewPosition(mID):
    return render_template("add.html",mID=mID)