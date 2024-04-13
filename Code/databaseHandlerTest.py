from databaseHandler import databaseHandler

Connector = databaseHandler()
failures = 0

def openDatabaseConnectionTest():
    return True if Connector.openDatabaseConnection() is not None else False
if not openDatabaseConnectionTest():
    print("openDatabaseConnectionTest failed")
    failures += 1

def countFromTableTest():
    tables = ["User", "Channel", "DM", "Admins", "ChannelMember", "Message"]
    for table in tables:
        testPass = True if Connector.countFromTable(table) is not None else False
        if not testPass:
            return False
    return True
if not countFromTableTest():
    print("countFromTableTest failed")
    failures += 1


def createUserTest():
    usersBefore = Connector.countFromTable("User")
    if Connector.createUser("testName", "testPass", "test@test.com", "2000-01-01") == False:
        return False
    usersAfter = Connector.countFromTable("User")
    return usersAfter[0] - usersBefore[0] == 1
if not createUserTest():
    print("createUserTest failed")
    failures += 1

def getUsersTest():
    return True if len(Connector.getUsers()) > 0 else False
if not getUsersTest():
    print("getUsersTest failed")
    failures += 1

def getUserByNameTest():
    return True if Connector.getUserByName("testName") is not None else False
if not getUserByNameTest():
    print("getUserByNameTest failed")
    failures += 1

def getUserByIdTest():
    userId = Connector.getUserByName("testName")[0]
    return True if Connector.getUserById(userId) is not None else False
if not getUserByIdTest():
    print("getUserByIdTest failed")
    failures += 1

def validateUserTest():
    return True if Connector.validateUser("testName", "testPass") is not None else False
if not validateUserTest():
    print("validateUserTest failed")
    failures += 1

def editUserTest():
    userId = Connector.getUserByName("testName")[0]
    return Connector.editUser(userId, "testName", "testPass", "test@test.com", "2000-01-01", "testPronouns", "testDesc")
if not editUserTest():
    print("editUserTest failed")
    failures += 1


def createChannelTest():
    channelsBefore = Connector.countFromTable("Channel")
    if Connector.createChannel("testChannel", 0) == False:
        return False
    channelsAfter = Connector.countFromTable("Channel")
    return channelsAfter[0] - channelsBefore[0] == 1
if not createChannelTest():
    print("createChannelTest failed")
    failures += 1

def getChannelByNameTest():
    return True if Connector.getChannelByName("testChannel") is not None else False
if not getChannelByNameTest():
    print("getChannelByNameTest failed")
    failures += 1

def renameChannelTest():
    channelId = Connector.getChannelByName("testChannel")[0]
    return True if Connector.renameChannel(channelId, "testChannel") is not None else False
if not renameChannelTest():
    print("renameChannelTest failed")
    failures += 1

def addUserToChannelTest():
    membersBefore = Connector.countFromTable("ChannelMember")
    userId = Connector.getUserByName("testName")[0]
    channelId = Connector.getChannelByName("testChannel")[0]
    if Connector.addUserToChannel(userId, channelId) == False:
        return False
    membersAfter = Connector.countFromTable("ChannelMember")
    return membersAfter[0] - membersBefore[0] == 1
if not addUserToChannelTest():
    print("addUserToChannelTest failed")
    failures += 1

def getChannelMemberTest():
    userId = Connector.getUserByName("testName")[0]
    channelId = Connector.getChannelByName("testChannel")[0]
    return True if Connector.getChannelMember(userId, channelId) is not None else False
if not getChannelMemberTest():
    print("getChannelMemberTest failed")
    failures += 1

def getAllChannelsTest():
    return True if len(Connector.getAllChannels()) > 0 else False
if not getAllChannelsTest():
    print("getAllChannelsTest failed")
    failures += 1

def getYourChannelsTest():
    userId = Connector.getUserByName("testName")[0]
    return True if len(Connector.getYourChannels(userId)) > 0 else False
if not getYourChannelsTest():
    print("getYourChannelsTest failed")
    failures += 1

def searchChannelsByNameTest():
    userId = Connector.getUserByName("testName")[0]
    return True if len(Connector.searchChannelsByName(userId, "testC")) > 0 else False
if not searchChannelsByNameTest():
    print("searchChannelsByNameTest failed")
    failures += 1

def addAdminTest():
    adminsBefore = Connector.countFromTable("Admins")
    userId = Connector.getUserByName("testName")[0]
    channelId = Connector.getChannelByName("testChannel")[0]
    if Connector.addAdmin(userId, channelId) == False:
        return False
    adminsAfter = Connector.countFromTable("Admins")
    return adminsAfter[0] - adminsBefore[0] == 1
