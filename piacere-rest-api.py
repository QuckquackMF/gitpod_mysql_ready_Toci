import mysql.connector
from flask import Flask, jsonify
from flask_cors import CORS
import random

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Education_Rich_People"
)
mycursor = mydb.cursor(dictionary=True)

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/all")
def getAllData():
    mycursor.execute("SELECT * FROM Education_Rich_People.Rich_People")
    myresult = mycursor.fetchall()
    result = []
    for x in myresult:
        print(x)
        result.append(x)
    return jsonify(result)

@app.route("/names")
def get_names():
    mycursor.execute("SELECT Name FROM Education_Rich_People.Rich_People")
    myresult = mycursor.fetchall()
    result = []
    for x in myresult:
        print(x)
        result.append(x)
    return jsonify(result)

@app.route("/profession")
def get_profession():
    mycursor.execute("SELECT Profession FROM Education_Rich_People.Rich_People")
    myresult = mycursor.fetchall()
    result = []
    for x in myresult:
        print(x)
        result.append(x)
    return jsonify(result)

@app.route("/degree")
def get_degree():
    mycursor.execute("SELECT Degree FROM Education_Rich_People.Rich_People")
    myresult = mycursor.fetchall()
    result = []
    for x in myresult:
        print(x)
        result.append(x)
    return jsonify(result)

@app.route("/ranking")
def get_ranking():
    mycursor.execute("SELECT University_Global_Ranking FROM Education_Rich_People.Rich_People")
    myresult = mycursor.fetchall()
    result = []
    for x in myresult:
        print(x)
        result.append(x)
    return jsonify(result)

@app.route("/search/<name>")
def search_by_name(name):
    sql = "SELECT * FROM Education_Rich_People.Rich_People WHERE Name LIKE %s"
    mycursor.execute(sql, (f"%{name}%",))
    found_people = mycursor.fetchall()
    if found_people:
        return jsonify(found_people)
    else:
        return jsonify({"message": f"Person with name '{name}' not found."})

@app.route("/random")
def get_random():
    mycursor.execute("SELECT * FROM Education_Rich_People.Rich_People")
    all_people = mycursor.fetchall()
    if all_people:
        random_person = random.choice(all_people)
        return jsonify(random_person)
    else:
        return jsonify({"message": "No people found in the database."})

if __name__ == "__main__":
    app.run(debug=True)