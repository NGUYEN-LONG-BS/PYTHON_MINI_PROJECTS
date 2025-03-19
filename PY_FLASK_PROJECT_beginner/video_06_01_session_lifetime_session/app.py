# https://www.youtube.com/watch?v=sJJsehONNc8&list=PLFyAEmibWSQCc60nNQByzmtbMjk3fGyIK&index=7
# LẬP TRÌNH WEB FLASK-PYTHON #6: SESSION LÀ GÌ, LIFETIME SESSION

from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.config["SECRET_KEY"] = "thanhdz"
app.permanent_session_lifetime = timedelta(minutes=1)

@app.route('/')
def render_start():
    return redirect(url_for('login'))

@app.route('/home')
def render_home_page():
    return render_template("home.html"
                           ,var_name="Kế thừa templates"
                           )
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session.permanent = True  # Làm cho session luôn có lifetime
        if username == 'admin' and password == '123456':
            session['username'] = username  # Lưu trữ tên người dùng vào session
            return redirect(url_for("hello_user", name=username))
    return render_template("login.html")
    
@app.route('/index')
def hello_world():
    return render_template("index.html"
                           ,var_name="biến đây"
                           ,cars=["Vin", "BMW", "Audi", "Toyota", "Honda", "Suzuki", "Mazda"]
                           )

@app.route('/user')
def hello_user():
    print("chuyển sang hello_user")
    if 'username' in session:
        name = session['username']
        return f"<H1>Hello {name}</H1>"
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))
    
if __name__ == '__main__':
    app.run(debug=True)