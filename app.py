from flask import Flask
from init.init_app import create_app

app = create_app()

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


if __name__ == "__main__":
    app.run()