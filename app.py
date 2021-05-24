from flask import Flask

app = Flask('foofl')

app.secret_key ="sung"

@app.route("/login")
def login():
    pass

@app.route("/callback")
def callback():
    pass


@app.route("/logout")
def logout():
    pass

@app.route("/")
def index():
    return "hello"

@app.route("/potect")
def protect():
    return "aa"