import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='iljas',
    password='',
    database='iljasdatabase'
)

yourcursor = mydb.cursor()

yourcursor.execute("CREATE DATABASE iljasdatabase")