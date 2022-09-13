from urllib import response
from flask import Flask,Response,request
app = Flask(__name__)
import json
import sqlite3
from db.dal import DAL,User

@app.route('/enterEmail',methods=["POST"])
def enterEmail():
    email=request.json["email"]
    user=User(email)
    rows=user.searchInDB()
    r=Response(json.dumps({'rows':rows}))
    r.headers["Content-type"]="application/json"
    return r