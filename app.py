from flask import Flask,render_template,request
import mysql.connector
import os

app = Flask(__name__)

# get Mysql Password.
mysql_password = os.getenv("MYSQL_ROOT_PASSWORD")
# Configure db

connection = mysql.connector.connect(user="root",password=mysql_password,host="mysql",database="flaskapp")

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        # Fetch the Form Data
        name = request.form.get("name")
        email = request.form.get("email")

        cur = connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name,email))
        cur.close()
        return 'Success'
    return render_template('index.html')

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("select * from users")

    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails= userDetails)
@app.route('/jin/<name>')
def jin(name):
    return render_template('jin.html',user_name= name)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)