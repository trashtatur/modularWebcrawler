import flask
from web.config import Config
from flask import Flask, render_template, request
from flask_login import LoginManager, login_required, login_user, current_user
from ModuleStarter import run_all_modules, stop_all_modules
from SearchStrings import SEARCHSTRINGS
from web.User import User
from web.forms.LoginForm import LoginForm
from spiders.RegisteredModules import REGISTERED_MODULES
from flask_socketio import SocketIO
from web.helper import is_safe_url

login_manager = LoginManager()
mood = Flask(__name__)
login_manager.init_app(mood)
socketio = SocketIO(mood)
mood.config.from_object(Config)
user = ""

@login_manager.user_loader
def load_user(user_id):
    global user
    if user != "":
        if user.get_id() == user_id:
            return user
    return None


@mood.route("/", methods=['GET'])
def redirToLogin():
    return flask.render_template('login.html', form=LoginForm())


@mood.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flask.redirect('/index')
    form = LoginForm()
    if form.validate_on_submit() and (form.password.data == 'bla') and (form.username.data == 'mood-user'):
        global user
        user = User(1)
        login_user(user)
        flask.flash("LOGIN SUCCESSFUL")
        next = flask.request.args.get('next')
        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect('/index')

    return render_template("login.html", form=form)


@mood.route("/index")
@login_required
def main():
    return render_template('index.html', moduleNames=REGISTERED_MODULES)


@socketio.on('##SEND_DATA')
@login_required
def startup(data):
    for thing in data['data']:
        SEARCHSTRINGS[thing] = data['data'][thing]

    run_all_modules()


@mood.route("/stopCrawler", methods=['POST'])
@login_required
def stop_crawler():
    stop_all_modules()

    return "200"


socketio.run(mood, host='0.0.0.0')
