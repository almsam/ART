from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    current_app,
)
from databaseHandler import databaseHandler
from validation import parameterValidator
from loggedInUser import loggedInUser
from datetime import datetime

Connector = databaseHandler()
Validator = parameterValidator()

app = Flask(__name__)

# Blueprint definitions
admin_bp = Blueprint("admin", __name__)
login_bp = Blueprint("login", __name__)
edit_profile_bp = Blueprint("edit_profile", __name__)
signup_bp = Blueprint("signup", __name__)
server_bp = Blueprint("server", __name__)
channel_bp = Blueprint("channel", __name__)
profile_bp = Blueprint("profile", __name__)

currentUser = loggedInUser()

@login_bp.route("/goto_page/<page>")
def goto_page(page):
    if page == "LogIn":
        return render_template("LogIn.html")
    elif page == "SignUp":
        return render_template("SignUp.html")
    elif page == "Edit":
        return render_template("Edit.html")
    elif page == "Admin":
        return render_template("Admin.html")
    elif page == "Server":
        return render_template("Server.html")
    elif page == "Channel":
        return render_template("Channel.html")
    elif page == "Registration":
        return render_template("Registration.html")
    # Add more conditions for other pages as needed
    else:
        return "Page not found"


#---Login page---

#Main page is login page
@login_bp.route("/")
def login_page():
    return render_template("LogIn.html")

#Log user in using the given username and password and redirect to server page, or else print error message
@login_bp.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    print("Username:", username)
    print("Password:", password)
    currentUser.id = authenticate(username, password)
    if currentUser.id is not None: #Store current user Id while logged in
        print(currentUser.id)
        return redirect(url_for("server.server_page"))
    else:
        print("Login fail")
        return render_template("LogInFail.html")

#Log out user and return to login page
@login_bp.route("/logout", methods=["POST"])
def logout():
    currentUser.id = None #Reset current user Id
    return redirect(url_for("login.login_page"))

#Helper method to check username and password
def authenticate(UN, PW) -> bool:
    return Connector.validateUser(UN, PW)



#---Registration and profile editing pages---

#Registration page with no errors the first time
@signup_bp.route("/register", methods=["POST"])
def signup_page():
    return render_template("Registration.html")

#Register user with the given information, and reload page with a message saying whether or not registration was successful
@signup_bp.route("/signup", methods=["POST"])
def signup():
    username = request.form["username"]
    password = request.form["password"]
    confirmPassword = request.form["confirmPassword"]
    email = request.form["email"]
    dob = request.form["dob"]
    print(
        "Received username:",
        username,
        " password*2: ",
        password,
        confirmPassword,
        " email: ",
        email,
        " dob: ",
        dob,
    )
    print("attempting to authenticate:")

    errors = profileErrors(username, "", password, confirmPassword, email, dob)

    if not errors:
        print("Sign up success")
        Connector.createUser(username, password, email, dob)
    return render_template("RegistrationCheck.html", errors=errors)

#Profile editing page with no errors the first time, fields are filled in with user's current information
@edit_profile_bp.route("/edit_profile")
def edit_profile_page():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))
    
    username = Connector.getUserById(currentUser.id)[1]
    password = Connector.getUserById(currentUser.id)[2]
    email = Connector.getUserById(currentUser.id)[3]
    dob = Connector.getUserById(currentUser.id)[4]
    pronouns = "" if Connector.getUserById(currentUser.id)[5] is None else Connector.getUserById(currentUser.id)[5]
    desc = "" if Connector.getUserById(currentUser.id)[6] is None else Connector.getUserById(currentUser.id)[6]
    return render_template("Edit.html", username=username, password=password, email=email, dob=dob, pronouns=pronouns, desc=desc)

