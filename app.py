from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Loan Calculator')

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        form = request.form
        A = float(form['loan'])
        p = float(form['payments'])
        y = float(form['years'])
        r = float(form['rate'])
        D = (((1+(r/p))**(p*y))-1)/((r/p)*(1+(r/p))**(p*y))
        calc = '${:,.2f}'.format(A/D)

        return render_template('index.html', display=calc, pageTitle='Loan Calculator')

    return redirect("/")


    if __name__ == '__main__':
        app.run(debug=True)
