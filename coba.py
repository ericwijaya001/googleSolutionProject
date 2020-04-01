from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__,template_folder='template')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flaskapp'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        nama = details['nama']
        email = details['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `users` (`id`, `name`, `email`) VALUES (NULL, %s, '%s);", (nama, email))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)