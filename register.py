from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/register', methods=['POST'])
def register():
    try:
        uid = request.form['uid']
        email = request.form['email']
        con = sqlite3.connect("users.db")
        cur = con.cursor()
        cur.execute("INSERT INTO users_ VALUES ('{}', '{}')".format(uid, email))
        con.commit()
        return "done"
    except Exception as e:
        print(e)
        return "error"

@app.route('/users', methods=['GET'])
def get_users():
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM users_")
    all = cur.fetchall()
    return str(all)

