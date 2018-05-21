""" 
tasks.py
Copyright 2011-2018 Qunhe Tech, all rights reserved.
Qunhe PROPRIETARY/CONFIDENTIAL, any form of usage is subject to approval.

@Author: tianming
@created: 5/21/18
"""
# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task

from django_test.celery import app


@app.task
def task_test():
    print('test_task')

