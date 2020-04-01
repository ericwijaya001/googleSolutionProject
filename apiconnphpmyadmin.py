from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__,template_folder='template')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskapp'

mysql = MySQL(app)

@app.route('/',methods=['GET','POST'])
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT name FROM `users` WHERE id < 3")
    # SELECT bla3 diatas buat ambil data apa
    fetchdata = cur.fetchall()
    cur.close()
    return render_template('home.html',mbo=fetchdata)
    # param 'mbo' diatas itu buat nampilin 
    # di home.htmlnya coba diliat di home.htmlnya

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == "POST":
        details = request.form
        nama = details['nama']
        email = details['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `users` VALUES (%s,%s, %s)", ('NULL',nama, email))
        mysql.connection.commit()
        cur.close()
        return 'asiap'
    return render_template('form.html')    

if __name__ == '__main__':
    app.run(debug=True)