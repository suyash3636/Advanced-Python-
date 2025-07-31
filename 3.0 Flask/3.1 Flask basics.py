from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Basics!"
@app.route('/home')
def home_alias():
    return "Welcome to the /home of Flask Basics!"
if __name__ == '__main__':
    app.run(debug=True)