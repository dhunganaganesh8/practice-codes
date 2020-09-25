from flask import Flask, render_template, request, redirect, url_for
#from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('upload_files'))

@app.route('/upload')
def upload_files():
    return render_template('upload.html')

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('gd')
        return 'file uploaded successfully'

if __name__ == "__main__":
    app.run(debug=True)
