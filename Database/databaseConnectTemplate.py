import mysql.connector #must download in pip

def noVariableSelectTemplate():
    try:
        ARTdb = mysql.connector.connect(    #building connection to database
        host="localhost",                   #database is hosted on local machine
        user="ART",                         #Username to access database
        password="ARTpw",                   #Password to access database
        database='ART',                     #Database name
        ssl_disabled='True',
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

def variableSelectTemplate():
    try:
        ARTdb = mysql.connector.connect(    #building connection to database
        host="localhost",                   #database is hosted on local machine
        user="ART",                         #Username to access database
        password="ARTpw",                   #Password to access database
        database='ART',                     #Database name
        ssl_disabled='True',
        )

        cursor = ARTdb.cursor()             #builds a cursor to retain selected information from queries
        query = "SELECT username from User where username='%s'" #SQL Query with variable inserts: %s for string, %d for integers
        cursor.execute(query, ("string"))               #Executes query with cursor

        for (username) in cursor:           #How to iterate over cursor
            print(username)

        cursor.close()
    except mysql.connector.Error as err:
        print(err)
    finally:
        ARTdb.close()

def insertTemplate():
    try:
        ARTdb = mysql.connector.connect(    #building connection to database
        host="localhost",                   #database is hosted on local machine
        user="ART",                         #Username to access database
        password="ARTpw",                   #Password to access database
        database='ART',                     #Database name
        ssl_disabled='True',
        )

        cursor = ARTdb.cursor()             #builds a cursor to retain selected information from queries
        query = "INSERT INTO User (username, password, email) VALUES (%s, %s, %s)"   #SQL Query with variable inserts: %s for string, %d for integers
        cursor.execute(query, ("string", "asd", "asd@asd.ca"))               #Executes query with cursor
        ARTdb.commit()      #uploads and commits data to database

        cursor.close()
    except mysql.connector.Error as err:
        print(err)
    finally:
        ARTdb.close()

insertTemplate()
noVariableSelectTemplate()
