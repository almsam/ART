from flask import Blueprint, request, render_template

login_bp = Blueprint("login", __name__)


# Define routes
@login_bp.route("/")
def login_page():
    return render_template("LogIn.html")


@login_bp.route("/process_user", methods=["POST"])
def process_user():
    username = request.form["username"]
    password = request.form["password"]
    print("Received username: ", username, password)
    # Perform any processing with the username here
    return "Received username: " + username + password


@login_bp.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    print("Username:", username)
    print("Password:", password)
    # Perform authentication logic here
    return "Received username: " + username + ", password: " + password
