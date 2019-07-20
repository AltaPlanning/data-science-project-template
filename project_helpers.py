"""
``project_helpers.py``
----------------------

A collection of variables, functions, and anything else that
facilitates development across this project's code base.

Example
-------

    >>> from project_helpers import PG_DB, PROJECT_FILE_ROOT

"""
from os.path import join

import alta_settings as settings

VERSION = '0.1.0'

# Project-level settings
PG_DB = 'ds_sunnyvale'

PROJECT_NAME = 'Sunnyvale'
PROJECT_FILE_ROOT = join(settings.DS_PROJECT_ROOT, PROJECT_NAME)

LOCAL_PROJECTION = 2227

TEAM_MEMBERS = [
    'Aaron Fraint, AICP',
]

ANALYST_TEAM = ' & '.join(TEAM_MEMBERS)

