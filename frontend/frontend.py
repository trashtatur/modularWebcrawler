
from flask import Flask, render_template
from ModuleStarter import run_all_modules, stop_all_modules
from SearchStrings import SEARCHSTRINGS
from spiders.RegisteredModules import REGISTERED_MODULES
from flask_socketio import SocketIO

mood = Flask(__name__)
socketio = SocketIO(mood)


@mood.route("/")
def main():
    return render_template('index.html', moduleNames=REGISTERED_MODULES)


@socketio.on('##SEND_DATA')
def startup(data):
    for thing in data['data']:
        SEARCHSTRINGS[thing] = data['data'][thing]

    run_all_modules()


@mood.route("/stopCrawler", methods=['POST'])
def stop_crawler():
    stop_all_modules()

    return "200"


socketio.run(mood, host='0.0.0.0')
