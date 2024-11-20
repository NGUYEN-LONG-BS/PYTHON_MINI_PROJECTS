from flask import Flask
from flask import Flask, render_template
from flask import Flask, render_template, request
from flask import Flask, render_template, json, request
# from flask.ext.mysql import MySQL   # không còn sử dụng nữa
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations 
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'long123456'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

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
    
# @app.route('/signUp',methods=['POST'])
# def signUp():
#     print("create user code will be here !!")
#     # create user code will be here !!
#     # read the posted values from the UI 
#     _name = request.form['inputName']
#     _email = request.form['inputEmail']
#     _password = request.form['inputPassword']
#     # validate the received values 
#     if _name and _email and _password:
#         return json.dumps({'html':'<span>All fields good !!</span>'})
#     else:
#         return json.dumps({'html':'<span>Enter the required fields</span>'})


@app.route('/signUp',methods=['POST','GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:
            
            # All Good, let's call MySQL
            
            conn = mysql.connect()
            cursor = conn.cursor()
            _hashed_password = generate_password_hash(_password)
            cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message':'User created successfully !'})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close() 
        conn.close()

if __name__ == "__main__":
    app.run()
    
# Vào link sau: http://127.0.0.1:5000 hoặc http://localhost:5000/ sẽ thấy chữ Welcome xuất hiện

