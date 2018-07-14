from flask import Flask, render_template, json, request
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/showSearch')
def showSignUp():
    return render_template('signUp.html')


@app.route('/search',methods=['POST'])
def signUp():
    keyword = request.form['inputName']
    return json.dumps({'keyword':keyword})

if __name__ == "__main__":
    app.run(port=5002, debug=True)
