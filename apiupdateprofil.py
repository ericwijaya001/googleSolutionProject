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
    photo = request.json['photo']
    name = request.json['name']
    email = request.json['email']
    telp = request.json['telp']
    address = request.json['address']

    cur = mysql.connection.cursor()
    query_get_data = "UPDATE `users` SET `photo` = '{}', `name` = '{}', `email` = '{}', `telp` = {}, `address` = '{}' WHERE `username` = '{}'".format(photo,name,email,telp,address,username)
    cur.execute(query_get_data)
    mysql.connection.commit()

    query_select_data = "SELECT photo,name,email,telp,address FROM `users` WHERE username='{}'".format(username)
    cur.execute(query_select_data)
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
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)