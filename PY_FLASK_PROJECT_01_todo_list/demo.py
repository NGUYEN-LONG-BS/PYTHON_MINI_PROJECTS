from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<H1>Thanh DZ</H1>"

@app.route('/user/<name>')
def hello_user(name):
    return f"<H1> Hello {name}</H1>"

if __name__ == '__main__':
    app.run(debug=True)