from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import json
import hashlib
from datetime import date
from json import dumps

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'userdb'

mysql = MySQL(app)

@app.route('/',methods=['GET','POST'])
def home():
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
        print(row_headers)
        print(date)
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
            c+=1
        json_response['data'] = json_data

        query1 = "SELECT disasterTitle,description,disasterPhoto,donationMethod,disasterType,location FROM `listbencana` ORDER BY disasterDate DESC LIMIT 10"
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

if __name__ == '__main__':
    app.run(debug=True)