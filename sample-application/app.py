from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def hello():
    message = "Hello! This is our Network and System Administration Project."
    return Response(message, mimetype='text/plain')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
