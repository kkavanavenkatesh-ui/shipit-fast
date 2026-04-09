import random
from flask import Flask

app = Flask(__name__)

def get_ai_message():
    messages = [
        "You're doing great!", 
        "Your code is clean.", 
        "The pipeline is healthy. India In the country",
        "Automation is the future! o",
        "Kavana's engine is officially running."
        "This is good day."

    ]
    return random.choice(messages)

@app.route('/')
def hello():
    ai_thought = get_ai_message()
    return f"""
    <html>
        <body style="font-family: sans-serif; text-align: center; margin-top: 50px;">
            <h1>🚀 ShipIt AI Engine</h1>
            <p style="font-size: 1.5em; color: #2c3e50;">
                <strong>AI Thought of the day:</strong> {ai_thought}
            </p>
            <p>Refresh the page to see a new thought!</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)