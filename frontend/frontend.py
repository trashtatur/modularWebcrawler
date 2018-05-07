
from flask import Flask, render_template, request
from ModuleFactory import run_all_modules, stop_all_modules
from SearchStrings import SEARCHSTRINGS
from spiders.RegisteredModules import REGISTERED_MODULES
from flask_socketio import SocketIO


mood = Flask(__name__)
#socketio = SocketIO(mood)


@mood.route("/")
def main():
    return render_template('index.html', moduleNames=REGISTERED_MODULES)


@mood.route('/receiveData', methods=['POST'])
#@socketio.on('receiveData')
def startup():
    for thing in request.form:
        SEARCHSTRINGS[thing] = request.form[thing]

    run_all_modules()
    return "200"


@mood.route("/stopCrawler", methods=['POST'])
def stop_crawler():
    stop_all_modules()

    return "200"


mood.run(host='0.0.0.0')
