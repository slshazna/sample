import mysql.connector
mysdb=mysql.connector.connect(
host="localhost",
user="root",
password='root123',
database='doctos')

mycursor=mysdb.cursor()
Name=input('enter the name')
Age=input('enter the age')
mycursor.execute("update employee set age=%s where name=%s",(Age,Name))
print('success')
mysdb.commit()
