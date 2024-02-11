#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Configuration file.
"""

import logging
from pathlib import Path

# **********
# Logging configuration
PROGRAM_LOG_FILE_PATH = Path(__file__).resolve().parent / "program_log.txt"

class StderrFilter(logging.Filter):
    def filter(self, record):
        return record.levelno >= logging.ERROR

class StdoutFilter(logging.Filter):
    def filter(self, record):
        return record.levelno < logging.ERROR

LOGGER_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,  # Doesn't disable other loggers that might be active
    "formatters": {
        "default": {
            "format": "[%(levelname)s][%(funcName)s] | %(asctime)s | %(message)s",
        },
        "simple": {
            "format": "[%(levelname)s][%(funcName)s] | %(message)s",
        },
    },
    
    "filters": {
        "stderr_only": {
            "()": StderrFilter,
        },
        "stdout_only": {
            "()": StdoutFilter,
        }
    },
        
    "handlers": {
        "logfile": {
            "class": "logging.FileHandler",
            "formatter": "default",
            "level": "INFO",
            "filename": PROGRAM_LOG_FILE_PATH.as_posix(),
            "mode": "a",
            "encoding": "utf-8",
        },
        "console_stdout": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "DEBUG",
            "stream": "ext://sys.stdout",
            "filters": ["stdout_only"],  # Using our filter
        },
        "console_stderr": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "ERROR",
            "stream": "ext://sys.stderr",
            "filters": ["stderr_only"],  # Using our filter
        },
    },
    "root": {  # Simple program, so root logger uses all handlers
        "level": "DEBUG",
        "handlers": [
            "logfile",
            "console_stdout",
            "console_stderr",
        ]
    }
}

# **********
if __name__ == "__main__":
    pass