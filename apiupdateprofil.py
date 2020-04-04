from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import json
import hashlib

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'userdb'

mysql = MySQL(app)
json_response = {}

@app.route('/',methods=['GET','POST'])
def home():
    username_input = request.json['data']['username']
    foto_profil = request.json['data']['foto_profil']
    nama = request.json['data']['nama']
    email = request.json['data']['email']
    telepon = request.json['data']['telepon']
    alamat = request.json['data']['alamat']

    cur = mysql.connection.cursor()
    query = "SELECT username FROM `users` WHERE username='{}' ".format(username_input)
    query_executed = cur.execute(query)

    # == 1 >> kalo usernamenya ditemukan di db
    if query_executed == 1:
        query_get_data = "UPDATE `users` SET `foto_profil` = '{}', `nama` = '{}', `email` = '{}', `telepon` = {}, `alamat` = '{}' WHERE `username` = '{}'".format(foto_profil,nama,email,telepon,alamat,username_input)
        cur.execute(query_get_data)
        mysql.connection.commit()
        query_select_data = "SELECT foto_profil,nama,email,telepon,alamat FROM `users` WHERE username='{}'".format(username_input)
        cur.execute(query_select_data)
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
    json_response['data'] = ''
    json_response['code'] = 9999
    json_response['message'] = 'failed'
    cur.close()
    return json_response
    

if __name__ == '__main__':
    app.run(debug=True)