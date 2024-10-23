import mysql.connector
mysdb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root123',
    database='contacts'
)
mycursor=mysdb.cursor()
# mycursor.execute('select place from details')
# mycursor.execute('select * from details')
mycursor.execute('select * from details order by name asc')
mylist=mycursor.fetchall()
for i in mylist:
    print(i)