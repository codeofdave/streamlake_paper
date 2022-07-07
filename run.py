from init.log import Log
from loguru import logger

Log()
#@logger.catch

logger.info("test info")
logger.error("test error")
logger.debug('test debug')