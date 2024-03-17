from flask import Flask, request, render_template

app = Flask(__name__)


# Define routes
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/mute", methods=["POST"])
def mute_user():
    print("Mute user function executed.")
    return "User muted successfully."


@app.route("/unmute", methods=["POST"])
def unmute_user():
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


if __name__ == "__main__":
    app.run(debug=True)