#Edit user with the given information, and reload page with a message saying whether or not edit was successful
@edit_profile_bp.route("/edited_profile", methods=["POST"])
def edit_profile():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))

    username = request.form["username"]
    password = request.form["password"]
    confirmPassword = request.form["confirmPassword"]
    email = request.form["email"]
    dob = request.form["dob"]
    pronouns = request.form["pronouns"]
    desc = request.form["desc"]

    oldUsername = Connector.getUserById(currentUser.id)[1]
    errors = profileErrors(username, oldUsername, password, confirmPassword, email, dob)

    if not errors:
        Connector.editUser(currentUser.id, username, password, email, dob, pronouns, desc)

        username = Connector.getUserById(currentUser.id)[1]
        password = Connector.getUserById(currentUser.id)[2]
        email = Connector.getUserById(currentUser.id)[3]
        dob = Connector.getUserById(currentUser.id)[4]
        pronouns = "" if Connector.getUserById(currentUser.id)[5] is None else Connector.getUserById(currentUser.id)[5]
        desc = "" if Connector.getUserById(currentUser.id)[6] is None else Connector.getUserById(currentUser.id)[6]
    return render_template("EditCheck.html", username=username, password=password, email=email, dob=dob, pronouns=pronouns, desc=desc, errors=errors)

#Helper method to record registration/profile editing errors
def profileErrors(username, oldUsername, password, confirmPassword, email, dob):
    errors = []

    nameConfirm = Validator.validateNames(username)
    if nameConfirm != None: #no error if None
        errors.append(nameConfirm + username)   #returns whether too long or short
        
    if username != oldUsername and username in Connector.getUsers():
        errors.append("Username is already taken: " + username)
    
    if password != confirmPassword:
        errors.append("Passwords do not match.")

    if not Validator.validateEmail(email):
        errors.append("Invalid email: " + email)

    if not Validator.validateAge(dob):
        errors.append("Your age is too young: " + dob)
    
    return errors



#---Server page---

#Main server page with list of your channels and all members on the server
@server_bp.route("/server")
def server_page():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))

    username = Connector.getUserById(currentUser.id)[1]
    users = Connector.getUsers()
    channels = Connector.getYourChannels(currentUser.id)
    return render_template("Server.html", username=username, users=users, channels=channels)

#Only show channels matching the search query
@server_bp.route("/search_channel", methods=["POST"])
def search_channel():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))

    username = Connector.getUserById(currentUser.id)[1]
    users = Connector.getUsers()
    channelName = request.form["channelName"]
    channels = Connector.searchChannelsByName(currentUser.id, channelName)
    message = "Returned channels matching search query: " + channelName + "."
    return render_template("ServerCheck.html", username=username, users=users, channels=channels, message=message)

#Add a channel, set yourself as a member and admin, and update the channel list
@server_bp.route("/create_channel", methods=["POST"])
def create_channel():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))

    username = Connector.getUserById(currentUser.id)[1]
    users = Connector.getUsers()
    channelName = request.form["channelName"]
    channels = Connector.getAllChannels()

    if channelName in channels:
        message = "Channel " + channelName + " already exists."
    else:
        Connector.createChannel(channelName, 0)
        channelId = Connector.getChannelByName(channelName)[0]
        Connector.addUserToChannel(currentUser.id, channelId)
        Connector.addAdmin(currentUser.id, channelId)
        message = "Channel " + channelName + " successfully created. You are now the admin of this channel."

    channels = Connector.getYourChannels(currentUser.id)
    return render_template("ServerCheck.html", username=username, users=users, channels=channels, message=message)

#Delete a channel, remove yourself as a member and admin, and update the channel list
@server_bp.route("/delete_channel", methods=["POST"])
def delete_channel():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))

    username = Connector.getUserById(currentUser.id)[1]
    users = Connector.getUsers()
    channelName = request.form["channelName"]
    channels = Connector.getAllChannels()
    channelInfo = Connector.getChannelByName(channelName)
    
    if channelInfo is None:
        message = "Channel " + channelName + " does not exist."
    else:
        adminStatus = Connector.getAdminById(currentUser.id, channelInfo[0])
        if adminStatus is None:
            message = "Cannot delete " + channelName + " as you are not an admin of this channel."
        else:
            Connector.removeUserFromChannel(currentUser.id, channelInfo[0])
            Connector.removeAdmin(currentUser.id, channelInfo[0])
            Connector.deleteChannel(channelName)
            message = "Channel " + channelName + " successfully deleted."

    channels = Connector.getYourChannels(currentUser.id)
    return render_template("ServerCheck.html", username=username, users=users, channels=channels, message=message)

