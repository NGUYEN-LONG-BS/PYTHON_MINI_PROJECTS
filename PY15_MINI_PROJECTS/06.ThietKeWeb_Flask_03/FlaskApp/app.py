from flask import Flask
from flask import Flask, render_template
from flask import Flask, render_template, request
from flask import Flask, render_template, json, request


app = Flask(__name__)

@app.route("/")
# Bước 1: Khởi tạo trang cơ bản Welcome
# def main():
#     return "Welcome!"

# Bước 2: Khởi tạo trang html có sẵn
def main():
    return render_template('index.html')

# Bước 3: Bấm vào nút Signup, đi đến trang signup
@app.route("/showSignUp")
def showSignUp():
    return render_template('signup.html')

# Bước 4: Tạo ra một phương thức mới gọi là signUp và đồng thời thêm một tuyến /signUp.
# @app.route('/signUp')
# def signUp():
#     print("create user code will be here !!")
#     # create user code will be here !!
    
@app.route('/signUp',methods=['POST'])
def signUp():
    print("create user code will be here !!")
    # create user code will be here !!
    # read the posted values from the UI 
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    # validate the received values 
    if _name and _email and _password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})

if __name__ == "__main__":
    app.run()
    
# Vào link sau: http://127.0.0.1:5000 hoặc http://localhost:5000/ sẽ thấy chữ Welcome xuất hiện

