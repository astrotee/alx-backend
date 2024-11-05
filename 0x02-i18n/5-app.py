#!/usr/bin/env python3
"Basic Flask app"
from typing import Dict, Optional
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    "app config"
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> Optional[str]:
    "get the locale to be used"
    locale_param = request.args.get('locale', None)
    if locale_param and locale_param in app.config['LANGUAGES']:
        return locale_param
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Optional[Dict]:
    "get the user logged in"
    user: str | None = request.args.get('login_as', None)
    if user:
        return users.get(int(user), None)


@app.before_request
def before_request():
    "set user if passed"
    user = get_user()
    if user:
        g.user = user


@app.route("/")
def index():
    "index page"
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run()
