import mysql.connector #must download in pip

class databaseHandler:
    ARTdb = None;

    def openDatabaseConnection(self):   #opens db connection
        self.ARTdb = mysql.connector.connect(    #building connection to database
        host="localhost",                   #database is hosted on local machine
        user="ART",                         #User name to access database
        password="ARTpw",                   #Password to access database
        database='ART',                     #Database name
        ssl_disabled='True',
        )

    def getUsers(self): #temporary, prints all users and all info from users
        try:
            self.openDatabaseConnection()
            cursor = self.ARTdb.cursor()             #builds a cursor to retain selected information from queries
            query = "SELECT * from User" #SQL Query with variable inserts: %s for string, %d for integers
            cursor.execute(query)               #Executes query with cursor

            for (user) in cursor:           #How to iterate over cursor, is all variables selected
                print(user)

            cursor.close()
        except mysql.connector.Error as err:
            print(err)
        finally:
            self.ARTdb.close()

    def createUser(self, name, password, email, dob):   #registers a user to the database
        try:
            self.openDatabaseConnection()

            cursor = self.ARTdb.cursor()             #builds a cursor to retain selected information from queries
            query = "INSERT INTO User (username, password, email, dateOfBirth) VALUES (%s, %s, %s, %s)"   #SQL Query with variable inserts: %s for string, %d for integers
            cursor.execute(query, (name, password, email, dob))               #Executes query with cursor
            self.ARTdb.commit()      #uploads and commits data to database

            cursor.close()
            validation = True
        except mysql.connector.Error as err:
            print(err)
            validation = False
        finally:
            self.ARTdb.close()
            return validation   #returns whether a user was successfully created
        
    def validateEmail(self):
        return True
    
    def validateDOB(self):
        return True
    
    def validateUsername(self):
        return True
    
    def validatePassword(self):
        return True
    
    #def convertDOB(self): idk if I need this yet

Connector = databaseHandler()
Connector.createUser("test", "test", "email@can.ca", "2001-09-01")
Connector.getUsers()
