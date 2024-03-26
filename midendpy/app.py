from flask import Flask, render_template

from Adminpy import admin_bp
from Adminserverpy import admin_server_bp
from loginpy import login_bp
from signuppy import signup_bp

app = Flask(__name__)
app.register_blueprint(admin_bp)
app.register_blueprint(admin_server_bp)
app.register_blueprint(login_bp)
app.register_blueprint(signup_bp)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
