from flask import Flask, render_template, json, request
from ModuleFactory import run_all_modules


mood = Flask(__name__)


@mood.route("/")
def main():
    return render_template('index.html')


@mood.route('/startup', methods=['POST'])
def startup():
    print("kaskade")
    run_all_modules()
    return "BLAAAAA"


mood.run()
