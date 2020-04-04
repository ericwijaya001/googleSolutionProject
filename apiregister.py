from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import json
import hashlib

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'regisdb'

mysql = MySQL(app)
json_response = {}

@app.route('/',methods=['GET','POST'])
def home():
    username_input = request.json['data']['username']
    password_input = request.json['data']['password']
    is_login = request.json['data']['is_login']
    foto_profil = request.json['data']['foto_profil']
    nama = request.json['data']['nama']
    email = request.json['data']['email']
    telepon = request.json['data']['telepon']
    level_member = request.json['data']['level_member']

    # md5
    hash_obj = hashlib.md5(password_input.encode())
    md5_password = hash_obj.hexdigest()

    cur = mysql.connection.cursor()
    query = "INSERT INTO `regis` (`id`, `username`, `password`, `is_login`, `foto_profil`, `nama`, `email`, `telepon`, `level_member`) VALUES (NULL, '{}', '{}', {}, '{}', '{}', '{}', {}, {});".format(username_input,md5_password,is_login,foto_profil,nama,email,telepon,level_member)
    cur.execute(query)
    mysql.connection.commit()
    cur.close()
    
    json_response['code'] = 0
    json_response['message'] = 'success'
    return json_response

if __name__ == '__main__':
    app.run(debug=True)