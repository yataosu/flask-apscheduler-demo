# -*- coding: utf-8 -*-
from flask import Flask
from flask_apscheduler import APScheduler

from app.api.task import bp


def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    app.register_blueprint(bp)

    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()

    return app
