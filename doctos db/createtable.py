import mysql.connector
mysdb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root123',
    database='doctos')

mycursor = mysdb.cursor()
mycursor.execute("CREATE TABLE employee (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(50),age INT)")
print("Table created successfully")
mycursor.close()
mysdb.close()

