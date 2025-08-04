from flask import Blueprint

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard_bp.route('/')
def home():
    return "Dashboard Home"
@dashboard_bp.route('/contact')
def contact():
    return "contact at hello@contact.com"

# /dashboard
# /dashboard/contact
