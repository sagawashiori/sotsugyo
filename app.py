import sqlite3
from flask import Flask,render_template

app = Flask(__name__)


@app.route("/base")
def test():
    return  render_template("base.html")    


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/list")
def task_list():
    conn = sqlite3.connect("fkask_test2.db")
    c = conn.cursor()
    c.execute("SELECT * FROM tasks;")
    task_list = []
    
    for row in c.fetchall():
        task_list.append({"id":row[0],"task":row[1]})
    
    c.close()
    return render_template("task_list.html",task_list=task_list)

@app.route("/add")
def add_get():
    return render_template("add.html")

@app.route("/main_upload")
def upload():
    return render_template("main_upload.html")

@app.route("/image_upload")
def upload2():
    return render_template("image_upload.html")
    
@app.route("/second_top")
def top2():
    return render_template("second_top.html")
    
if __name__ == '__main__':
    app.run(debug =True)