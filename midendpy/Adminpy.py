from flask import Blueprint, request, render_template

admin_bp = Blueprint("admin", __name__)

username = ""


# Define routes
@admin_bp.route("/admin")
def admin_page():
    render_template("Admin.html")
    return render_template("Admin.html")


@admin_bp.route("/mute", methods=["POST"])
def mute_user():
    global username
    username = request.form.get("username")
    if not username:
        print("username: ", username)
        return "Please provide a username. "
    else:
        print("Muted ", username)
        return "Muted " + username


@admin_bp.route("/unmute", methods=["POST"])
def unmute_user():
    print("Unmute user function executed.")
    return "User unmuted successfully."


@admin_bp.route("/kick", methods=["POST"])
def kick_user():
    print("Kick user function executed.")
    return "User kicked successfully."


@admin_bp.route("/ban", methods=["POST"])
def ban_user():
    print("Ban user function executed.")
    return "User banned successfully."


@admin_bp.route("/unban", methods=["POST"])
def unban_user():
    print("Unban user function executed.")
    return "User unbanned successfully."


@admin_bp.route("/edit_roles", methods=["POST"])
def edit_user_roles():
    print("Edit user roles function executed.")
    return "User roles edited successfully."


@admin_bp.route("/process_user", methods=["POST"])
def process_user():
    global username
    username = request.form.get("username")
    if not username:
        return "Please provide a username."
    else:
        print("Received username:", username)
        return "Received username: " + username
