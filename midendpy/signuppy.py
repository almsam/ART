from flask import Flask, request, render_template
import re

app = Flask(__name__, template_folder="html")
username = ""
Password = ""
confirmPassword = ""
email = ""
dob = ""

a = False
b = False
c = False
d = False


# Define routes
@app.route("/")
def Admin():
    return render_template("Registration.html")


@app.route("/signup", methods=["POST"])
def login():
    global username
    username = request.form["username"]  # Get the username from the form data
    global password
    password = request.form["password"]
    global confirmPassword
    confirmPassword = request.form["confirmPassword"]
    global email
    email = request.form["email"]
    global dob
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

    if len(username) > 8:
        a = True
    if password == confirmPassword:
        b = True
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(email_regex, email):
        c = True
    if int(dob[:4]) < 2005:
        d = True

    if a == False:
        print("Username too short:", username)
        return "username too short: " + username
    elif b == False:
        print("Passwords don't match:", password, ",", confirmPassword)
        return "passwords dont match: " + password + ", " + confirmPassword
    elif c == False:
        print("Email invalid:", email)
        return "email invalid: " + email
    elif a == False:
        print("You must be >18:", dob)
        return "you must be >18: " + dob
    else:
        print("sign up success")
        return (
            "login success, Received username: "
            + username
            + " password: "
            + password
            + " cp: "
            + confirmPassword
            + "email: "
            + email
            + " dob: "
            + dob
        )


if __name__ == "__main__":
    app.run(debug=True)
