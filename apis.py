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

@app.route('/apilogin',methods=['GET','POST'])
def apilogin():
    json_response = {}

    username = request.json['username']
    password = request.json['password']

    hash_obj = hashlib.md5(password.encode())
    md5_password = hash_obj.hexdigest()

    cur = mysql.connection.cursor()
    query = "SELECT username,password FROM `users` WHERE username='{}' AND password='{}'".format(username,md5_password)
    found = cur.execute(query)

    # found = 1 brarti ada username n pass di db 
    if found == 1:
        querygetdata = "SELECT username,photo,name,email,telp,address,total FROM `users` WHERE username='{}' AND password='{}'".format(username,md5_password)
        cur.execute(querygetdata)
        row_headers=[x[0] for x in cur.description] #this will extract row headers
        rv = cur.fetchall()
        json_data=[]
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        json_response['data'] = json.loads(json.dumps(json_data[0]))
        json_response['code'] = 0
        json_response['message'] = 'success'
        update_islogin = "UPDATE `users` SET `isLogin` = '1' WHERE username ='{}';".format(username)
        cur.execute(update_islogin)
        mysql.connection.commit()
        return json_response
    json_response['code'] = 9999
    json_response['message'] = "failed"
    return json_response

@app.route('/apichangepassword',methods=['GET','POST'])
def apichangepassword():
    json_response = {}

    username = request.json['username']
    password = request.json['password']

    # md5
    hash_obj = hashlib.md5(password.encode())
    md5_password = hash_obj.hexdigest()

    cur = mysql.connection.cursor()
    query = "SELECT username FROM `users` WHERE username ='{}'".format(username)
    query_executed = cur.execute(query)

    if query_executed == 1:
        query_get_data = "UPDATE `users` SET `password` = '{}' WHERE `users`.`username` = '{}'".format(md5_password,username)
        cur.execute(query_get_data)
        mysql.connection.commit()
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

@app.route('/apigetlistbencana',methods=['GET','POST'])
def apigetlistbencana():
    json_response = {}

    cur = mysql.connection.cursor()
    # BENAKNO DATE DOL RIBET IKU
    query = "SELECT disasterDate FROM `listbencana` ORDER BY disasterDate DESC LIMIT 10"
    found = cur.execute(query)

    # found > 0 brarti ada username n pass di db 
    if found > 0:
        row_headers = [x[0] for x in cur.description] #this will extract row headers
        rv = cur.fetchall()
        json_data = []
        date = []
        c = 0
        for r in range(2):
            date.append(str(rv[r][0]))
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
            c+=1
        json_response['data'] = json_data

        query1 = "SELECT id,disasterTitle,description,disasterPhoto,donationMethod,disasterType,location,disasterDate FROM `listbencana` ORDER BY disasterDate DESC LIMIT 10"
        cur.execute(query1)
        row_headers1 = [x[0] for x in cur.description] #this will extract row headers
        rv1 = cur.fetchall()
        c1 = 0 
        for result1 in rv1:
            x = dict(zip(row_headers1,result1))
            json_response['data'][c1].update(x)
            c1 += 1
        json_response['code'] = 0
        json_response['message'] = 'success'
        return json_response
    json_response['code'] = 9999
    json_response['message'] = "failed"
    return json_response

@app.route('/apilogout',methods=['GET','POST'])
def apilogout():
    json_response = {}

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

@app.route('/apiregister',methods=['GET','POST'])
def apiregister():
    json_response = {}

    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']
    telp = request.json['telp']

    # md5
    hash_obj = hashlib.md5(password.encode())
    md5_password = hash_obj.hexdigest()

    cur = mysql.connection.cursor()
    query = "INSERT INTO `users` (`id`, `username`, `password`, `name`, `email`, `telp`, `anonymous`) VALUES (NULL, '{}', '{}', '{}', '{}', '{}', 0);".format(username,md5_password,name,email,telp)
    try:
        query_executed = cur.execute(query)
    except:
        json_response['code'] = 9998
        json_response['message'] = 'failed'
        cur.close()
        return json_response
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

@app.route('/apiupdateprofil',methods=['GET','POST'])
def apiupdateprofil():
    json_response = {}

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

@app.route('/apidetail',methods=['GET','POST'])
def apidetail():
    json_response = {}

    id = request.json['id']

    cur = mysql.connection.cursor()
    query = "SELECT type, need, colected FROM `detailbencana` WHERE listbencana='{}' ".format(id)
    found = cur.execute(query)

    if found >0:
        json_response['data'] = []
        row_headers=[x[0] for x in cur.description] #this will extract row headers
        rv = cur.fetchall()
        json_data=[]
        for result in rv:
            x = dict(zip(row_headers,result))
            json_response['data'].append(x)
        json_response['code'] = 0
        json_response['message'] = 'success'
        cur.close()
        return json_response
    json_response['code'] = 9997
    json_response['message'] = "failed"
    cur.close()
    return json_response

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)