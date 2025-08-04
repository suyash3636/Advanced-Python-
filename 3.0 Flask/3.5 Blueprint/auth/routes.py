from flask import Blueprint, render_template

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login')
def login():
    return "Auth Login Page"
@auth_bp.route('/')
def home():
    return "    Home Page"
# /auth/login