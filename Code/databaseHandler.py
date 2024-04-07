import mysql.connector #must download in pip
from validation import parameterValidator

class databaseHandler:

    Validator = parameterValidator()

    def openDatabaseConnection(self):   #opens db connection and returns it
        ARTdb = mysql.connector.connect(    #building connection to database
        host="localhost",                   #database is hosted on local machine
        user="ART",                         #User name to access database
        password="ARTpw",                   #Password to access database
        database='ART',                     #Database name
        ssl_disabled='True',
        port=3307                           #port number
        )
        return ARTdb
    
    def getUsers(self):
        users = []
        try:
            ARTdb = self.openDatabaseConnection()
            cursor = ARTdb.cursor()
            query = "SELECT username from User ORDER BY username"
            cursor.execute(query)

            for user in cursor:
                users.append(user[0])

            cursor.close()
        except mysql.connector.Error as err:
            print(err)
        finally:
            ARTdb.close()
            return users

    def getUserById(self, id: int):
        userInfo = None
        try:
            ARTdb = self.openDatabaseConnection()
            cursor = ARTdb.cursor()
            query = "SELECT * from User WHERE id = %s"
            cursor.execute(query, (id,))

            for user in cursor:
                userInfo = user

            cursor.close()
        except mysql.connector.Error as err:
            print(err)
        finally:
            ARTdb.close()
            return userInfo

    def validateUser(self, username: str, password: str) -> bool:   #returns if username and password combination is in list of users
        if (self.Validator.validateNames(username) is None and self.Validator.validatePassword(password)):
            userId = None
            try:
                ARTdb = self.openDatabaseConnection()
                cursor = ARTdb.cursor()
                query = "SELECT id, username, password from User WHERE username = %s AND password = %s"
                cursor.execute(query, (username, password))

                for user in cursor:
                    userId = user[0]

                cursor.close()
            except mysql.connector.Error as err:
                print(err)
            finally:
                ARTdb.close()
                return userId
        return None

    def createUser(self, name: str, password: str, email: str, dob: str):   #registers a user to the database
        if (self.Validator.validateNames(name) is None and self.Validator.validatePassword(password) and self.Validator.validateEmail(email)):  #todo, add dob validation when implemented
            try:
                ARTdb = self.openDatabaseConnection()

                cursor = ARTdb.cursor()             #builds a cursor to retain selected information from queries
                query = "INSERT INTO User (username, password, email, dateOfBirth) VALUES (%s, %s, %s, %s)"   #SQL Query with variable inserts: %s for string, %d for integers
                cursor.execute(query, (name, password, email, dob))               #Executes query with cursor
                ARTdb.commit()      #uploads and commits data to database

                cursor.close()
                validation = True
            except mysql.connector.Error as err:
                print(err)
                validation = False
            finally:
                ARTdb.close()
                return validation   #returns whether a user was successfully created
        return False
    
    def editUser(self, id: int, name: str, password: str, email: str, dob: str, pronouns: str, desc: str):   #edits a user in the database
        if (self.Validator.validateNames(name) is None and self.Validator.validatePassword(password) and self.Validator.validateEmail(email)):  #todo, add dob validation when implemented
            try:
                ARTdb = self.openDatabaseConnection()

                cursor = ARTdb.cursor()             #builds a cursor to retain selected information from queries
                query = "UPDATE User SET username = %s, password = %s, email = %s, dateOfBirth = %s, pronouns = %s, userDescription = %s WHERE id = %s"   #SQL Query with variable inserts: %s for string, %d for integers
                cursor.execute(query, (name, password, email, dob, pronouns, desc, id))               #Executes query with cursor
                ARTdb.commit()      #uploads and commits data to database

                cursor.close()
                validation = True
            except mysql.connector.Error as err:
                print(err)
                validation = False
            finally:
                ARTdb.close()
                return validation   #returns whether a user was successfully edited
        return False
    
    def getChannels(self):
        channels = []
        try:
            ARTdb = self.openDatabaseConnection()
            cursor = ARTdb.cursor()
            query = "SELECT name FROM Channel"
            cursor.execute(query)

            for channel in cursor:
                channels.append(channel[0])

            cursor.close()
        except mysql.connector.Error as err:
            print(err)
        finally:
            ARTdb.close()
            return channels
    
    def getChannelByName(self, name: str):
        channel = None
        if (self.Validator.validateNames(name) is None):
            try:
                ARTdb = self.openDatabaseConnection()
                cursor = ARTdb.cursor()
                query = "SELECT id, name FROM Channel WHERE name = %s"
                cursor.execute(query, (name,))

                for c in cursor:
                    channel = c

                cursor.close()
            except mysql.connector.Error as err:
                print(err)
            finally:
                ARTdb.close()
        return channel
        
    def searchChannelsByName(self, name: str):
        channels = []
        if (self.Validator.validateNames(name) is None):
            try:
                ARTdb = self.openDatabaseConnection()
                cursor = ARTdb.cursor()
                query = "SELECT name FROM Channel WHERE name LIKE '%%s%'"
                cursor.execute(query, (name,))

                for channel in cursor:
                    channels.append(channel[1])

                cursor.close()
            except mysql.connector.Error as err:
                print(err)
            finally:
                ARTdb.close()
        return channels
        
    def createChannel(self, name: str):
        if (self.Validator.validateNames(name) is None):
            try:
                ARTdb = self.openDatabaseConnection()
                cursor = ARTdb.cursor()
                query = "INSERT INTO Channel (name) VALUES (%s)"
                cursor.execute(query, (name,))
                ARTdb.commit()

                cursor.close()
                validation = True
            except mysql.connector.Error as err:
                print(err)
                validation = False
            finally:
                ARTdb.close()
                return validation
        return False
    
    def deleteChannel(self, name: str):
        if (self.Validator.validateNames(name) is None):
            try:
                ARTdb = self.openDatabaseConnection()
                cursor = ARTdb.cursor()
                query = "DELETE FROM Channel WHERE name = %s"
                cursor.execute(query, (name,))
                ARTdb.commit()

                cursor.close()
                validation = True
            except mysql.connector.Error as err:
                print(err)
                validation = False
            finally:
                ARTdb.close()
                return validation
        return False
    
    def getAdminById(self, userId: int, channelId: int):
        admin = None
        if (self.Validator.validateInt(userId) and self.Validator.validateInt(channelId)):
            try:
                ARTdb = self.openDatabaseConnection()
                cursor = ARTdb.cursor()
                query = "SELECT * FROM Admins WHERE userId = %s AND channelId = %s"
                cursor.execute(query, (userId, channelId))

                for a in cursor:
                    admin = a

                cursor.close()
            except mysql.connector.Error as err:
                print(err)
            finally:
                ARTdb.close()
        return admin
    
    def addAdmin(self, userId: int, channelId: int):
        if (self.Validator.validateInt(userId) and self.Validator.validateInt(channelId)):
            try:
                ARTdb = self.openDatabaseConnection()
                cursor = ARTdb.cursor()
                query = "INSERT INTO Admins (userId, channelId) VALUES (%s, %s)"
                cursor.execute(query, (userId, channelId))
                ARTdb.commit()

                cursor.close()
                validation = True
            except mysql.connector.Error as err:
                print(err)
                validation = False
            finally:
                ARTdb.close()
                return validation
        return False
    
    def removeAdmin(self, userId: int, channelId: int):
        if (self.Validator.validateInt(userId) and self.Validator.validateInt(channelId)):
            try:
                ARTdb = self.openDatabaseConnection()
                cursor = ARTdb.cursor()
                query = "DELETE FROM Admins WHERE userId = %s AND channelId = %s"
                cursor.execute(query, (userId, channelId))
                ARTdb.commit()

                cursor.close()
                validation = True
            except mysql.connector.Error as err:
                print(err)
                validation = False
            finally:
                ARTdb.close()
                return validation
        return False