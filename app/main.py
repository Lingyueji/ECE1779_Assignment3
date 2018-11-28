from flask import render_template, url_for, redirect
from app import webapp

@webapp.route('/',methods=['GET','POST'])
@webapp.route('/index',methods=['GET','POST'])
@webapp.route('/welcome',methods=['GET','POST'])
def displayPosition():
    list = [{'jobTitle': 'C++ developer', 'positionID': 'jjjjjj', 'managerID': '1082dd38-f284-11e8-8aeb-f40f242190e7'},
            {'jobTitle': 'math tutor', 'positionID': 'sadwaere', 'managerID': '1082dd38-f284-11e8-8aeb-f40f242190e7'},
            {'jobTitle': 'junior java developer', 'positionID': 'sajijiwe', 'managerID': '1082dd38-f284-11e8-8aeb-f40f242190e7'}]
    jobTitle = []
    managerID = []
    positionID = []
    for row in list:
        jobTitle.append(row['jobTitle'])
        managerID.append(row['managerID'])
        positionID.append(row['positionID'])
    return render_template("/main.html",positions = jobTitle, mID = managerID, pID = positionID)


@webapp.route('/view/<mID>/<pID>', methods=['POST'])
def view(mID, pID):
    list = [{'positionID': '7', 'resume': 'https://s3.amazonaws.com/a3-resume/lecture2_ewADCWQ.pdf', 'managerID': '43601e88-f2ab-11e8-ba53-f40f242190e7', 'candidateEmail': 'Tom@google.com', 'skills': {'php': '2', 'python': '1', 'java': '2', 'machine learning': '0'}, 'candidatePhone': '778234012'}]
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