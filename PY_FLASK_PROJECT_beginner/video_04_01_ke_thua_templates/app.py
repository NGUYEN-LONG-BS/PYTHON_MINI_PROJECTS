# https://www.youtube.com/watch?v=PoKKO48A_pg&list=PLFyAEmibWSQCc60nNQByzmtbMjk3fGyIK&index=5
# LẬP TRÌNH WEB FLASK-PYTHON #4: KẾ THỪA TEMPLATE, SỬ DỤNG BOOTSTRAP

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html"
                           ,var_name="biến đây"
                           ,cars=["Vin", "BMW", "Audi", "Toyota", "Honda", "Suzuki", "Mazda"]
                           )

@app.route('/home')
def render_home_page():
    return render_template("home.html"
                           ,var_name="Kế thừa templates"
                           )
    

if __name__ == '__main__':
    app.run(debug=True)