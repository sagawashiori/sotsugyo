import sqlite3
from flask import Flask,render_template

app = Flask(__name__)


@app.route("/base")
def test():
    return  render_template("base.html")    


@app.route("/top")
def top():
    return render_template("top.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/second_top")
def second_top():
    return render_template("second_top.html")


@app.route("/image_upload")
def image_upload():
    return render_template("image_upload.html")


@app.route("/main_upload")
def main_upload():
    return render_template("main_upload.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/release")
def release():
    return render_template("release.html")

    
if __name__ == '__main__':
    app.run(debug =True)