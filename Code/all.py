from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    current_app,
)
import re
from databaseHandler import databaseHandler

Connector = databaseHandler()

app = Flask(__name__)

# Blueprint definitions
admin_bp = Blueprint("admin", __name__)
login_bp = Blueprint("login", __name__)
signup_bp = Blueprint("signup", __name__)
admin_server_bp = Blueprint("admin_server", __name__)
index_bp = Blueprint("index", __name__)


# admin_page(); signup_page(); admin_server_page(); login_page()


@login_bp.route("/")
def login_page():
    return render_template("LogIn.html")


@login_bp.route("/goto_page/<page>")
def goto_page(page):
    if page == "LogIn":
        return render_template("LogIn.html")
    elif page == "SignUp":
        return render_template("SignUp.html")
    elif page == "Admin":
        return render_template("Admin.html")
    elif page == "Index":
        return render_template("Index.html")
    # Add more conditions for other pages as needed
    else:
        return "Page not found"


@index_bp.route("/index")
def index_page():
    return render_template("Index.html")

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


@admin_bp.route("/kick", methods=["POST"])
def kick_user():
    print("Kick user function executed.")
    return "User kicked successfully."


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


@login_bp.route("/process_user", methods=["POST"])
def process_user():
    username = request.form["username"]
    password = request.form["password"]
    print("Received username: ", username, password)
    return "Received username: " + username + password


@login_bp.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    print("Username:", username)
    print("Password:", password)
    if authenticate(username, password):
        # admin_page()
        return redirect(url_for("index.index_page"))
    else:
        return render_template("LogInFail.html")


def authenticate(UN, PW):
    (username, password) = Connector.getUsernameAndPassword(UN, PW)
    if UN is not None and PW is not None:
        if UN == username and PW == password:
            return True
    return False


def invoke_pageAdmin():
    with current_app.test_request_context():
        response = current_app.test_client().get("/admin")
        return response


# Routes and functionalities for signup module
@signup_bp.route("/register", methods=["POST"])
def signup_page():
    return render_template("Registration.html")


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
    #errors = []
    #if len(username) <= 8:
    #    errors.append("Username too short: " + username)
    #if password != confirmPassword:
    #    errors.append("Passwords don't match: " + password + ", " + confirmPassword)
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    #if not re.match(email_regex, email):
    #    errors.append("Invalid email: " + email)
    year = int(dob[:4]) if len(dob) >= 4 else 9999
    #if year >= 2005:
    #    errors.append("You must be >=18: " + dob)
    #if errors:
    if len(username) <= 8 or password != confirmPassword or not re.match(email_regex, email) or year >= 2005:
        #return "\n".join(errors)
        return render_template("RegistrationFail.html")
    else:
        print("Sign up success")
        Connector.createUser(username, password, email, dob)
        return render_template("RegistrationSuccess.html")


# Routes and functionalities for admin_server module
@admin_server_bp.route("/admin_server")
def admin_server_page():
    return render_template("Admin_Server.html")


@admin_server_bp.route("/CreateChannel", methods=["POST"])
def create_channel():
    channelName = request.form.get("ChannelName")
    if not channelName:
        print("Please name the channel.")
        return "Please name the channel."
    else:
        print("Created Channel: ", channelName)
        return "Created Channel: " + channelName


@admin_server_bp.route("/DeleteChannel", methods=["POST"])
def delete_channel():
    channelName = request.form.get("ChannelName")
    if not channelName:
        print("Please name the target channel.")
        return "Please name the target channel."
    else:
        print("Deleted Channel: ", channelName)
        return "Deleted Channel: " + channelName


@admin_server_bp.route("/CreateServer", methods=["POST"])
def create_server():
    serverName = request.form.get("ServerName")
    if not serverName:
        print("Please name the server.")
        return "Please name the server."
    else:
        print("Created Server: ", serverName)
        return "Created Server: " + serverName


@admin_server_bp.route("/DeleteServer", methods=["POST"])
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
app.register_blueprint(admin_server_bp)
app.register_blueprint(index_bp)

if __name__ == "__main__":
    app.run(debug=True)
