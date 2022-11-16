#!/usr/bin/python3
'''
Wesnoth Site Status (codename Valen)

Copyright (C) 2012 - 2022 by Iris Morelle <iris@irydacea.me>
See COPYING for use and distribution terms.
'''

from datetime import datetime
import sys

LOG_LEVEL_CRIT = -1
LOG_LEVEL_ERR = 0
LOG_LEVEL_WARN = 1
LOG_LEVEL_NOTICE = 2
LOG_LEVEL_INFO = 3
LOG_LEVEL_DEBUG = 4
LOG_LEVEL_TRACE = 5

_LOG_LEVEL_MIN = LOG_LEVEL_CRIT
_LOG_LEVEL_MAX = LOG_LEVEL_TRACE

_LOG_MARKERS = ('!!!', '***', '***', '===', '---', '···', '$$$')
_LOG_DESC = ('critical', 'error', 'warning', 'notice', 'info', 'debug', 'trace')
_LOG_TS_FORMAT = '%Y-%m-%d %H:%M:%S'

_log_level = LOG_LEVEL_NOTICE


def write(level: int, msg: str):
    """
    Writes a formatted log message to stderr with the specified log level.

    If the current log level is less than the one specified for the message,
    no message will be written.
    """
    global _log_level
    if level > _log_level:
        return
    marker = _LOG_MARKERS[level + 1] if 0 <= level + 1 < len(_LOG_MARKERS) else '???'
    desc = _LOG_DESC[level + 1] if 0 <= level + 1 < len(_LOG_MARKERS) else '???'
    ts = datetime.now().strftime(_LOG_TS_FORMAT)
    sys.stderr.write("{} [{} {}] {}\n".format(marker, ts, desc, msg))


def set_log_level(new_level: int):
    """
    Sets the log level.
    """
    global _log_level
    _log_level = max(_LOG_LEVEL_MIN, min(_LOG_LEVEL_MAX, new_level))


def log_level():
    """
    Retrieves the current log level.
    """
    global _log_level
    return _log_level


def critical(msg: str):
    """
    Outputs a message with LOG_LEVEL_CRIT severity.
    """
    write(LOG_LEVEL_CRIT, msg)


def error(msg: str):
    """
    Outputs a message with LOG_LEVEL_ERR severity.
    """
    write(LOG_LEVEL_ERR, msg)


def warning(msg: str):
    """
    Outputs a message with LOG_LEVEL_WARN severity.
    """
    write(LOG_LEVEL_WARN, msg)


def notice(msg: str):
    """
    Outputs a message with LOG_LEVEL_NOTICE severity.
    """
    write(LOG_LEVEL_NOTICE, msg)


def info(msg: str):
    """
    Outputs a message with LOG_LEVEL_INFO severity.
    """
    write(LOG_LEVEL_INFO, msg)


def debug(msg: str):
    """
    Outputs a message with LOG_LEVEL_DEBUG severity.
    """
    write(LOG_LEVEL_DEBUG, msg)


def trace(msg: str):
    """
    Outputs a message with LOG_LEVEL_TRACE severity.
    """
    write(LOG_LEVEL_TRACE, msg)
