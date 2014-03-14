#!var/env/bin/python
import os
import time
import urllib
import subprocess

import prettytable


FRAMEWORKS = [
    {'name': 'bottle',  'run': ['./run.py']},
    {'name': 'django',  'run': ['./run.py']},
    {'name': 'django_jinja',  'run': ['./run.py']},
    {'name': 'flask',   'run': ['./run.py']},
    {'name': 'pysi',    'run': ['./run.py']},
    {'name': 'tornado', 'run': ['./run.py']},
    {'name': 'express', 'run': ['node', 'app.js']},
]
BENCHMARKS = [
    {
        'name': 'hello',
        'url': 'http://127.0.0.1:8000/hello/',
        'requests': 10000,
        'concurrency': 10,
        'test_output': 'Hello',
    },
    {
        'name': 'table',
        'url': 'http://127.0.0.1:8000/table/',
        'requests': 1000,
        'concurrency': 10,
        'test_output': '<table',
    },
]


def run_server(fw, bench):
    print ('starting server: %s ...' % fw['name']),
    os.chdir('%s_app' % fw['name'])
    process = subprocess.Popen(fw['run'])
    while True:
        time.sleep(1)
        r = urllib.urlopen(bench['url'])
        if r.code != 200:
            print '.',
            continue
        break
    body = r.read()
    assert bench['test_output'] in body, body
    print ' ok'
    os.chdir('..')
    return process


def run_bench(bench):
    output =  subprocess.check_output(['sudo', 'ab', '-n%s' % bench['requests'],
        '-c%s' % bench['concurrency'], bench['url']])
    return parse_result(output)


def parse_result(output):
    rps = output.split('Requests per second:')[1].strip().split(' ')[0]
    return int(float(rps))


if __name__ == '__main__':
    table = prettytable.PrettyTable(['benchmark / framework'] +
            [b['name'] for b in BENCHMARKS])
    for fw in FRAMEWORKS:
        cols = [fw['name']]
        for bench in BENCHMARKS:
            print 'starting bench: %(name)s ...' % bench
            server = run_server(fw, bench)
            rps = run_bench(bench)
            server.terminate()
            server.wait()
            print 'RPS:', rps
            cols.append(rps)
        table.add_row(cols)
    print table
