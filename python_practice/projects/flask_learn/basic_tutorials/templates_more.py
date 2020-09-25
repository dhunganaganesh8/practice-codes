from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/hello/<int:score>')
def hello_name(score):
    return render_template('hello_more.html', marks=score)

@app.route('/result', methods=['POST', 'GET'])
def result_check():
    if request.method == 'POST':
        marks = request.form.get("input")
        return redirect(url_for('hello_name', score=int(marks)))
    else:
        marks = request.args.get("marks")
        return redirect(url_for('hello_name', score=int(marks)))


if __name__ == "__main__":
    app.run(debug=True)
