import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/base")
def test():
    return  render_template("base.html")    

#--------maha編集箇所----------#

@app.route("/top")
def top():
    return render_template("top.html")


@app.route("/login", methods=["POST"])
def move_login():
    return render_template("login.html")

@app.route("/login")
def login():
    return render_template("login.html")


# @app.route("/register", methods=["POST"])
# def move_register():
#     return render_template("register.html")

@app.route("/register")
def register():
    return render_template("register.html")


@app.route('/register', methods=['POST'])
def register_post():
    name = request.form.get('name')
    mail = request.form.get('mail')
    password = request.form.get('password')
    conn = sqlite3.connect('sotu.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES(null,?,?,?)", (name, mail, password))
    conn.commit()
    conn.close()
    return redirect('/login')


#--------maha編集箇所----------#


#--------maino編集箇所----------#

@app.route("/second_top")
def second_top():
    return render_template("second_top.html")


@app.route("/image_upload")
def image_upload():
    return render_template("image_upload.html")


@app.route("/main_upload")
def main_upload():
    return render_template("main_upload.html")
#--------maino編集箇所----------#


#--------sagawa-san編集箇所----------#

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/release")
def release():
    return render_template("release.html")

#--------sagawa-san編集箇所----------#

if __name__ == '__main__':
    app.run(debug =True)