import mysql.connector

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

my_db = mysql.connector.connect(
    host = "localhost",     #to connect to local host
    user= "root",
    password = "root",
    database = "P_sample" #create a database and then call it here
)

mycursor = my_db.cursor()   # control the cursor
print(my_db)

mycursor.execute("SHOW DATABASES")
# code was executed with no errors

for x in mycursor:
   print(x) # for printing the resulting tuple in cursor

# Creating Database
mycursor.execute("create database P_sample")

# Creating a New Table
mycursor.execute("CREATE TABLE sample_t1 (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("show tables")
for x in mycursor:
    print(x)

mycursor.execute("ALTER TABLE sample_t1 ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")  # ALTER table used to make changes.

# INSERT INTO

sql = "insert into sample_t1 (name, address) values (%s, %s)"
val = ("John", "Hoghway 21")
mycursor.execute(sql,val)

sql = "INSERT INTO sample_t1 (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)
#executemany is used

my_db.commit() # commit is used.

print(mycursor.rowcount, "record inserted.")
# mycursor.lastrowid is used to get last ID

mycursor.execute("select * from sample_t1")
myresult = mycursor.fetchall()
#a variable is used to store the data
#fetchall, fetchone can be use
for x in myresult:
    print(x)

# WHERE

sql = "SELECT * FROM sample_t1 WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)
for x in mycursor:
    print(x)

sql = "SELECT * FROM sample_t1 WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# ORDER BY

sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)

sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

# DELETE TABLE

sql = "DELETE FROM sample_t1 WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)
my_db.commit()

# DROP TABLE

sql = "DROP TABLE sample_t1"

mycursor.execute(sql)

# UPDATE TABLE

sql = "UPDATE sample_t1 SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

my_db.commit() # commit is used.

# LIMIT

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

# offset = Skips a number of rows before starting to return rows.
# limit = Specifies the maximum number of rows to return.

# JOIN 

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)



------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