#Add the given user to the given channel, which will appear in their channel list
@server_bp.route("/add_user", methods=["POST"])
def add_user():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))

    username = Connector.getUserById(currentUser.id)[1]
    users = Connector.getUsers()
    userToAdd = request.form["userToAdd"]
    userInfo = Connector.getUserByName(userToAdd)
    channelName = request.form["channel"]
    channelInfo = Connector.getChannelByName(channelName)
    channels = Connector.getAllChannels()

    if channelInfo is None:
        message = "Channel " + channelName + " does not exist."
    elif userInfo is None:
        message = "User " + userToAdd + " does not exist."
    else:
        currentMember = Connector.getChannelMember(userInfo[0], channelInfo[0])
        if currentMember is not None:
            message = "User " + userToAdd + " is already a member of this channel."
        else:
            Connector.addUserToChannel(userInfo[0], channelInfo[0])
            message = "User " + userToAdd + " successfully added to channel " + channelName + "."
    
    channels = Connector.getYourChannels(currentUser.id)
    return render_template("ServerCheck.html", username=username, users=users, channels=channels, message=message)

#Remove yourself from a channel and update the channel list
@server_bp.route("/leave_channel", methods=["POST"])
def leave_channel():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))

    username = Connector.getUserById(currentUser.id)[1]
    users = Connector.getUsers()
    channelName = request.form["channel"]
    channelInfo = Connector.getChannelByName(channelName)

    if channelInfo is None:
        message = "Channel " + channelName + " does not exist."
    else:
        admins = Connector.getAdminsOfChannel(channelInfo[0])
        print(admins)
        if len(admins) == 1 and username in admins:
            message = "Cannot leave this channel as you are the only admin of this channel."
        else:
            Connector.removeUserFromChannel(currentUser.id, channelInfo[0])
            Connector.removeAdmin(currentUser.id, channelInfo[0])
            message = "You have left the channel " + channelName + ". To rejoin, you must be added back in by a member of that channel."
    
    channels = Connector.getYourChannels(currentUser.id)
    return render_template("ServerCheck.html", username=username, users=users, channels=channels, message=message)

#Rename a channel that you own and update the channel list
@server_bp.route("/rename_channel", methods=["POST"])
def rename_channel():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))

    username = Connector.getUserById(currentUser.id)[1]
    users = Connector.getUsers()
    channelName = request.form["channel"]
    newChannelName = request.form["newChannelName"]
    channelInfo = Connector.getChannelByName(channelName)

    if channelInfo is None:
        message = "Channel " + channelName + " does not exist."
    elif newChannelName is None:
        message = "Name not specified."
    else:
        adminStatus = Connector.getAdminById(currentUser.id, channelInfo[0])
        if adminStatus is None:
            message = "Cannot rename this channel as you are not an admin of this channel."
        else:
            Connector.renameChannel(channelInfo[0], newChannelName)
            message = "Renamed channel to " + newChannelName + "."
    
    channels = Connector.getYourChannels(currentUser.id)
    return render_template("ServerCheck.html", username=username, users=users, channels=channels, message=message)



#---Profile and direct messaging pages---

#View the profile of another user
@profile_bp.route("/profile", methods=["POST"])
def profile_page():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))
    
    username = Connector.getUserById(currentUser.id)[1]
    other = Connector.getUserByName(request.form["other"])

    if other is None:
        message = "User does not exist."
        users = Connector.getUsers()
        channels = Connector.getYourChannels(currentUser.id)
        return render_template("ServerCheck.html", username=username, users=users, channels=channels, message=message)
    else:
        othername = other[1]
        pronouns = other[5]
        desc = other[6]
        return render_template("Profile.html", username=username, othername=othername, pronouns=pronouns, desc=desc)
    
