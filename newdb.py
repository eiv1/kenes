#for testing 
from faker import Faker
import sqlite3
# import uuid

con=sqlite3.connect('users.db')
cur=con.cursor()

def create_mock_users(user_num=20):
    for i in range(user_num):
        firstName=Faker().first_name()
        lastName=Faker().last_name()
        email=Faker().email()
        cur.execute(f'INSERT INTO students VALUES ("{firstName}","{lastName}","{email}")')
    con.commit()    
    cur.close()
    con.close()

def initialize():
    cur.execute('CREATE TABLE IF NOT EXISTS students ("firstName" TEXT, "lastName" TEXT, "email" TEXT)')
    create_mock_users()

initialize()