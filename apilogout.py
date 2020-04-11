from flask import Flask, request
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
    cur = mysql.connection.cursor()
    query = "SELECT username FROM `users` WHERE username ='{}'".format(username)
    query_executed = cur.execute(query)

    if query_executed == 1:
        query_get_data = "UPDATE `users` SET `isLogin` = '0' WHERE `username` = '{}';".format(username)
        cur.execute(query_get_data)
        mysql.connection.commit()
        json_response['code'] = 0
        json_response['message'] = 'success'
        cur.close()
        return json_response
    json_response['code'] = 9999
    json_response['message'] = 'failed'
    cur.close()
    return json_response
    

if __name__ == '__main__':
    app.run(debug=True)