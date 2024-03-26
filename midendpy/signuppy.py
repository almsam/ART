from flask import Flask, request, render_template

app = Flask(__name__, template_folder="html")
username = ""
Password = ""
confirmPassword = ""
email = ""
dob = ""


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

    return (
        "Received username: "
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