if not addAdminTest():
    print("addAdminTest failed")
    failures += 1

def getAdminByIdTest():
    userId = Connector.getUserByName("testName")[0]
    channelId = Connector.getChannelByName("testChannel")[0]
    return True if Connector.getAdminById(userId, channelId) is not None else False
if not getAdminByIdTest():
    print("getAdminByIdTest failed")
    failures += 1

def getAdminsOfChannelTest():
    channelId = Connector.getChannelByName("testChannel")[0]
    return True if len(Connector.getAdminsOfChannel(channelId)) > 0 else False
if not getAdminsOfChannelTest():
    print("getAdminsOfChannelTest failed")
    failures += 1

def removeAdminTest():
    adminsBefore = Connector.countFromTable("Admins")
    userId = Connector.getUserByName("testName")[0]
    channelId = Connector.getChannelByName("testChannel")[0]
    if Connector.removeAdmin(userId, channelId) == False:
        return False
    adminsAfter = Connector.countFromTable("Admins")
    return adminsAfter[0] - adminsBefore[0] == -1
if not removeAdminTest():
    print("removeAdminTest failed")
    failures += 1

def getNonAdminsOfChannelTest():
    channelId = Connector.getChannelByName("testChannel")[0]
    return True if len(Connector.getNonAdminsOfChannel(channelId)) > 0 else False
if not getNonAdminsOfChannelTest():
    print("getNonAdminsOfChannelTest failed")
    failures += 1


def postMessageTest():
    messagesBefore = Connector.countFromTable("Message")
    userId = Connector.getUserByName("testName")[0]
    channelId = Connector.getChannelByName("testChannel")[0]
    if Connector.postMessage(userId, "2000-01-01", channelId, "test") == False:
        return False
    messagesAfter = Connector.countFromTable("Message")
    return messagesAfter[0] - messagesBefore[0] == 1
if not postMessageTest():
    print("postMessageTest failed")
    failures += 1

def getMessagesByChannelTest():
    channelId = Connector.getChannelByName("testChannel")[0]
    return True if len(Connector.getMessagesByChannel(channelId)) > 0 else False
if not getMessagesByChannelTest():
    print("getMessagesByChannelTest failed")
    failures += 1

def getMessageByIdTest():
    channelId = Connector.getChannelByName("testChannel")[0]
    messageId = Connector.getMessagesByChannel(channelId)[0]
    return True if Connector.getMessageById(messageId) is not None else False
if not getMessageByIdTest():
    print("getMessageByIdTest failed")
    failures += 1

def deleteMessageTest():
    messagesBefore = Connector.countFromTable("Message")
    channelId = Connector.getChannelByName("testChannel")[0]
    messageId = Connector.getMessagesByChannel(channelId)[0]
    if Connector.deleteMessage(messageId) == False:
        return False
    messagesAfter = Connector.countFromTable("Message")
    return messagesAfter[0] - messagesBefore[0] == -1
if not deleteMessageTest():
    print("deleteMessageTest failed")
    failures += 1

def createDMTest():
    DMsBefore = Connector.countFromTable("Message")
    userId = Connector.getUserByName("testName")[0]
    channelId = Connector.getChannelByName("testChannel")[0]
    if Connector.createDM(userId, userId, channelId) == False:
        return False
    DMsAfter = Connector.countFromTable("Message")
    return DMsAfter[0] - DMsBefore[0] == 1
if not createDMTest():
    print("createDMTest failed")
    failures += 1

def getDMTest():
    userId = Connector.getUserByName("testName")[0]
    return True if Connector.getDM(userId, userId) is not None else False
if not getDMTest():
    print("getDMTest failed")
    failures += 1
    

def removeUserFromChannelTest():
    membersBefore = Connector.countFromTable("ChannelMember")
    userId = Connector.getUserByName("testName")[0]
    channelId = Connector.getChannelByName("testChannel")[0]
    if Connector.removeUserFromChannel(userId, channelId) == False:
        return False
    membersAfter = Connector.countFromTable("ChannelMember")
    return membersAfter[0] - membersBefore[0] == -1
if not removeUserFromChannelTest():
    print("removeUserFromChannelTest failed")
    failures += 1

def deleteChannelTest():
    channelsBefore = Connector.countFromTable("Channel")
    if Connector.deleteChannel("testChannel") == False:
        return False
    channelsAfter = Connector.countFromTable("Channel")
    return channelsAfter[0] - channelsBefore[0] == -1
if not deleteChannelTest():
    print("deleteChannelTest failed")
    failures += 1



if failures == 0:
    print("All tests passed")
else:
    print(failures, "tests failed")

