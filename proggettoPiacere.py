# save this as app.py
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS Education_Rich_People")

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Education_Rich_People.Rich_People (
        Name VARCHAR(100) NOT NULL,
        Profession VARCHAR(100),
        Degree VARCHAR(100),
        Field VARCHAR(100),
        Institution VARCHAR(100),
        Graduation_Year VARCHAR(10),
        Country VARCHAR(100),
        University_Global_Ranking VARCHAR(100),
        GPA VARCHAR(255),
        Scholarship_Award VARCHAR(255),
        PRIMARY KEY (Name)
    );""")
mydb.commit()

mycursor.execute("DELETE FROM Education_Rich_People.Rich_People")
mydb.commit()

rich_data = pd.read_csv('./successful_educations.csv', index_col=False, delimiter=',')
rich_data = rich_data.fillna('Null')

for i, row in rich_data.iterrows():
    cursor = mydb.cursor()
    sql = """
        INSERT INTO Education_Rich_People.Rich_People
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    row['GPA'] = str(row['GPA']).strip()
    cursor.execute(sql, tuple(row))
    mydb.commit()
    cursor.close()

mycursor.execute("SELECT * FROM Education_Rich_People.Rich_People LIMIT 10")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)