# -*- coding: utf-8 -*-
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

DEBUG = True

SCHEDULER_JOBSTORES = {
    'default': SQLAlchemyJobStore(url="mysql+pymysql://root:123456@192.168.0.111:3306/apscheduler?charset=utf8")
}

SCHEDULER_EXECUTORS = {
    'default': {'type': 'threadpool', 'max_workers': 5}
}

SCHEDULER_JOB_DEFAULTS = {
    'coalesce': False,
    'max_instances': 3
}

SCHEDULER_API_ENABLED = True
