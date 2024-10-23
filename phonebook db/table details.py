import mysql.connector
mysdb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root123',
    database='contacts')

mycursor = mysdb.cursor()
mycursor.execute('create table details(id int auto_increment primary key,name varchar(10),place varchar(50),phone int)')
print('table created')
mycursor.close()
mysdb.close()