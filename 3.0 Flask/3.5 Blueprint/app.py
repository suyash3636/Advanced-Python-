from flask import Flask
from auth.routes import auth_bp
from dashboard.routes import dashboard_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)

@app.route('/')
def index():
    return "Main Home Page"

if __name__ == '__main__':
    app.run(debug=True)
