import os
from flask import Flask, flash, request, redirect, url_for
app = Flask(__name__)
from werkzeug.utils import secure_filename

from deep_lip_reading.main import main

UPLOAD_FOLDER = '/Users/LucyWang/MLRelated/dubhacks/deep_lip_reading/media/example'
ALLOWED_EXTENSIONS = set(['mp4'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # call deep lip reading, and get the returned file
            f= open("/Users/LucyWang/MLRelated/dubhacks/deep_lip_reading/demofile3.txt","r")
            l = f.readline()
            return l
    return '''