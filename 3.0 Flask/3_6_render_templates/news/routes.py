from flask import Blueprint, render_template

news_bp = Blueprint('news', __name__)

@news_bp.route('/')
def home():
    print("✅ Home route called")
    return render_template('home.html')


@news_bp.route('/article1')
def article1():
    return render_template('article1.html')

@news_bp.route('/article2')
def article2():
    return render_template('article2.html')
