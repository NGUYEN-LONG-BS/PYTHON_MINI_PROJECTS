# https://www.youtube.com/watch?v=KzOhmp6qJBA&list=PLFyAEmibWSQCc60nNQByzmtbMjk3fGyIK&index=6
# LẬP TRÌNH WEB FLASK-PYTHON #5: HTTP METHODS, POST AND GET

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

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
        if username == 'admin' and password == '123456':
            return redirect(url_for('hello_user', name='admin'))
        # else:
        #     return redirect(url_for('login'))
    return render_template("login.html")
    
@app.route('/index')
def hello_world():
    return render_template("index.html"
                           ,var_name="biến đây"
                           ,cars=["Vin", "BMW", "Audi", "Toyota", "Honda", "Suzuki", "Mazda"]
                           )

@app.route('/user/<name>')
def hello_user(name):
    return f"<H1>Hello {name}</H1>"
    
if __name__ == '__main__':
    app.run(debug=True)