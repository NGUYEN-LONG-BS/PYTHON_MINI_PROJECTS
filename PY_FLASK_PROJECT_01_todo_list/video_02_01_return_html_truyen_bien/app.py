# https://www.youtube.com/watch?v=s_LRaPSDpyY&list=PLFyAEmibWSQCc60nNQByzmtbMjk3fGyIK&index=2
# LẬP TRÌNH WEB FLASK-PYTHON #2: RETURN THẺ HTML, TRUYỀN BIẾN, CHUYỂN HƯỚNG TRANG!

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World: Anh Nè 27"

@app.route('/admin')
def hello_admin():
    return f"<H1>Hello, đây là trang admin!</H1>"

@app.route('/user/<username>')
def hello_user(username):
    if username == "admin_name":
        return redirect(url_for('hello_admin'))
    return f"<H1>Hello {username}!</H1>"


    

if __name__ == '__main__':
    app.run(debug=True)