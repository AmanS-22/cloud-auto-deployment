from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return " please leave me i want to go home i am sleepy"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
