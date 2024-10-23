import mysql.connector
mysdb=mysql.connector.connect(
host="localhost",
user="root",
password='root123',
database='doctos')

mycursor=mysdb.cursor()
Name=input('enter the name')
mycursor.execute("DELETE FROM employee WHERE name = %s",(Name,))
mysdb.commit()
print('success')