import mysql.connector
import csv

def query_with_id(id_value):
    # Connect to MySQL database
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="123456",
      database="world"
    )

    # Create a cursor object
    mycursor = mydb.cursor()

    # Define the query with the provided ID value in the WHERE clause
    sql = "SELECT * FROM country WHERE Code = %s"
    #'MY-SZB-2023-22129'
    val = (id_value,)

    # Execute the query
    mycursor.execute(sql, val)

    # Fetch the results
    results = mycursor.fetchall()

    # Print the results
    #for result in results:
    #    print(result)
    
    # Open a CSV file for writing
    with open("Countrs.csv", 'a', newline='') as csvfile:
        # Create a CSV writer object
        csvwriter = csv.writer(csvfile)

        # Write the header row
        #csvwriter.writerow([i[0] for i in mycursor.description])

        # Write each row of data to the CSV file
        for row in results:
            csvwriter.writerow(row)
    mydb.close()

# Open the CSV file using the built-in `open()` function
with open('countrycode.csv', 'r') as csv_file:

    # Create a `csv.reader` object to read the CSV file
    csv_reader = csv.reader(csv_file)

    # Loop through each row in the CSV file and print it without square brackets
    for row in csv_reader:
        my_string = ', '.join(row)
        query_with_id(my_string)
    #    print(",".join(row))
    #   query_with_id("MY-SZB-2023-22129")
