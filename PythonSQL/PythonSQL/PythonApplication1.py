print("Hello world.")
import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=.;'
                      'Database=northwind;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute('SELECT * FROM Products')
for row in cursor:
    print(row)

