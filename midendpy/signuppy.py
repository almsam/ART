from flask import Blueprint, request, render_template
import re

signup_bp = Blueprint("signup", __name__)


# Define routes
@signup_bp.route("/")
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

    errors = []

    if len(username) <= 8:
        errors.append("Username too short: " + username)
    if password != confirmPassword:
        errors.append("Passwords don't match: " + password + ", " + confirmPassword)
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_regex, email):
        errors.append("Invalid email: " + email)
    year = int(dob[:4]) if len(dob) >= 4 else 9999
    if year >= 2005:
        errors.append("You must be <=18: " + dob)

    if errors:
        return "\n".join(errors)
    else:
        print("Sign up success")
        return (
            "Sign up success, Received username: "
            + username
            + " password: "
            + password
            + " cp: "
            + confirmPassword
            + " email: "
            + email
            + " dob: "
            + dob
        )
