from flask import Flask,render_template,request
from flask_mysqldb import MySQL
import yaml
app = Flask(__name__)

# Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST']= db['mysql_host']
app.config['MYSQL_USER']= db['mysql_user']
app.config['MYSQL_PASSWORD']= db['mysql_password']
app.config['MYSQL_DB']= db['mysql_db']

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