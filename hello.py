from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run()