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

Connector = databaseHandler()
Validator = parameterValidator()

app = Flask(__name__)

# Blueprint definitions
admin_bp = Blueprint("admin", __name__)
login_bp = Blueprint("login", __name__)
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
    elif page == "Admin":
        return render_template("Admin.html")
    elif page == "Server":
        return render_template("Server.html")
    elif page == "Channel":
        return render_template("Channel.html")
    # Add more conditions for other pages as needed
    else:
        return "Page not found"


#Login and logout
@login_bp.route("/") #Main page is login page
def login_page():
    return render_template("LogIn.html")
    
@login_bp.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    print("Username:", username)
    print("Password:", password)
    currentUser.id = authenticate(username, password)
    if currentUser.id is not None:
        print(currentUser.id)
        return redirect(url_for("server.server_page"))
    else:
        print("Login fail")
        return render_template("LogInFail.html")
    
@login_bp.route("/logout", methods=["POST"])
def logout():
    currentUser.id = None
    return redirect(url_for("login.login_page"))

@login_bp.route("/process_user", methods=["POST"])
def process_user():
    username = request.form["username"]
    password = request.form["password"]
    print("Received username: ", username, password)
    return "Received username: " + username + password

def authenticate(UN, PW) -> bool:
    return Connector.validateUser(UN, PW)



#Registration and profile editing
@signup_bp.route("/register", methods=["POST"])
def signup_page():
    errors = None
    return render_template("Registration.html", errors=errors)

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

    errors = []

    nameConfirm = Validator.validateNames(username)
    if nameConfirm != None: #no error if None
        errors.append(nameConfirm + username)   #returns whether too long or short

    if username in Connector.getUsers():
        errors.append("Username is already taken: " + username)
        
    if password != confirmPassword:
        errors.append("Passwords do not match.")

    if not Validator.validateEmail(email):
        errors.append("Invalid email: " + email)

    if not Validator.validateAge(dob):
        errors.append("Your age is too young: " + dob)

    if not errors:
        print("Sign up success")
        Connector.createUser(username, password, email, dob)
    return render_template("RegistrationCheck.html", errors=errors)

@profile_bp.route("/profile")
def profile_page():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))
    else:
        username = Connector.getUserById(currentUser.id)[1]
        password = Connector.getUserById(currentUser.id)[2]
        email = Connector.getUserById(currentUser.id)[3]
        dob = Connector.getUserById(currentUser.id)[4]
        pronouns = "" if Connector.getUserById(currentUser.id)[5] is None else Connector.getUserById(currentUser.id)[5]
        desc = "" if Connector.getUserById(currentUser.id)[6] is None else Connector.getUserById(currentUser.id)[6]
        return render_template("Profile.html", username=username, password=password, email=email, dob=dob, pronouns=pronouns, desc=desc)
    
@profile_bp.route("/editprofile", methods=["POST"])
def edit_profile():   #todo, refactor
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))
    else:
        username = request.form["username"]
        password = request.form["password"]
        confirmPassword = request.form["confirmPassword"]
        email = request.form["email"]
        dob = request.form["dob"]
        pronouns = request.form["pronouns"]
        desc = request.form["desc"]

        errors = []

        nameConfirm = Validator.validateNames(username)
        if nameConfirm != None: #no error if None
            errors.append(nameConfirm + username)   #returns whether too long or short
        
        oldUsername = Connector.getUserById(currentUser.id)[1]
        if username != oldUsername and username in Connector.getUsers():
            errors.append("Username is already taken: " + username)
    
        if password != confirmPassword:
            errors.append("Passwords do not match.")

        if not Validator.validateEmail(email):
            errors.append("Invalid email: " + email)

        if not Validator.validateAge(dob):
            errors.append("Your age is too young: " + dob)

        if not errors:
            Connector.editUser(currentUser.id, username, password, email, dob, pronouns, desc)

            username = Connector.getUserById(currentUser.id)[1]
            password = Connector.getUserById(currentUser.id)[2]
            email = Connector.getUserById(currentUser.id)[3]
            dob = Connector.getUserById(currentUser.id)[4]
            pronouns = "" if Connector.getUserById(currentUser.id)[5] is None else Connector.getUserById(currentUser.id)[5]
            desc = "" if Connector.getUserById(currentUser.id)[6] is None else Connector.getUserById(currentUser.id)[6]
            return render_template("ProfileCheck.html", username=username, password=password, email=email, dob=dob, pronouns=pronouns, desc=desc, errors=errors)
        else:
            return redirect(url_for("login.login_page"))



#Server page
@server_bp.route("/server")
def server_page():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))
    else:
        username = Connector.getUserById(currentUser.id)[1]
        users = Connector.getUsers()
        channels = Connector.getYourChannels(currentUser.id)
        return render_template("Server.html", username=username, users=users, channels=channels)
    
@server_bp.route("/search_channel", methods=["POST"])
def search_channel():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))
    else:
        username = Connector.getUserById(currentUser.id)[1]
        users = Connector.getUsers()
        channelName = request.form["channelName"]
        channels = Connector.searchChannelsByName(currentUser.id, channelName)
        message = "Returned channels matching search query: " + channelName + "."
        return render_template("ServerCheck.html", username=username, users=users, channels=channels, message=message)
    