@channel_bp.route("/dm", methods=["POST"])
def dm():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))
    
    user = Connector.getUserById(currentUser.id)
    username = user[1]
    other = Connector.getUserByName(request.form["other"])

    if other is None:
        message = "User does not exist."
        users = Connector.getUsers()
        channels = Connector.getYourChannels(currentUser.id)
        return render_template("ServerCheck.html", username=username, users=users, channels=channels, message=message)
    elif user[0] == other[0]:
        message = "You cannot direct message yourself."
        othername = other[1]
        pronouns = other[5]
        desc = other[6]
        return render_template("ProfileDMError.html", username=username, othername=othername, pronouns=pronouns, desc=desc, message=message)
    elif not (Connector.getDM(user[0], other[0]) or Connector.getDM(other[0], user[0])):
        tempName = str(datetime.now())
        Connector.createChannel(tempName, 1)
        channelId = Connector.getChannelByName(tempName)[0]
        Connector.renameChannel(channelId, "Direct Message")
        Connector.addUserToChannel(user[0], channelId)
        Connector.addUserToChannel(other[0], channelId)
        Connector.createDM(user[0], other[0], channelId)

    channelId = Connector.getDM(user[0], other[0])[2] if Connector.getDM(user[0], other[0]) is not None else Connector.getDM(other[0], user[0])[2]
    return loadChannel(username, "Direct Message", channelId)



#---Channel page---

#Channel page with messages and list of members grouped by admin and non-admin
@channel_bp.route("/channel", methods=["POST"])
def channel_page():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))

    username = Connector.getUserById(currentUser.id)[1]
    channel = request.form["channel"]
    channelInfo = Connector.getChannelByName(channel)
    if channelInfo is None:
        return redirect(url_for("server.server_page"))
    else:
        return loadChannel(username, channel, channelInfo[0])

#Remove the given user from this channel, but only if you are an admin
@channel_bp.route("/ban", methods=["POST"])
def ban():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))

    username = Connector.getUserById(currentUser.id)[1]
    channel = request.form["channel"]
    channelInfo = Connector.getChannelByName(channel)
    userToBan = request.form["user"]
    userInfo = Connector.getUserByName(userToBan)

    if channelInfo is None:
        return redirect(url_for("server.server_page"))
    elif userInfo is None:
        message = "User " + userToBan + " does not exist in this channel."
    elif userInfo[0] == currentUser.id:
        message = "Cannot ban yourself. To leave this channel, please do so from the Server page." #TODO: Add method to leave a channel
    else:
        adminStatus = Connector.getAdminById(currentUser.id, channelInfo[0])
        if adminStatus is None:
            message = "Cannot ban this user as you are not an admin of this channel."
        else:
            Connector.removeUserFromChannel(userInfo[0], channelInfo[0])
            Connector.removeAdmin(userInfo[0], channelInfo[0])
            message = "User " + userToBan + " banned successfully. To unban them, they must be added back to the channel."
    
    return reloadChannel(username, channel, channelInfo[0], message)

#Unset the given user as an admin, but only if you are an admin and are not unsetting yourself when you are the only admin
@channel_bp.route("/remove_admin", methods=["POST"])
def remove_admin():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))

    username = Connector.getUserById(currentUser.id)[1]
    channel = request.form["channel"]
    channelInfo = Connector.getChannelByName(channel)
    userToUnset = request.form["user"]
    userInfo = Connector.getUserByName(userToUnset)

    if channelInfo is None:
        return redirect(url_for("server.server_page"))
    elif userInfo is None:
        message = "User " + userToUnset + " does not exist in this channel."
    else:
        adminStatus = Connector.getAdminById(currentUser.id, channelInfo[0])
        if adminStatus is None:
            message = "Cannot unset this user as admin as you are not an admin of this channel."
        elif len(Connector.getAdminsOfChannel(channelInfo[0])) == 1:
            message = "Cannot unset yourself as admin as you are the only admin of this channel."
        else:
            Connector.removeAdmin(userInfo[0], channelInfo[0])
            message = "User " + userToUnset + " has been unset as an admin."
    
    return reloadChannel(username, channel, channelInfo[0], message)

