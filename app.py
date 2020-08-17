from flask import Flask, render_template, Response, request, send_from_directory
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from jinja2 import Template


app = Flask(__name__, static_folder='static')
auth = HTTPBasicAuth()

users = {
    "default": generate_password_hash("password"),
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route("/")
@auth.login_required
def index():
    return render_template('index.html',
        current_user = auth.current_user()
    )


if __name__ == '__main__':
    app.run(debug=True)
