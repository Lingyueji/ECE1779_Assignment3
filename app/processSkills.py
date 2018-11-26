from flask import render_template, request
from app import webapp

@webapp.route('/skill_match',methods=['POST'])
def check():
    if request.form['desired']:
        desiredSkills = request.form['desired'].lower().split(',')

        resume = "JavaC_+d=".lower() #TODO change to resume = convertPDFtoString() after implementing convertPDFtoString()
        res = {}
        for keyword in desiredSkills:
            if keyword in resume:
                res[keyword] = True
                continue
            res[keyword] = False
        return render_template("/skillMatch.html", desired = desiredSkills, match = res)

#TODO download pdf from s3, convert it to string
def convertPDFtoString():
    #TODO: download pdf from s3, convert it to string
    return str

