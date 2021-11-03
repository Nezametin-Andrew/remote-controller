from flask import Flask
import json
import redis


app = Flask(__name__)


@app.route("/")
def main():
    return json.dumps({"command": "open_web", "params": ["https://google.com", 0]})



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')