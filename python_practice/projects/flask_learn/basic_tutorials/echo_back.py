from flask import Flask, request

app = Flask(import_name=__name__)

@app.route('/hello')
def echo():

    to_echo = request.args.get("gd", "")
    response = "{}".format(to_echo)

    return response

if __name__ == "__main__":
    app.run(debug=True)
