# api/app.py
from flask import Flask, request, render_template, jsonify, session, redirect, url_for
from dialogue.dialogue_system import DialogueSystem
import logging

app = Flask(__name__)
app.secret_key = 'YOUR_SECRET_KEY'  # Replace with a secure key in production.
logger = logging.getLogger(__name__)

# Initialize the dialogue system.
dialogue_system = DialogueSystem()

@app.route("/")
def index():
    # Default to day theme; allow theme switching via URL parameter.
    theme = request.args.get("theme", "day")
    return render_template("index.html", theme=theme)

@app.route("/set_theme/<theme>")
def set_theme(theme):
    session['theme'] = theme
    return redirect(url_for('index', theme=theme))

@app.route("/diagnose", methods=["POST"])
def diagnose():
    user_input = request.form.get("user_input")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400
    response = dialogue_system.generate_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    # Use a production WSGI server (like Gunicorn) when deploying.
    app.run(host="0.0.0.0", port=5000, debug=True)
