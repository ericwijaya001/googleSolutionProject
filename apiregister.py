from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import json

# buat coba aja
datainput = {
        'username' : 'orginput1',
        'password' : 'orginput1',
        'is_login': '0', 
        'fotoprofil' : 'orginput1.jpg',
        'nama' : 'namaorginput1', 
        'email' : 'orginput1@gmail.com', 
        'telepon' : '0123456789',
        'levelmember' : '0'
        }

app = Flask(__name__,template_folder='template')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'regisdb'

mysql = MySQL(app)

@app.route('/',methods=['GET','POST'])
def home():
    # username_input = request.json['username']
    # password_input = request.json['password']
    # is_login = request.json['is_login']
    # fotoprofil = request.json['fotoprofil']
    # nama = request.json['nama']
    # email = request.json['email']
    # telepon = request.json['telepon']
    # levelmember = request.json['levelmember']

    username_input = datainput['username']
    password_input = datainput['password']
    is_login = datainput['is_login']
    fotoprofil = datainput['fotoprofil']
    nama = datainput['nama']
    email = datainput['email']
    telepon = datainput['telepon']
    levelmember = datainput['levelmember']

    cur = mysql.connection.cursor()
    query = "INSERT INTO `regis` (`id`, `username`, `password`, `is_login`, `fotoprofil`, `nama`, `email`, `telepon`, `levelmember`) VALUES ('2', '{}', '{}', {}, '{}', '{}', '{}', {}, {});".format(username_input,password_input,is_login,fotoprofil,nama,email,telepon,levelmember)
    cur.execute(query)
    mysql.connection.commit()
    cur.close()
    return render_template('home.html',mbo='NTAP')

if __name__ == '__main__':
    app.run(debug=True)