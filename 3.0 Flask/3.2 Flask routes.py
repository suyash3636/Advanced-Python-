from flask import Flask

app= Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Basics!"

@app.route('/home')
def home_alias():
    return "Welcome to the /home of Flask Basics!"
@app.route("/user/<username>")
def greet_user(username):
    return f"Hello, {username}!"

@app.route("/user/<int:user_id>")
def show_user_id(user_id):
    return f"User ID is {user_id}"

@app.route("/about")
def about():
    return "This is the About Page"

@app.route("/contact")
def contact():
    return "Contact us at: hello@example.com"
@app.route("/user/<username>/<int:user_id>")
def user_profile(username, user_id):
    return f"User {username} has ID {user_id}"
if __name__ == '__main__':
    app.run(debug=True) 