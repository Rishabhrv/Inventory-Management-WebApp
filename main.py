from flask import Flask, render_template,request,url_for
import mysql.connector

app = Flask(__name__)

con = mysql.connector.connect(host='localhost', user='root', password='', database='inventory')
cur = con.cursor()


@app.route('/')
def home():
    cur.execute("SELECT * FROM data")
    data = cur.fetchall()
    print(data[-1])
    return render_template('index.html', units = data[-1])

@app.route('/update')
def update():

    cur.execute("SELECT * FROM data")
    data = cur.fetchall()

    return render_template('update.html', units = data[-1])

@app.route('/login')
def login():

    return render_template('login.html')

@app.route('/fetch',methods = ['POST'])
def fetch():
    book1 = request.form.get('book1')
    book2 = request.form.get('book2')
    book3 = request.form.get('book3')
    oders = request.form.get('oders')
    pending = request.form.get('pending')
    complete = request.form.get('complete')
    print = request.form.get('print')
    production = request.form.get('production')
    ready = request.form.get('ready')


    cur.execute("""INSERT INTO `data` (`book1`, `book2`, `book3`, `oders`, `oder pending`, `complete oders`, `books in printing`, `books in production`, `books ready`) VALUES ({}, {},{},{},{},{},{},{},{});""".format(book1,book2,book3,oders,pending,complete,print,production,ready))
    con.commit()
    cur.execute("SELECT * FROM data")
    data = cur.fetchall()

    return render_template('index.html', units = data[-1])

@app.route('/validation',methods = ['POST'])
def val():
    email = request.form.get('email')
    passw = request.form.get('password')

    cur.execute("SELECT * FROM data")
    data = cur.fetchall()

    try:
        cur.execute("""INSERT INTO `user` (`user id`,`email`,`password`) VALUES (NULL,{},{});""".format(email,passw))
        con.commit()
    except:
        return render_template('update.html', units = data[-1])

    return render_template('update.html', units = data[-1])

if __name__=='__main__':
    app.run(debug = True)