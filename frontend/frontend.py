from flask import Flask, render_template, request
import ModuleFactory
from SearchStrings import SEARCHSTRINGS
from spiders.RegisteredModules import REGISTERED_MODULES


mood = Flask(__name__)


@mood.route("/")
def main():
    return render_template('index.html', moduleNames=REGISTERED_MODULES)


@mood.route('/receiveData', methods=['POST'])
def startup():
    for thing in request.form:
        SEARCHSTRINGS[thing] = request.form[thing]

    ModuleFactory.run_all_modules()


    return "200"


mood.run(host='0.0.0.0')
