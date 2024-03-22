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
    if channelName == "":
        print("Please Name the target Channel " + channelName)
        return "Please Name the target Channel " + channelName
    else:
        print("Deleted Channel " + channelName)
        return "Deleted Channel " + channelName


@app.route("/CreateServer", methods=["POST"])
def CreateServer():
    if serverName == "":
        print("Please Name the Server " + serverName)
        return "Please Name the Server " + serverName
    else:
        print("Created Server " + serverName)
        return "Created Server " + serverName


@app.route("/DeleteServer", methods=["POST"])
def DeleteServer():
    if serverName == "":
        print("Please Name the target Server " + serverName)
        return "Please Name the target Server " + serverName
    else:
        print("Deleted Server " + serverName)
        return "Deleted Server " + serverName


@app.route("/process_user", methods=["POST"])
def process_user():
    global username
    username = request.form["username"]  # Get the username from the form data
    print("Received username:", username)  # Print the received username
    # Perform any processing with the username here
    return "Received username: " + username


if __name__ == "__main__":
    app.run(debug=True)
