from flask import Flask, jsonify ,abort , request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome to the Flask Error Handling Example!")

@app.route('/divide/<int:num1>/<int:num2>')
def divide(num1, num2):
    try:
        result = num1 / num2
        return jsonify(result=result)
    except ZeroDivisionError:
        return jsonify(error="Division by zero is not allowed."), 400

@app.route('/data/<Name>')
def get_data(Name):
    if Name == "admin":
        return jsonify(data="Admin data accessed.")
    else:
        return jsonify(error="Unauthorized access."), 403
    
@app.errorhandler(403)
def forbidden(e):
    print(e)  # Logs the exception object
    return "Access denied (403)", 403

@app.errorhandler(404)
def not_found(error):
    return jsonify(error="Resource not found."), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify(error="Internal server error."), 500

@app.route('/admin')
def admin():
    role = request.args.get('role', 'guest')  # e.g., /admin?role=admin

    if role != 'admin':
        abort(403)
    
    return "Welcome, Admin!"

if __name__ == '__main__':
    app.run(debug=True)