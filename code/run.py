import os
import re

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("main.html")  # Serve main.html from templates/html/

@app.route('/goToManagerPage')
def goToManagerPage():
    version =read_version()
    log = read_log()
    return render_template("manager.html",version=version,log = log)  # Serve main.html from templates/

def read_log():
        with open("log.txt",'r') as file:
            log = file.read().splitlines()
        return log  # Serve main.html from templates/

@app.route('/clean_log', methods=['POST'])
def clean_log():
    print("[INFO] Cleaning log file!!!")
    with open("log.txt", 'w') as file:
            file.write("")
    return {'message': 'Git update successful'}, 200

@app.route('/git_update', methods=['POST'])
def git_update():
    print("[INFO] Update files from git w8 4 finish!!!")
    if is_production:
        os.system("cd /home/ubuntu/Desktop/site-/code && git reset --hard HEAD  && git pull https://github.com/elad014/site-.git master --progress")
    return {'message': 'Git update successful'}, 200

def is_production():
    try:
        with open("prodaction.txt",'r') as file:
            key = file.read()
        return key == 'yes'
    except:
        pass


def read_version():
    with open('version.txt','r') as file:
        version = file.read()
    return version

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)