import mysql.connector #must download in pip
try:
    ARTdb = mysql.connector.connect(    #building connection to database
    host="localhost",                   #database is hosted on local machine
    user="ART",                         #Username to access database
    password="ARTpw",                   #Password to access database
    database='ART',                     #Database name
    ssl_disabled='True'
    )

    cursor = ARTdb.cursor()             #builds a cursor to retain selected information from queries
    query = "SELECT username from User" #SQL Query
    cursor.execute(query)               #Executes query with cursor

    for (username) in cursor:           #How to iterate over cursor
        print(username)

    cursor.close()
except mysql.connector.Error as err:
    print(err)
finally:
    ARTdb.close()

