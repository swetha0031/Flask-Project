from flask import flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'W@2915djkq#'
app.config['MYSQL_DB'] = 'users'  

mysql = MySQL(app)

@app.route('/hello')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/users')
def list_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    return render_template('users.html', users=users)

@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template('new_user.html')

@app.route('/users/<int:id>')
def user_details(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cur.fetchone()
    cur.close()
    if user:
        return render_template('user_details.html', user=user)
    else:
        return "Error"
