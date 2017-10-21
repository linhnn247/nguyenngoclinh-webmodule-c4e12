from flask import Flask, render_template
import mlab
from mongoengine import *
from faker import Faker

app = Flask(__name__)

mlab.connect()

class Girl(Document):
    name = StringField()
    image = StringField()
    description = StringField()
    rating = FloatField()

f = Faker()

#for i in range(5):
    #g = Girl(name = f.name(),
            #image = 'https://source.unsplash.com/500x300/?girl',
            #description = f.text(),
            #rating = 4.1)
    #g.save()

@app.route('/girl')
def index1():
    girllist = Girl.objects()
    return render_template('girls.html', girls = girllist)

@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/list')
def listdemo():
    nlist = ['huy','tuan anh','linh','truong','quan','nhung nguoi ban']
    return render_template("girlslist.html", names = nlist)

@app.route('/dict')
def dictdemo():
    d = {
        'name':'Xưa và nay',
        'image':'http://www.tieuthien.com/wp-content/uploads/2016/10/hot-girl-gai-xinh-facebook-tieuthien.com-5.jpg'
    }

    return render_template('girldict.html',girl = d)

@app.route('/css-demo')
def cssdemo():
    return render_template('cssdemo.html')



if __name__ == '__main__':
  app.run(debug=True)
