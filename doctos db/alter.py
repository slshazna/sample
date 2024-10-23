import mysql.connector
mysdb=mysql.connector.connect(
host="localhost",
user="root",
password='root123',
database='doctos')

mycursor=mysdb.cursor()
alter_query="alter table employee add column designation varchar(255)"
mycursor.execute(alter_query)
print('success')
mysdb.commit()
mycursor.close()
mysdb.close()