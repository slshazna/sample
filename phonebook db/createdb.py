import mysql.connector
mysdb=mysql.connector.connect(
host='localhost',
user='root',
password='root123')
mycursor=mysdb.cursor()

mycursor.execute("create database contacts")
print('success')