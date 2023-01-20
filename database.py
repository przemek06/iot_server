import sqlite3

class Database:

    instances = {}

    @classmethod
    def add_instance(cls, id, encoder):
        cls.instances[id] = encoder

    @classmethod
    def get_instance(cls, id):
        return cls.instances[id]

    def __init__(self):
        self.create_table()

    def create_table(self):
        con = sqlite3.connect("users.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users_(uid, email)")

    def find_email_by_uid(self, uid):
        con = sqlite3.connect("users.db")
        cur = con.cursor()
        res = cur.execute("SELECT email FROM users_ WHERE uid = '{}'".format(uid))
        row = res.fetchone()
        return row

