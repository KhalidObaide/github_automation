from flask import Flask


db_uri = "DB_URI"
updated = "soet"

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world!"


if __name__ == '__main__':
    app.run(debug=True)

