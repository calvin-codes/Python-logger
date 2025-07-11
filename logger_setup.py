import logging
from paths import LOG_PATH

def init_logger(name=__name__, level=logging.INFO, log_file=LOG_PATH):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.hasHandlers():
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

        # Handler für Konsole
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # Handler für Datei
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
    return logger
