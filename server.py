from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def server_info():
    return "My server"


@app.route("/author")
def author():
    author = {
        "name": "Stas",
        "course": 3,
        "age": 21,
    }
    return jsonify(author)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
