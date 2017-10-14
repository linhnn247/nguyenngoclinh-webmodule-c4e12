from flask import Flask
from flask import Flask, render_template
from flask import Flask, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/school')
def direct():
    return redirect("http://techkids.vn/")

@app.route('/<tenfile>')
def demo(tenfile):
    return render_template( tenfile +'.html')

@app.route('/bmi/<w>/<h>')
def bmi(w, h):
    h1 = float (int(h)/100)
    bmi = int(w)/(h1*h1)
    if (bmi<16):
        ketqua = "You are severely underweight (còi xương)"
    elif (16 <= bmi <18.5):
        ketqua = "You are underweight (Thiếu cân)"
    elif (18.5<= bmi < 25):
        ketqua = "You are normal (Bình thường)"
    elif (25 <= bmi < 30):
        ketqua = "You are overweight (Thừa cân)"
    else:
        ketqua = "You are obese (Béo phì)"
    return "chỉ số bmi của bạn là: " + str(bmi) + "<br>" +  ketqua

if __name__ == '__main__':
  app.run(debug=True)
