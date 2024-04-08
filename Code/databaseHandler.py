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
    
    #Returns a list of the usernames of all users in the database in alphabetical order
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

    #Returns the information of a user matching the given user id
    def getUserById(self, id: int):
        if (self.Validator.validateInt(id)):
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
        return None
    
    #Returns the information of a user matching the given username
    def getUserByName(self, name: str):
        if (self.Validator.validateNames(name) is None):
            userInfo = None
            try:
                ARTdb = self.openDatabaseConnection()
                cursor = ARTdb.cursor()
                query = "SELECT * from User WHERE username = %s"
                cursor.execute(query, (name,))

                for user in cursor:
                    userInfo = user

                cursor.close()
            except mysql.connector.Error as err:
                print(err)
            finally:
                ARTdb.close()
                return userInfo
        return None

    #Returns if the given username and password combination is in the list of users
    def validateUser(self, username: str, password: str) -> bool:
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

    #Registers a user to the database with the given information
    def createUser(self, name: str, password: str, email: str, dob: str):   
        if (self.Validator.validateNames(name) is None and self.Validator.validatePassword(password) and self.Validator.validateEmail(email)):  #todo, add dob validation when implemented
            try:
                ARTdb = self.openDatabaseConnection()

                cursor = ARTdb.cursor()
                query = "INSERT INTO User (username, password, email, dateOfBirth) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (name, password, email, dob))
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
    
    #Edits a user in the database using the given information
    def editUser(self, id: int, name: str, password: str, email: str, dob: str, pronouns: str, desc: str):
        if (self.Validator.validateNames(name) is None and self.Validator.validatePassword(password) and self.Validator.validateEmail(email)):  #todo, add dob validation when implemented
            try:
                ARTdb = self.openDatabaseConnection()

                cursor = ARTdb.cursor()
                query = "UPDATE User SET username = %s, password = %s, email = %s, dateOfBirth = %s, pronouns = %s, userDescription = %s WHERE id = %s"
                cursor.execute(query, (name, password, email, dob, pronouns, desc, id))
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
    
    #Returns a list of the names of all channels in the database
    def getAllChannels(self):
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
    
    #Returns a list of the names of all channels that the current user is a member of in alphabetical order
    def getYourChannels(self, id: int):
        channels = []
        if (self.Validator.validateInt(id)):
            try:
                ARTdb = self.openDatabaseConnection()
                cursor = ARTdb.cursor()
                query = "SELECT Channel.name FROM Channel JOIN ChannelMember ON Channel.id = ChannelMember.channelId WHERE ChannelMember.userId = %s ORDER BY Channel.name"
                cursor.execute(query, (id,))

                for channel in cursor:
                    channels.append(channel[0])

                cursor.close()
            except mysql.connector.Error as err:
                print(err)
            finally:
                ARTdb.close()
        return channels
    
    #Returns the id and name of a channel matching the given name
    def getChannelByName(self, name: str):
        channel = None
        if (self.Validator.auxValidateString(name)):
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
    
    #Returns a list of the names of all channels that the current user is a member of matching the given search query in alphabetical order
    #TODO: Figure out how to pass a parameter into the field for the LIKE operator
    def searchChannelsByName(self, id: int, name: str):
        channels = []
        if (self.Validator.auxValidateString(name) and self.Validator.validateInt(id)):
            try:
                ARTdb = self.openDatabaseConnection()
                cursor = ARTdb.cursor()
                query = "SELECT Channel.name FROM Channel JOIN ChannelMember ON Channel.id = ChannelMember.channelId WHERE ChannelMember.userId = %s AND Channel.name LIKE '%%s%' ORDER BY Channel.name"
                cursor.execute(query, (id, name))

                for channel in cursor:
                    channels.append(channel[0])

                cursor.close()
            except mysql.connector.Error as err:
                print(err)
            finally:
                ARTdb.close()
        return channels
    
    #Creates a new channel in the database
    def createChannel(self, name: str):
        if (self.Validator.auxValidateString(name)):
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
    
    #Deletes a channel from the database
    def deleteChannel(self, name: str):
        if (self.Validator.auxValidateString(name)):
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
    
    #Returns the given user and channel ids if the database has recorded that the user with the given id is a member of the channel with the given id
    def getChannelMember(self, userId: int, channelId: int):
        member = None
        if (self.Validator.validateInt(userId) and self.Validator.validateInt(channelId)):
            try:
                ARTdb = self.openDatabaseConnection()
                cursor = ARTdb.cursor()
                query = "SELECT userId, channelId FROM ChannelMember WHERE userId = %s AND channelId = %s"
                cursor.execute(query, (userId, channelId))

                for m in cursor:
                    member = m

                cursor.close()
            except mysql.connector.Error as err:
                print(err)
            finally:
                ARTdb.close()
        return member
    
    #Sets the user with the given id as a member of the channel with the given id
    def addUserToChannel(self, userId: int, channelId: int):
        if (self.Validator.validateInt(userId) and self.Validator.validateInt(channelId)):
            try:
                ARTdb = self.openDatabaseConnection()
                cursor = ARTdb.cursor()
                query = "INSERT INTO ChannelMember (userId, channelId) VALUES (%s, %s)"
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
    
    #Sets the user with the given id as not a member of the channel with the given id
    def removeUserFromChannel(self, userId: int, channelId: int):
        if (self.Validator.validateInt(userId) and self.Validator.validateInt(channelId)):
            try:
                ARTdb = self.openDatabaseConnection()
                cursor = ARTdb.cursor()
                query = "DELETE FROM ChannelMember WHERE userId = %s AND channelId = %s"
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
    
    #Returns a list of names of all admins of the given channel
    def getAdminsOfChannel(self, channelId: int):
        admins = []
        if (self.Validator.validateInt(channelId)):
            try:
                ARTdb = self.openDatabaseConnection()
                cursor = ARTdb.cursor()
                query = "SELECT User.username FROM User JOIN Admins ON User.id = Admins.userId WHERE Admins.channelId = %s ORDER BY User.username"
                cursor.execute(query, (channelId,))

                for m in cursor:
                    admins.append(m[0])

                cursor.close()
            except mysql.connector.Error as err:
                print(err)
            finally:
                ARTdb.close()
        return admins
    
    #Returns a list of names of all members of the given channel who are not admins of said channel
    def getNonAdminsOfChannel(self, channelId: int):
        users = []
        if (self.Validator.validateInt(channelId)):
            try:
                ARTdb = self.openDatabaseConnection()
                cursor = ARTdb.cursor()
                query = "SELECT User.username FROM User JOIN ChannelMember ON User.id = ChannelMember.userId WHERE ChannelMember.channelId = %s AND User.username NOT IN (SELECT User.username FROM User JOIN Admins ON User.id = Admins.userId WHERE Admins.channelId = %s) ORDER BY User.username"
                cursor.execute(query, (channelId, channelId))

                for m in cursor:
                    users.append(m[0])

                cursor.close()
            except mysql.connector.Error as err:
                print(err)
            finally:
                ARTdb.close()
        return users
    
    #Returns the given user and channel ids if the database has recorded that the user with the given id is an admin of the channel with the given id
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

    #Sets the user with the given id as an admin of the channel with the given id
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
    
    #Sets the user with the given id as not an admin of the channel with the given id
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
    
    def getMessagesByChannel(self, channelId: int):
        messageData = []
        if (self.Validator.validateInt(channelId)):
            try:
                ARTdb = self.openDatabaseConnection()
                cursor = ARTdb.cursor()
                query = "SELECT User.username, Message.messageTime, Message.messageContent FROM User JOIN Message ON User.id = Message.userId WHERE channelId = %s ORDER BY Message.messageId DESC"
                cursor.execute(query, (channelId,))

                for m in cursor:
                    messageData.append(m)

                cursor.close()
            except mysql.connector.Error as err:
                print(err)
            finally:
                ARTdb.close()
        return messageData
    
    def postMessage(self, userId: int, messageTime: str, channelId: int, messageContent: str):
        if (self.Validator.validateInt(userId) and self.Validator.auxValidateString(messageTime) and self.Validator.validateInt(channelId) and self.Validator.auxValidateString(messageContent)):
            try:
                ARTdb = self.openDatabaseConnection()
                cursor = ARTdb.cursor()
                query = "INSERT INTO Message (userId, messageTime, channelId, messageContent) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (userId, messageTime, channelId, messageContent))
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