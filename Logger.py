# coding: utf-8
import os
import sys
import json
import logging
import logging.config


class Logger(object):

    def __init__(self):
        try:
            with open('log_config.json', 'rt') as f:
                logging.config.dictConfig(json.load(f))
                self.logger_instance = logging.getLogger()
        except Exception as e:
            print("load logger failed: " + os.path.abspath(u'log_config.json'))
            print(e)
            sys.exit(1)

    def info(self, message):
        return self.logger_instance.info(message)

    def error(self, message):
        return self.logger_instance.error(message)

    def warning(self, message):
        return self.logger_instance.warning(message)

    def debug(self, message):
        return self.logger_instance.debug(message)


Logger = Logger()
