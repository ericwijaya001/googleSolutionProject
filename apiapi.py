from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import json

# bbuat coba aja
datainput = {
        'username' : 'orang1',
        'password' : 'orang1'
        }


app = Flask(__name__,template_folder='template')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'userdb'

mysql = MySQL(app)

@app.route('/',methods=['GET','POST'])
def home():
    # usernameinput = request.json['username']
    # passwordinput = request.json['password']
    usernameinput = datainput['username']
    passwordinput = datainput['password']
    cur = mysql.connection.cursor()
    query = "SELECT username,password FROM `users` WHERE username='{}' AND password='{}'".format(usernameinput,passwordinput)
    adagak = cur.execute(query)
    # adagak = 1 brarti ada username n pass di db 
    if adagak == 1:
        querygetdata = "SELECT fotoprofil,nama,email,telepon,alamat,setsumbangan,totalsumbangan FROM `users` WHERE username='{}' AND password='{}'".format(usernameinput,passwordinput)
        cur.execute(querygetdata)
        row_headers=[x[0] for x in cur.description] #this will extract row headers
        rv = cur.fetchall()
        json_data=[]
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        return render_template('home.html', mbo=json.loads(json.dumps(json_data[0])))
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)