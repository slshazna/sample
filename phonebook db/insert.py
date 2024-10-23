import mysql.connector
mysdb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root123',
    database='contacts'
)
mycursor=mysdb.cursor()
name=input('enter the name')
place=input('enter the place')
phone=int(input('enter the phone number'))
mycursor.execute('insert into details(name,place,phone) values (%s,%s,%s)',(name,place,phone))
mysdb.commit()
print('successfull')