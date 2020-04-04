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

@app.route('/',methods=['GET','POST'])
def home():
    username_input = request.json['data']['username']
    password_input = request.json['data']['password']
    json_response = {}

    hash_obj = hashlib.md5(password_input.encode())
    md5_password = hash_obj.hexdigest()

    cur = mysql.connection.cursor()
    query = "SELECT username,password FROM `users` WHERE username='{}' AND password='{}'".format(username_input,md5_password)
    found = cur.execute(query)

    # found = 1 brarti ada username n pass di db 
    if found == 1:
        querygetdata = "SELECT foto_profil,nama,email,telepon,alamat,set_sumbangan,total_sumbangan FROM `users` WHERE username='{}' AND password='{}'".format(username_input,md5_password)
        cur.execute(querygetdata)
        row_headers=[x[0] for x in cur.description] #this will extract row headers
        rv = cur.fetchall()
        json_data=[]
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        json_response['data'] = json.loads(json.dumps(json_data[0]))
        json_response['code'] = 0
        json_response['message'] = 'success'
        return json_response
    json_response['data'] = ''
    json_response['code'] = 9999
    json_response['message'] = "failed"
    return json_response

if __name__ == '__main__':
    app.run(debug=True)