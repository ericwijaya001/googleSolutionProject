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
    username = request.json['username']
    password = request.json['password']
    photo = request.json['photo']
    name = request.json['name']
    email = request.json['email']
    telp = request.json['telp']
    anonymous = request.json['anonymous']

    # md5
    hash_obj = hashlib.md5(password.encode())
    md5_password = hash_obj.hexdigest()

    cur = mysql.connection.cursor()
    query = "INSERT INTO `users` (`id`, `username`, `password`, `photo`, `name`, `email`, `telp`, `anonymous`) VALUES (NULL, '{}', '{}', '{}', '{}', '{}', {}, {});".format(username,md5_password,photo,name,email,telp,anonymous)
    query_executed = cur.execute(query)

    if query_executed == 1:
        mysql.connection.commit()
        query_get_data = "SELECT `id`, `username`, `password`, `photo`, `name`, `email`, `telp`, `anonymous` FROM `users` WHERE username='{}' AND password='{}'".format(username,md5_password)
        cur.execute(query_get_data)
        row_headers=[x[0] for x in cur.description] #this will extract row headers
        rv = cur.fetchall()
        json_data=[]
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        json_response = json.loads(json.dumps(json_data[0]))
        json_response['code'] = 0
        json_response['message'] = 'success'
        cur.close()
        return json_response
    json_response = json.loads(json.dumps(json_data[0]))
    json_response['code'] = 9999
    json_response['message'] = 'failed'
    cur.close()
    return json_response
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
