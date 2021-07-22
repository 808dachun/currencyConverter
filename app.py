# https://forex-python.readthedocs.io/en/latest/usage.html
from flask import Flask, request, render_template
from random import randint
from forex_python.converter import CurrencyRates
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

c = CurrencyRates()

app.config['SECRET KEY'] = "123456"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """Show Home Page"""
    html = """
    <html>
        <body>
            <h1> Home Page </h1>
            <p> Hello welcome to my currency converter!</p>
            <a href='/go_convert'> Go to convert page</a>
        </body>
    </html>
    """
    return html


@app.route('/go_convert')
def show_form():
    return render_template("convert.html")


@app.route('/final')
def final():
    from_c = request.args["convert_from"]
    to_c = request.args["convert_to"]
    amount = request.args["amount"]
    final = c.convert(from_c , to_c, float(amount)) 
    return render_template("final.html", final = final)
    
    
