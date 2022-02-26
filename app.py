import sqlite3
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/helloworld")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/user/<name>")
def greet(name):
    return name + "さん、こんばんは！"

@app.route("/base")
def test():
    return  render_template("base.html")    

@app.route("/test_val")
def test_val():
    py_name ="にんじゃわんこ"
    py_age =14
    return render_template("index_val.html",name =py_name ,age =py_age)

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
    
if __name__ == '__main__':
    app.run(debug =True)