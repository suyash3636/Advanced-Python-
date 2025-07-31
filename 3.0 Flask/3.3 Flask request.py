from flask import Flask , request , jsonify

app= Flask(__name__)

@app.route('/greet', methods=["GET"])
def greet():
    name = request.args.get("name", "Guest")  # get ?name=... from URL
    return jsonify({"message": f"Hello, {name}!"})

@app.route('/submit', methods=["POST"])
def submit():
    data = request.get_json()  # Expecting JSON data
    name = data.get("name")
    age = data.get("age")
    print("Received data:", data)
    return jsonify({
        "status": "success",
        "name": name,
        "age": age
    })
if __name__ == '__main__':
    app.run(debug=True)