from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Simple Flask Site</h1><p>This is the home page.</p>"

@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This is a simple site built with Flask.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=106, debug=False)