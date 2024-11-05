#!/usr/bin/env python3
"Basic Flask app"
from typing import Optional
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


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


@app.route("/")
def index():
    "index page"
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
