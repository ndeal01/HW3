from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='My Calculator')

@app.route('/nick')
def nick():
    return render_template('nick.html', pageTitle='About Nick')

    if __name__ == '__main__':
        app.run(debug=True)
