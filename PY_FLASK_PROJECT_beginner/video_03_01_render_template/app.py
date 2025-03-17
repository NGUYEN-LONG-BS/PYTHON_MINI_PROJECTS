# https://www.youtube.com/watch?v=AZjBgndiF4w&list=PLFyAEmibWSQCc60nNQByzmtbMjk3fGyIK&index=4
# LẬP TRÌNH WEB FLASK-PYTHON #3: RENDER TEMPLATE, CODE PYTHON TRONG HTML

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/user/<username>')
def hello_user(username):
    return f"<H1>Hello {username}!</H1>"

@app.route('/blog/<int:blog_id>')
def blog(blog_id):
    return f"<H1>Blog {blog_id}!</H1>"
    

if __name__ == '__main__':
    app.run(debug=True)