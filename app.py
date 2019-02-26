from flask import Flask, jsonify, request, render_template
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)
db = yaml.load(open('db.yaml'))

#db settings
app.config['MYSQL_HOST'] 	 = db['mysql_host']
app.config['MYSQL_USER'] 	 = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB']		 = db['mysql_db']

mysql = MySQL(app)

## Using SQL - Read
@app.route('/cards/', methods=['GET'])
def home():
	cursor = mysql.connection.cursor()
	result = cursor.execute("SELECT * FROM cards")
	if result > 0:
		cards = cursor.fetchall()
		return render_template('index.html', cards=cards )

## Create
@app.route('/cards/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        name = request.form['name']
        flag = request.form['flag']
        cursor = mysql.connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS cards(PersonID int NOT NULL PRIMARY KEY AUTO_INCREMENT, name varchar(255), flag varchar(100))")
        cursor.execute("INSERT INTO cards VALUES (null, %s, %s);", (name, flag))
        mysql.connection.commit()
        mysql.connection.close()
        return 'Sucess! :)'

## Update
@app.route('/cards/update', methods=['POST', 'PUT'])
def update():
    if request.method == "POST" or request.method == "PUT":
        id_num = request.form['id']
        name = request.form['name']
        flag = request.form['flag']
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE cards SET name = %s, flag = %s WHERE id = %s;", (name, flag, id_num))
        mysql.connection.commit()
        mysql.connection.close()        
        return 'Sucess! :)'

## Delete
@app.route('/cards/delete', methods=['POST'])
def delete():
    if request.method == "POST":
        id_num = request.form['id']        
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM cards WHERE id = %s;", id_num)
        mysql.connection.commit()
        mysql.connection.close()
        return 'Sucess! :)'


if(__name__ == '__main__'):
	app.run(host = 'localhost', debug = True)
	#app.run(host = 'localhost', port = 8088, debug = True)