import os
import sqlite3
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'user'

@app.route("/base")
def test():
    return  render_template("base.html")    

#--------maha編集箇所----------#

@app.route("/top")
def top():
    return render_template("top.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")


@app.route('/register', methods=['POST'])
def register_post():
    name = request.form.get('name')
    mail = request.form.get('mail')
    password = request.form.get('password')
    conn = sqlite3.connect('sotu1.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES(null,?,?,?)", (name, mail, password))
    conn.commit()
    conn.close()
    return redirect('/login')


@app.route('/login')
def login_get():
    if 'user_id' in session:  # もしsessionに user_id が含まれていたら
        return redirect('/second_top')  # .list ページにリダイレクト
    return render_template('second_top.html')


@app.route('/login', methods=['POST'])
def login_post():
    if 'user_id' in session:  # もしsessionに user_id が含まれていたら
        return redirect('/second_top')  # .list ページにリダイレクト
    mail = request.form.get('mail')
    password = request.form.get('password')

    conn = sqlite3.connect('sotu1.db')
    c = conn.cursor()

    c.execute('SELECT id FROM users WHERE mail = ? AND pass = ?',
              (mail, password))
    user = c.fetchone()  # (1, )
    conn.close()

    if user is None:  # 送られてきた mailとpassに一致するuserがいなかった場合
        return render_template('login.html')
    else:
        session['user_id'] = user[0]
        return redirect('/second_top')


@app.route('/image_upload', methods=["GET","POST"])
def image_upload():

    if request.method == "GET":
        return render_template("image_upload.html")

    else:
    # bbs.tplのinputタグ name="upload" をgetしてくる
        upload = request.files['upload']
    # uploadで取得したファイル名をlower()で全部小文字にして、ファイルの最後尾の拡張子が'.png', '.jpg', '.jpeg'ではない場合、returnさせる。
        if not upload.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            return 'png,jpg,jpeg形式のファイルを選択してください'

        else:
        # 下の def get_save_path()関数を使用して "./static/img/" パスを戻り値として取得する。
            save_path = get_save_path()
            # パスが取得できているか確認
            print(save_path)
            # ファイルネームをfilename変数に代入
            filename = upload.filename
            # 画像ファイルを./static/imgフォルダに保存。 os.path.join()は、パスとファイル名をつないで返してくれます。
            upload.save(os.path.join(save_path, filename))
            # ファイル名が取れることを確認、あとで使うよ
            print(filename)

            # アップロードしたユーザのIDを取得
            user_id = session['user_id']
            image = request.form.get('image')

            conn = sqlite3.connect('sotu1.db')
            c = conn.cursor()
            # update文
            # 上記の filename 変数ここで使うよ
            c.execute("update item set image = ? where id=?", (image, user_id))
            conn.commit()
            conn.close()

        return redirect('/main_upload')

def get_save_path():
    path_dir = "./static/img"
    return path_dir


@app.route('/main_upload', methods=['POST'])
def add_post():
    if 'user_id' not in session:  # もしsessionに user_id が含まれない場合
        return redirect('/login')  # ログインページにリダイレクト
    item_name = request.form.get('item_name')
    category = request.form.get('category')
    date = request.form.get('date')
    image = request.form.get('image')
    conn = sqlite3.connect("sotu1.db")
    c = conn.cursor()
    #  c.execute(文字列, リストorタプル)
    c.execute('INSERT INTO item VALUES(NULL, ?, ?, ?, ?)', (item_name, category, date, image))
    conn.commit()
    c.close()
    return redirect('/home')  # リダイレクト


# #--------maha編集箇所----------#


# #--------maino編集箇所----------#

@app.route("/second_top")
def second_top():
    return render_template("second_top.html")


# @app.route("/image_upload")
# def image_upload():
#     return render_template("image_upload.html")


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