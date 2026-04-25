from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Docker Assignment</h1>
    <p>Containerized Python Flask Application</p>
    <p>Status: Running Successfully</p>
    <p>Created by: Your Name</p>
    """

@app.route("/about")
def about():
    return "This application is running inside a Docker container."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)