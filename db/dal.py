# data access layer

import sqlite3
ADMIN_USER="admin"
ADMIN_PASSWORD="admin"

class DAL:
    filename='users.db'
    def __init__(self) -> None:
        self.initialize()

    def exec(self, SQL):
            rows=[]
            with sqlite3.connect(self.filename) as con:
                cur=con.cursor()
                cur.execute(SQL)
                con.commit()
                rows=cur.fetchall()
            return rows
    
    def initialize(self):
        self.exec("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    
    def authenticate(self, username, password):
        rows=self.exec(f'SELECT rowid,username,password FROM users WHERE username="{username}" and password="{password}"')
        if len(rows)>0:
            return rows[0][0]
        else:
            return "null"

    def authenticatePasswordAndId(self, password, id):
        rows=self.exec(f'SELECT rowid,username,password FROM users WHERE password="{password}" and rowid="{id}"')
        if len(rows)>0:
            return rows[0][1]
        else:
            return "null"

    def add(self, new_username, new_password):
        self.exec(f'INSERT INTO users VALUES ("{new_username}","{new_password}")')
        rows=self.exec(f'SELECT rowid,username,password FROM users WHERE username="{new_username}" and password="{new_password}"')
        id=rows[0][0]
        return id

    def remove(self, id):
        self.exec(f'DELETE FROM users WHERE rowid="{id}"')
        return True

    def update(self, id, username, password):
        self.exec(f'UPDATE users SET username="{username}", password="{password}" WHERE rowid="{id}"')
        return True
        
    def list1(self):
        rows=self.exec('SELECT rowid,username,password FROM users')
        return rows
    
    def openDB(self):
        self.exec("CREATE TABLE IF NOT EXISTS kenes (firstName TEXT, lastName TEXT, email TEXT)")

    def enterDB(self,rows):
        DAL().openDB()
        firstName=rows[0][0]
        lastName=rows[0][1]
        email=rows[0][2]
        self.exec(f'INSERT INTO kenes VALUES ("{firstName}","{lastName}","{email}")')

    def searchInDB(self,email):
        rows=self.exec(f'SELECT * FROM students WHERE email="{email}"')
        print("len: ", len(rows))
        if len(rows)>0:
            DAL().enterDB(rows)
            return rows
        else:
            return "null"     

class User(): 
    def __init__(self, email='none', firstName='none', lastName='none') -> None:
        self.email=email
        self.firstName=firstName
        self.lastName=lastName

    def searchInDB(self):
        print("d: ",self.email, self.firstName, self.lastName)
        d=DAL().searchInDB(email=self.email)
        print("users: ", d)
        return d