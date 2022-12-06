#------------------------task1--------------------------------------
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='yourpassword',
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE my_first_db2")

#-------------------------------------------------------------------

#------------------------task2--------------------------------------
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='yourpassword',
)

mycursor = mydb.cursor()
mycursor.execute("use my_first_db2; CREATE table student(id INT,  name VARCHAR(255));")
#-------------------------------------------------------------------

#------------------------task3--------------------------------------
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='yourpassword',
)

mycursor = mydb.cursor()
mycursor.execute("use my_first_db2; CREATE table employee(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255),salary INT(6));")
#-------------------------------------------------------------------

#------------------------task4--------------------------------------
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='yourpassword',
)

mycursor = mydb.cursor()
mycursor.execute("use my_first_db2; ALTER TABLE student ADD PRIMARY KEY (id);")
#-------------------------------------------------------------------

#------------------------task5--------------------------------------
#------------------------student--------------------------------------
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='yourpassword',
    database='my_first_db2'
)

mycursor = mydb.cursor()

sql = "INSERT INTO student (id, name) VALUES (%s, %s)"
val = ('01', 'John')

mycursor.executemany(sql, val)
mydb.commit()

#----------------------------employee--------------------------------
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='yourpassword',
    database='my_first_db2'
)

mycursor = mydb.cursor()
# mycursor.execute("INSERT INTO student (id, name) VALUES (01, 'Johny'); ")
sql = "INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)"
val = [('01', 'John', '10000')]

mycursor.executemany(sql, val)
mydb.commit()
#-------------------------------------------------------------------