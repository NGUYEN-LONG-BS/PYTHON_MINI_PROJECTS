# https://www.youtube.com/watch?v=AZjBgndiF4w&list=PLFyAEmibWSQCc60nNQByzmtbMjk3fGyIK&index=4
# LẬP TRÌNH WEB FLASK-PYTHON #3: RENDER TEMPLATE, CODE PYTHON TRONG HTML

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html"
                           ,var_name="biến đây"
                           ,cars=["Vin", "BMW", "Audi", "Toyota", "Honda", "Suzuki", "Mazda"]
                           )
    

if __name__ == '__main__':
    app.run(debug=True)