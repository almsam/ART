from flask import Flask, request, render_template

app = Flask(__name__, template_folder="html")
channelName = ""
serverName = ""


# Define routes
@app.route("/")
def Admin():
    return render_template("Admin_Server.html")


@app.route("/CreateChannel", methods=["POST"])
def CreateChannel():
    if channelName == "":
        print("Please Name the Channel " + channelName)
        return "Please Name the Channel " + channelName
    else:
        print("Created Channel " + channelName)
        return "Created Channel " + channelName


@app.route("/DeleteChannel", methods=["POST"])
def DeleteChannel():
    print("Unmute user function executed.")
    return "User unmuted successfully."


@app.route("/kick", methods=["POST"])
def kick_user():
    print("Kick user function executed.")
    return "User kicked successfully."


@app.route("/ban", methods=["POST"])
def ban_user():
    print("Ban user function executed.")
    return "User banned successfully."


@app.route("/unban", methods=["POST"])
def unban_user():
    print("Unban user function executed.")
    return "User unbanned successfully."


@app.route("/edit_roles", methods=["POST"])
def edit_user_roles():
    print("Edit user roles function executed.")
    return "User roles edited successfully."


@app.route("/process_user", methods=["POST"])
def process_user():
    global username
    username = request.form["username"]  # Get the username from the form data
    print("Received username:", username)  # Print the received username
    # Perform any processing with the username here
    return "Received username: " + username


if __name__ == "__main__":
    app.run(debug=True)
