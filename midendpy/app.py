from flask import Flask, render_template

from Adminpy import admin_bp
from Adminserverpy import admin_server_bp
from loginpy import login_bp
from signuppy import signup_bp

app = Flask(__name__, template_folder="HTML")
app.register_blueprint(signup_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(admin_server_bp)
app.register_blueprint(login_bp)


@app.route("/")
def index():
    return render_template("LogIn.html")


if __name__ == "__main__":
    app.run(debug=True)
