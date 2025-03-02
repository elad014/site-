import os

from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("main.html")  # Serve main.html from templates/html/

@app.route('/goToManagerPage')
def goToManagerPage():
    return render_template("manager.html")  # Serve main.html from templates/

@app.route('/git_update', methods=['POST'])
def git_update():
    print("Clicked")  # This prints to the server terminal
    return jsonify({"message": "Button clicked!"})  # Respond to client

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)