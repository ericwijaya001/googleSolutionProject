from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import json
import hashlib

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'regisdb'

data = {
    'data' : {
        'username' : 'mbo',
        'password' : 'mbo',
        'is_login' : 0,
        'foto_profil' : 'mbo.jpg',
        'nama' : 'namae_mbo',
        'email' : 'mbo@gmmail.com',
        'telepon' : 12345678,
        'level_member' : 0
    }
}

mysql = MySQL(app)
json_response = {}

@app.route('/',methods=['GET','POST'])
def home():
    # username_input = request.json['data']['username']
    # password_input = request.json['data']['password']
    # is_login = request.json['data']['is_login']
    # foto_profil = request.json['data']['foto_profil']
    # nama = request.json['data']['nama']
    # email = request.json['data']['email']
    # telepon = request.json['data']['telepon']
    # level_member = request.json['data']['level_member']

    username_input = data['data']['username']
    password_input = data['data']['password']
    is_login = data['data']['is_login']
    foto_profil = data['data']['foto_profil']
    nama = data['data']['nama']
    email = data['data']['email']
    telepon = data['data']['telepon']
    level_member = data['data']['level_member']

    # md5
    hash_obj = hashlib.md5(password_input.encode())
    md5_password = hash_obj.hexdigest()

    cur = mysql.connection.cursor()
    query = "INSERT INTO `regis` (`id`, `username`, `password`, `is_login`, `foto_profil`, `nama`, `email`, `telepon`, `level_member`) VALUES (NULL, '{}', '{}', {}, '{}', '{}', '{}', {}, {});".format(username_input,md5_password,is_login,foto_profil,nama,email,telepon,level_member)
    query_executed = cur.execute(query)

    if query_executed == 1:
        mysql.connection.commit()
        query_get_data = "SELECT `id`, `username`, `password`, `is_login`, `foto_profil`, `nama`, `email`, `telepon`, `level_member` FROM `regis` WHERE username='{}' AND password='{}'".format(username_input,md5_password)
        cur.execute(query_get_data)
        row_headers=[x[0] for x in cur.description] #this will extract row headers
        rv = cur.fetchall()
        json_data=[]
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        json_response['data'] = json.loads(json.dumps(json_data[0]))
        json_response['code'] = 0
        json_response['message'] = 'success'
        cur.close()
        return json_response
    json_response['data'] = json.loads(json.dumps(json_data[0]))
    json_response['code'] = 9999
    json_response['message'] = 'failed'
    cur.close()
    return json_response
    

if __name__ == '__main__':
    app.run(debug=True)