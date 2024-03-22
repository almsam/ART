from flask import Flask, request, render_template

app = Flask(__name__, template_folder="html")
username = ""
password = ""


# Define routes
@app.route("/")
def Admin():
    return render_template("LogIn.html")


@app.route("/process_user", methods=["POST"])
def process_user():
    global username
    username = request.form["username"]  # Get the username from the form data
    global password
    password = request.form["password"]
    print("Received username: ", username, password)  # Print the received username
    # Perform any processing with the username here
    return "Received username: " + username + password


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    print("Username:", username)
    print("Password:", password)
    # Perform authentication logic here
    return "Received username: " + username + ", password: " + password


if __name__ == "__main__":
    app.run(debug=True)
