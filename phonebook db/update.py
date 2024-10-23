import mysql.connector
mysdb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root123',
    database='contacts')

mycursor=mysdb.cursor()
name=input('enter the name')
place=input('enter the place')
mycursor.execute('update details set place=%s where name=%s',(place,name))
mycursor.execute('update details set age=%s where name=%s',(name,age))
mysdb.commit()
print('succesfull')