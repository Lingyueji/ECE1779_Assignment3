from flask import render_template, request, redirect,url_for
from app import webapp
import os
from app.S3UploadDownload import s3_upload

bucketName = "resume-bucket-a3"



@webapp.route('/upload_submit/<mID>/<pID>',methods=['POST'])
def upload_submit(mID, pID):
    file = request.files['resume']
    filepath = os.path.join('static',file.filename)
    file.save(filepath)
    s3_upload(filepath, bucketName, file.filename)
    return redirect(url_for('displayPosition'))


