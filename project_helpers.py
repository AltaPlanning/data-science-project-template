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

# Project-level settings
PROJECT_NAME = 'Sunnyvale'
PROJECT_FILE_ROOT = join(settings.DS_PROJECT_ROOT, PROJECT_NAME)
PG_DB = 'ds_sunnyvale'

LOCAL_PROJECTION = 2227
