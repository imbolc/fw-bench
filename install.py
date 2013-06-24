#!/usr/bin/env python
import os

ENV_DIR = 'var/env'

try:
    os.makedirs(ENV_DIR)
except OSError:
    pass
os.system('virtualenv %s' % ENV_DIR)
os.system('%s/bin/easy_install pip' % ENV_DIR)
os.system('%s/bin/pip install --upgrade -r pipreq.txt' % ENV_DIR)
