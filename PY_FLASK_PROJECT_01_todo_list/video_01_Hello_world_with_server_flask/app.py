# https://www.youtube.com/watch?v=s_LRaPSDpyY&list=PLFyAEmibWSQCc60nNQByzmtbMjk3fGyIK&index=2

from flask import Flask

app = Flask(__name__)

@app.route('/index')
def hello_world():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)