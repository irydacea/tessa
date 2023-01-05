#!/usr/bin/python3
'''
Wesnoth Site Status (codename Valen)

Copyright (C) 2012 - 2023 by Iris Morelle <iris@irydacea.me>
See COPYING for use and distribution terms.
'''

import lib.log as log
import sys


def die(msg: str):
    log.critical("*** {}".format(msg))
    sys.exit(42)
