from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def aboutus():
    return render_template('aboutus.html')


@app.route('/contact')
def contactus():
    return render_template('contactus.html')


@app.route('/register')
def registration():
    return render_template('registration.html')


@app.route('/success', methods=['post'])
def success():
    return render_template('success.html')

@app.route('/square')
def square():
    return render_template('square.html')

@app.route('/resultsq', methods=['post'])
def resultsq():
    n = int(request.form['txtNumber'])
    z= n*n
    return "<h1>Square is : " +str(z)

@app.route('/add')
def add():
    return render_template('addition.html')

@app.route('/resultadd', methods=['post'])
def resultadd():
    n = int(request.form['txtNumber'])
    m = int(request.form['txtNumber1'])
    z= n+m
    return "<h1>Addition is : " +str(z)

@app.route('/sub')
def subtract():
    return render_template('subtraction.html')

@app.route('/resultsub', methods=['post'])
def resultsub():
    n = int(request.form['txtNumber'])
    m = int(request.form['txtNumber1'])
    z= n-m
    return "<h1>Subtraction is : " +str(z)

@app.route('/mul')
def multiply():
    return render_template('multiplication.html')

@app.route('/resultmul', methods=['post'])
def resultmul():
    n = int(request.form['txtNumber'])
    m = int(request.form['txtNumber1'])
    z= n*m
    return "<h1>Multiplication is : " +str(z)




app.run(debug=True, host='0.0.0.0')
