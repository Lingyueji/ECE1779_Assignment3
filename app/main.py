
from flask import render_template, url_for, redirect, request,session
from app import webapp
from app.jobDDB import query_jobs,query_skills
from app.candidateDDB import query_candidate_of_position
from app.createNewJob import createNJ


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

def displayPosition():#TODO: pass the managerid to this function
    ManagerID = "43601e88-f2ab-11e8-ba53-f40f242190e7"
    list = query_jobs(ManagerID)
    jobTitle = []
    managerID = []
    positionID = []
    for row in list:
        jobTitle.append(row['jobTitle'])
        managerID.append(row['managerID'])
        positionID.append(row['positionID'])

    return render_template("/main.html", positions=jobTitle, mID=managerID, pID=positionID, uName = session['uName'])


    # ManagerID = "43601e88-f2ab-11e8-ba53-f40f242190e7"
    # list = query_jobs(ManagerID)
    # jobTitle = []
    # managerID = []
    # positionID = []
    # for row in list:
    #     jobTitle.append(row['jobTitle'])
    #     managerID.append(row['managerID'])
    #     positionID.append(row['positionID'])
    # return render_template("/main.html",positions = jobTitle, mID = managerID, pID = positionID)


@webapp.route('/view/<mID>/<pID>', methods=['POST'])
def view(mID, pID):
    #list = [{'positionID': '7', 'resume': 'https://s3.amazonaws.com/a3-resume/lecture2_ewADCWQ.pdf', 'managerID': '43601e88-f2ab-11e8-ba53-f40f242190e7', 'candidateEmail': 'Tom@google.com', 'skills': {'php': '2', 'python': '1', 'java': '2', 'machine learning': '0'}, 'candidatePhone': '778234012'}]
    pID = "4220f558-f337-11e8-b8de-f40f242190e7"
    list = query_candidate_of_position(pID)
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
    mID = "43601e88-f2ab-11e8-ba53-f40f242190e7"
    pID = "4220f558-f337-11e8-b8de-f40f242190e7"
    return render_template("/upload.html", mID=mID, pID=pID)


@webapp.route('/add/<mID>', methods=['POST'])
def addNewPosition(mID):
    return render_template("add.html",mID=mID)

@webapp.route('/addnewJob', methods=['POST'])
def addNewJob():
    positionName = request.form['position']
    skills = request.form['skills']
    mid="43601e88-f2ab-11e8-ba53-f40f242190e7"
    createNJ(mid,positionName,skills)
    return redirect(url_for('displayPosition'))