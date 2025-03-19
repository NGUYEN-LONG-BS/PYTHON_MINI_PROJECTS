# https://www.youtube.com/watch?v=0jYoqAXjry0&t=5s
# LẬP TRÌNH WEB FLASK-PYTHON #8: TỔNG QUAN ORM, SQLAlchemy

from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.config["SECRET_KEY"] = "thanhdz"
app.permanent_session_lifetime = timedelta(minutes=1)

@app.route('/home')
@app.route('/')
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
            flash('You logged in successfully', 'info')
            return render_template("user.html", var_name=username)
    if 'username' in session:
        print("username đã có trong session")
        flash('You are already logged in', 'info')
        name = session['username']
        return render_template("user.html", var_name=name)
    else:
        flash('You are not logged in', 'info')
        print("username không có trong session")
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
        return render_template("user.html", var_name=name)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You logged out', 'info')
    return redirect(url_for('login'))
    
if __name__ == '__main__':
    app.run(debug=True)