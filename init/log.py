import logging
from logging.config import dictConfig
from init.config import g_config

log_level = {
    'FATAL': logging.FATAL,
    'ERROR': logging.ERROR,
    'WARNING': logging.WARNING,
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG,
    'NOTSET': logging.NOTSET
}


class Log():
    def __init__(self):
        log_config = g_config.get('log')
        log_file = log_config.get('file', 'streamlake.log')
        level = log_config.get('level', 'INFO')
        rotation = log_config.get('rotation', '100 MB')
        LOGGER = {
            'version': 1,
            'formatters': {
                'default': {
                    'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
                }
            },
            'handlers': {
                'file': {
                    'class': 'logging.handlers.RotatingFileHandler',
                    'formatter': 'default',
                    'filename': log_file,
                    'level': level,
                    'maxBytes': rotation*1024*1024,
                    'backupCount': 5,
                    'delay': True
                }
            },
            'root': {
                'level': 'INFO',
                'handlers': ['file']
            }
        }

        dictConfig(LOGGER)

        logging
        logging.basicConfig(level=log_level.get(level),
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            rotation=)
        hander = logging.
        self.log = logging.getLogger('streamLake')
    def info(self, message):
        log

log: Log
