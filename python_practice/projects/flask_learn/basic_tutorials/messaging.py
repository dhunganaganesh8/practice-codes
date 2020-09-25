from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('start_page.html')

@app.route('/first', methods=['POST', 'GET'])
def decision_first():
    if request.method == 'POST':
        return render_template('decision_first.html')
    else:
        return redirect('/')
