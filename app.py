from flask import Flask,render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure db
app.config['MYSQL_HOST']="mysql-crud"
app.config["MYSQL_USER"] = "godi"
app.config["MYSQL_PASSWORD"] = "godi"
app.config["MYSQL_DB"] = "flaskapp"

mysql = MySQL(app)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        # Fetch the Form Data
        name = request.form.get("name")
        email = request.form.get("email")

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name,email))
        mysql.connection.commit()
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