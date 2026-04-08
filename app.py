from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    # CHANGE THE TEXT BELOW
    return "<h1>Version 3.0: Full!</h1>"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)