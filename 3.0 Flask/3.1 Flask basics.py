from flask import Flask

app = Flask(__name__)  # create Flask app instance

@app.route("/")  # define route for homepage
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)