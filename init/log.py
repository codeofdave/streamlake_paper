from loguru import logger
from init.config import g_config


class Log:
    def __init__(self):
        log_config = g_config.get('log')
        path = log_config.get('path', 'streamlake.log')
        level = log_config.get('level', 'INFO')
        rotation = log_config.get('rotation', '100 MB')
        logger.add(path, format="{time} | {level} | {message}", level=level, rotation=rotation)
