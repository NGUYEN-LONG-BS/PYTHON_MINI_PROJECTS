from flask import Blueprint, render_template

# Khởi tạo Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')