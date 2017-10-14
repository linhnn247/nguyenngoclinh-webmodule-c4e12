from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/c4e12')
def c4e12():
    return "Hello c4e12"

@app.route('/tungmtp')
def tungmtp():
    return "Ta lac troi giua doi"

@app.route('/<int:a>/<int:b>')
def add(a,b):
    tong = a + b
    return str(tong)

@app.route('/h1')
def tagh1():
    return "<h1> Ta lạc trôi giữa đời </h1><p> aaa, teo teo teo teo teo</p><p> bbbb </p>"



if __name__ == '__main__':
  app.run(debug=True)
