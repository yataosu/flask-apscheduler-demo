# -*- coding: utf-8 -*-
from datetime import datetime

from flask import Blueprint, current_app, request

bp = Blueprint("task", __name__, url_prefix="/task")


def job01(name, *args, **kwags):
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("hello {}".format(name), time_now)


@bp.route("/add", methods=["POST"])
def add():
    params = request.get_json()
    name = params.get("name")

    job_id = "job_id:{}".format(name)
    job = current_app.apscheduler.add_job(id=job_id, func=job01, trigger='interval', seconds=3, args=[name])

    job_id = job.id
    return job_id


@bp.route("/remove", methods=["DELETE"])
def remove():
    params = request.get_json()
    job_id = params.get("job_id")
    print(job_id)
    current_app.apscheduler.remove_job(id=job_id)
    return "remove"


@bp.route("/pause", methods=["POST"])
def pause():
    current_app.apscheduler.pause()
    return "pause"


@bp.route("/resume", methods=["POST"])
def resume():
    current_app.apscheduler.resume()
    return "resume"


@bp.route("/jobs", methods=["POST"])
def jobs():
    jobs = current_app.apscheduler.get_jobs()
    print(type(jobs), jobs)
    return "jobs"
