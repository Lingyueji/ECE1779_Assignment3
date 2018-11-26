from flask import render_template, request, flash
from app import webapp
import os
from app.S3UploadDownload import s3_upload

bucketName = "a3-resume"

@webapp.route('/',methods=['GET'])
@webapp.route('/index',methods=['GET'])
@webapp.route('/upload',methods=['GET'])
def upload():
    return render_template("/upload.html")

@webapp.route('/skill_check',methods=['POST'])
def upload_and_skill_check():
    if not request.files:
        return render_template("/upload.html", error = "Please select a file!")
    file = request.files['resume']
    filepath = os.path.join('static', file.filename)
    print(filepath)
    file.save(filepath)
    msg = s3_upload(filepath, bucketName, file.filename)
    print(msg)
    return render_template("/skillCheck.html")


