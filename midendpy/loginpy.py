from flask import Blueprint, request, redirect, url_for, render_template
from flask import current_app

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

    if authenticate(request.form["username"], request.form["password"]):
        # Redirect to the admin page upon successful login
        # print(render_template("admin.html"))
        # app.pageAdmin()
        invoke_pageAdmin()
        return render_template("admin.html")
        # return redirect(url_for("admin.admin_page"))
    else:
        # Return some response for unsuccessful login
        return "Login failed. Please try again."

    return "Received username: " + username + ", password: " + password


def authenticate(UN, PW):
    if UN == "ss":
        if PW == "ss":
            return True
    return False


def invoke_pageAdmin():
    with current_app.test_request_context():
        response = current_app.test_client().get("/pageAdmin")
        # Process the response if needed
        return response
