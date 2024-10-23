import mysql.connector
mysdb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root123',
    database='contacts'
)
mycursor=mysdb.cursor()
alter_query="alter table details add column age int"
mycursor.execute(alter_query)
mysdb.commit()
mycursor.close()
mysdb.close()
print('success')