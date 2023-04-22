import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="world"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM country"

mycursor.execute(sql)

results = mycursor.fetchall()

for row in results:
  # Access the values of each column using the index or column name
  print(row[0], row[1], row[2])

mydb.close()