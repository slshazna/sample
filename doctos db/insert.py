import mysql.connector
mysdb=mysql.connector.connect(
host="localhost",
user="root",
password='root123',
database='doctos')

mycursor=mysdb.cursor()
Name=input("enter the name")
Age=int(input('enter the age'))
mycursor.execute('insert into employee(name,age) values(%s,%s)',(Name,Age))
mysdb.commit()
print('done')