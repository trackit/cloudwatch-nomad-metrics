#!/usr/bin/env python3

import collections
import datetime
import sched
import time
import pprint

import nomad
import boto3


client_cloudwatch = boto3.client('cloudwatch')
client_nomad = nomad.Nomad()
states = frozenset(['running', 'pending', 'dead'])


def put_metrics(now):
    jobs = client_nomad.jobs.get_jobs()
    job_states = collections.Counter({s: 0 for s in states})
    job_states.update(j['Status'] for j in jobs)
    metric_data = [
        {
            'MetricName': 'Job count',
            'Timestamp': now,
            'Value': count,
            'Unit': 'Count',
            'Dimensions': [
                { 'Name': 'State', 'Value': state },
            ],
        }
        for state, count in job_states.items()
    ]
    pprint.pprint(metric_data)
    client_cloudwatch.put_metric_data(
        Namespace='Nomad',
        MetricData=metric_data,
    )
    enter_next(s, put_metrics)


def enter_next(s, function):
    now = datetime.datetime.utcnow()
    now_next = now.replace(
        second=0,
        microsecond=0,
    ) + datetime.timedelta(minutes=1)
    s.enterabs(
        time=now_next.timestamp(),
        priority=1,
        action=function,
        argument=(now_next,),
    )


if __name__ == '__main__':
    s = sched.scheduler(lambda: datetime.datetime.utcnow().timestamp(), time.sleep)
    enter_next(s, put_metrics)
    while True:
        s.run()
