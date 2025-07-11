import logging
from logger_setup import init_logger

logger = init_logger(level=logging.INFO)
logger.info("fyi it worked!")
