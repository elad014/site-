import os

from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("main.html")  # Serve main.html from templates/html/

@app.route('/goToManagerPage')
def goToManagerPage():
    with open('version.txt','r') as file:
        version = file.read()
    return render_template("manager.html",version=version)  # Serve main.html from templates/

@app.route('/git_update', methods=['POST'])
def git_update():

    print("update_git w8 for finish!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    os.system("cd /home/ubuntu/Desktop/site-/code && git reset --hard HEAD  && git pull https://github.com/elad014/site-.git master --progress")
    return {'message': 'Git update successful'}, 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)