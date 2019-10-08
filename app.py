from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/nick')
def nick():
    return "hello Nick!"

    if __name__ == '__main__':
        app.run(debug=True)