@server_bp.route("/create_channel", methods=["POST"])
def create_channel():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))
    else:
        username = Connector.getUserById(currentUser.id)[1]
        users = Connector.getUsers()
        channelName = request.form["channelName"]
        channels = Connector.getAllChannels()

        if channelName in channels:
            message = "Channel " + channelName + " already exists."
        else:
            Connector.createChannel(channelName)
            channelId = Connector.getChannelByName(channelName)[0]
            Connector.addUserToChannel(currentUser.id, channelId)
            Connector.addAdmin(currentUser.id, channelId)
            message = "Channel " + channelName + " successfully created. You are now the admin of this channel."

        channels = Connector.getYourChannels(currentUser.id)
        return render_template("ServerCheck.html", username=username, users=users, channels=channels, message=message)

@server_bp.route("/delete_channel", methods=["POST"])
def delete_channel():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))
    else:
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
    
@server_bp.route("/add_user", methods=["POST"])
def add_user():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))
    else:
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
    


#Channel page
@channel_bp.route("/channel", methods=["POST"])
def index_page():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))
    else:
        username = Connector.getUserById(currentUser.id)[1]
        channel = request.form["channel"]
        channelInfo = Connector.getChannelByName(channel)
        if channelInfo is None:
            return redirect(url_for("server.server_page"))
        else:
            admins = Connector.getAdminsOfChannel(channelInfo[0])
            users = Connector.getNonAdminsOfChannel(channelInfo[0])
            return render_template("Channel.html", username=username, channel=channel, admins=admins, users=users)
        
@channel_bp.route("/kick", methods=["POST"])
def kick():
    if currentUser.id is None:
        return redirect(url_for("login.login_page"))
    else:
        username = Connector.getUserById(currentUser.id)[1]
        channel = request.form["channel"]
        channelInfo = Connector.getChannelByName(channel)
        userToKick = request.form["user"]
        userInfo = Connector.getUserByName(userToKick)

        if channelInfo is None:
            return redirect(url_for("server.server_page"))
        elif userInfo is None:
            message = "User " + userToKick + " does not exist in this channel."
        elif userInfo[0] == currentUser.id:
            message = "Cannot kick yourself. To leave this channel, please do so from the Server page."
        else:
            adminStatus = Connector.getAdminById(currentUser.id, channelInfo[0])
            if adminStatus is None:
                message = "Cannot kick this user as you are not an admin of this channel."
            else:
                Connector.removeUserFromChannel(userInfo[0], channelInfo[0])
                Connector.removeAdmin(userInfo[0], channelInfo[0])
                message = "User " + userToKick + " kicked successfully."
        
        admins = Connector.getAdminsOfChannel(channelInfo[0])
        users = Connector.getNonAdminsOfChannel(channelInfo[0])
        return render_template("ChannelCheck.html", username=username, channel=channel, admins=admins, users=users, message=message)



# Routes and functionalities for admin module
@admin_bp.route("/admin")
def admin_page():
    return render_template("Admin.html")

@admin_bp.route("/mute", methods=["POST"])
def mute_user():
    print("Mute user function executed.")
    return "User muted successfully."

@admin_bp.route("/unmute", methods=["POST"])
def unmute_user():
    print("Unmute user function executed.")
    return "User unmuted successfully."

#@admin_bp.route("/kick", methods=["POST"])
#def kick_user():
#    print("Kick user function executed.")
#    return "User kicked successfully."

@admin_bp.route("/ban", methods=["POST"])
def ban_user():
    print("Ban user function executed.")
    return "User banned successfully."

@admin_bp.route("/unban", methods=["POST"])
def unban_user():
    print("Unban user function executed.")
    return "User unbanned successfully."

@admin_bp.route("/edit_roles", methods=["POST"])
def edit_user_roles():
    print("Edit user roles function executed.")
    return "User roles edited successfully."

@admin_bp.route("/process_user_admin", methods=["POST"])
def process_user_admin():
    username = request.form.get("username")
    if not username:
        return "Please provide a username."
    else:
        print("Received username:", username)
        return "Received username: " + username


# Routes and functionalities for login module






def invoke_pageAdmin():
    with current_app.test_request_context():
        response = current_app.test_client().get("/admin")
        return response








@server_bp.route("/CreateServer", methods=["POST"])
def create_server():
    serverName = request.form.get("ServerName")
    if not serverName:
        print("Please name the server.")
        return "Please name the server."
    else:
        print("Created Server: ", serverName)
        return "Created Server: " + serverName


@server_bp.route("/DeleteServer", methods=["POST"])
def delete_server():
    serverName = request.form.get("ServerName")
    if not serverName:
        print("Please name the target server.")
        return "Please name the target server."
    else:
        print("Deleted Server: ", serverName)
        return "Deleted Server: " + serverName
    



# Register blueprints
app.register_blueprint(admin_bp)
app.register_blueprint(login_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(server_bp)
app.register_blueprint(channel_bp)
app.register_blueprint(profile_bp)

if __name__ == "__main__":
    app.run(debug=True)
