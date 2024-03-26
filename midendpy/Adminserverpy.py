from flask import Blueprint, request, render_template

admin_server_bp = Blueprint("admin_server", __name__)

channelName = ""
serverName = ""


# Define routes
@admin_server_bp.route("/admin_server")
def admin_server_page():
    return render_template("Admin_Server.html")


@admin_server_bp.route("/CreateChannel", methods=["POST"])
def create_channel():
    global channelName
    channelName = request.form.get("ChannelName")
    if not channelName:
        print("Please name the channel.")
        return "Please name the channel."
    else:
        print("Created Channel: ", channelName)
        return "Created Channel: " + channelName


@admin_server_bp.route("/DeleteChannel", methods=["POST"])
def delete_channel():
    global channelName
    channelName = request.form.get("ChannelName")
    if not channelName:
        print("Please name the target channel.")
        return "Please name the target channel."
    else:
        print("Deleted Channel: ", channelName)
        return "Deleted Channel: " + channelName


@admin_server_bp.route("/CreateServer", methods=["POST"])
def create_server():
    global serverName
    serverName = request.form.get("ServerName")
    if not serverName:
        print("Please name the server.")
        return "Please name the server."
    else:
        print("Created Server: ", serverName)
        return "Created Server: " + serverName


@admin_server_bp.route("/DeleteServer", methods=["POST"])
def delete_server():
    global serverName
    serverName = request.form.get("ServerName")
    if not serverName:
        print("Please name the target server.")
        return "Please name the target server."
    else:
        print("Deleted Server: ", serverName)
        return "Deleted Server: " + serverName
