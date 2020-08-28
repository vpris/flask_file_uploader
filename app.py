import os
from flask import Flask, request, render_template, url_for, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './upload'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4'])

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/uploads', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        myfile = request.files['myfile']
        if myfile and allowed_file(myfile.filename):
            filename = secure_filename(myfile.filename)
            print(filename)
            myfile.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template("upload.html")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER,
                               filename)


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1')
