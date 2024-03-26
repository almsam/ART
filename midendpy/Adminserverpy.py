from flask import Flask, request, render_template

app = Flask(__name__, template_folder="html")
channelName = ""
serverName = ""


# Define routes
@app.route("/")
def Admin_Server():
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


@app.route("/subChannelName", methods=["POST"])
def process_cname():
    global channelName
    channelName = request.form["ChannelName"]  # Get the username from the form data
    print("Received channel Name:", channelName)  # Print the received username
    # Perform any processing with the username here
    return "Received channel Name: " + channelName


@app.route("/subChannelName", methods=["POST"])
def process_sname():
    global serverName
    serverName = request.form["ServerName"]  # Get the username from the form data
    print("Received channel Name:", serverName)  # Print the received username
    # Perform any processing with the username here
    return "Received channel Name: " + serverName


if __name__ == "__main__":
    app.run(debug=True)
