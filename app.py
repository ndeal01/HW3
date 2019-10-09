from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Loan Calculator')

@app.route('/payment', methods=['GET', 'POST'])
def calculation():
    if request.method == 'POST':
        form = request.form
        A = int(form['A'])
        p = int(form['p'])
        y = int(form['y'])
        r = int(form['r'])
        f = int(form['f'])
        Discount = (((1+(r/f))^(p*y))-1)/((r/f)(1+(r/f)^(p*y)))
        calc = A/Discount
        return render_template('index.html', display=calc, pageTitle='Loan Calculator')

    return redirect("/")


    if __name__ == '__main__':
        app.run(debug=True)
