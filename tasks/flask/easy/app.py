# Flask - Easy

from flask import Flask

app = Flask(__name__)

# TODO: Implement rest of the code here

@app.route("/")
def index():
    return "Hello, Flask!"


if __name__ == "__main__":
    app.run(debug=True)
