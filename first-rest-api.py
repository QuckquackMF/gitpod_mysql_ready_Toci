import mysql.connector
from flask import Flask, jsonify
import json

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="CLASH_ROYALE"
)
mycursor = mydb.cursor()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/getAllDataInHtml")
def getAllData():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit")
    row_headers=[x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    result = []
    for resulti in myresult:
        result.append(dict(zip(row_headers,resulti))) #zip in Python è una funzione integrata molto utile che aggrega elementi da due o più iterabili (come liste o tuple) in un singolo iterabile di tuple.
    return jsonify(result)

@app.route("/air_transport")
def airTransport():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Transport='Air'")
    myresult = mycursor.fetchall()
    result = []
    for x in myresult:
        print(x)
        result.append(x)
    return jsonify(result)

@app.route("/epic_units")
def epicUnits():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Rarity='Epic'")
    myresult = mycursor.fetchall()
    result = []
    for x in myresult:
        print(x)
        result.append(x)
    return jsonify(result)

@app.route("/type")
def typeUnits():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Type='Troop'")
    myresult = mycursor.fetchall()
    result = []
    for x in myresult:
        print(x)
        result.append(x)
    return jsonify(result)

@app.route("/cost")
def costUnits():
    mycursor.execute("SELECT * FROM CLASH_ROYALE.Clash_Unit WHERE Cost=3")
    myresult = mycursor.fetchall()
    result = []
    for x in myresult:
        print(x)
        result.append(x)
    return jsonify(result)

if __name__ == "__main__":
    app.run()