#Set the given user as an admin, but only if you are an admin
@channel_bp.route("/add_admin", methods=["POST"])
def add_admin():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))

    username = Connector.getUserById(currentUser.id)[1]
    channel = request.form["channel"]
    channelInfo = Connector.getChannelByName(channel)
    userToSet = request.form["user"]
    userInfo = Connector.getUserByName(userToSet)

    if channelInfo is None:
        return redirect(url_for("server.server_page"))
    elif userInfo is None:
        message = "User " + userToSet + " does not exist in this channel."
    else:
        adminStatus = Connector.getAdminById(currentUser.id, channelInfo[0])
        if adminStatus is None:
            message = "Cannot set this user as admin as you are not an admin of this channel."
        else:
            Connector.addAdmin(userInfo[0], channelInfo[0])
            message = "User " + userToSet + " has been set as an admin."
    
    return reloadChannel(username, channel, channelInfo[0], message)

#Post a message to the channel with your username and timestamp beside it
@channel_bp.route("/post_message", methods=["POST"])
def post_message():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))

    username = Connector.getUserById(currentUser.id)[1]
    channel = request.form["channel"]
    chat = request.form["message-box"]
    channelInfo = Connector.getChannelByName(channel)
    if channelInfo is None:
        return redirect(url_for("server.server_page"))
    elif chat is None:
        message = "Message failed."
    else:
        timestamp = Validator.convertDatetime(str(datetime.now()))
        Connector.postMessage(currentUser.id, timestamp, channelInfo[0], chat)
        message = "Message posted."
        
    return reloadChannel(username, channel, channelInfo[0], message)
    
#Delete a message from a channel, but only if you wrote it or are an admin
@channel_bp.route("/delete_message", methods=["POST"])
def delete_message():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))

    username = Connector.getUserById(currentUser.id)[1]
    channel = request.form["channel"]
    messageId = int(request.form["messageId"])
    messageInfo = Connector.getMessageById(messageId)
    print(messageInfo)
    channelInfo = Connector.getChannelByName(channel)
    if channelInfo is None:
        return redirect(url_for("server.server_page"))
    elif messageInfo is None:
        message = "Message does not exist."
    else:
        adminStatus = Connector.getAdminById(currentUser.id, channelInfo[0])
        if adminStatus is None and currentUser.id != messageInfo[1]:
            message = "Cannot delete a message you did not post unless you are an admin."
        else:
            Connector.deleteMessage(messageId)
            message = "Message deleted."
        
    return reloadChannel(username, channel, channelInfo[0], message)

def loadChannel(username, channel, channelId):
    chats = []
    messageData = Connector.getMessagesByChannel(channelId)
    for m in messageData:
        chats.append([m[0], str(m[1]) + " (" + str(m[2]) + "): " + str(m[3])])
    admins = Connector.getAdminsOfChannel(channelId)
    users = Connector.getNonAdminsOfChannel(channelId)
    return render_template("Channel.html", username=username, channel=channel, admins=admins, users=users, chats=chats)
    
def reloadChannel(username, channel, channelId, message):
    chats = []
    messageData = Connector.getMessagesByChannel(channelId)
    for m in messageData:
        chats.append([m[0], str(m[1]) + " (" + str(m[2]) + "): " + str(m[3])])
    admins = Connector.getAdminsOfChannel(channelId)
    users = Connector.getNonAdminsOfChannel(channelId)
    return render_template("ChannelCheck.html", username=username, channel=channel, admins=admins, users=users, chats=chats, message=message)



# Register blueprints
app.register_blueprint(admin_bp)
app.register_blueprint(login_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(edit_profile_bp)
app.register_blueprint(server_bp)
app.register_blueprint(channel_bp)
app.register_blueprint(profile_bp)

if __name__ == "__main__":
    app.run(debug=True)
