import logging

class Logger:
    def __init__(self, log_file):
        self._logger = logging.getLogger('html_validator_logger')
        self._logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        self._logger.addHandler(file_handler)

    def error(self, message):
        self._logger.error(message)

    def warning(self, message):
        self._logger.warning(message)

    def info(self, message):
        self._logger.info(message)

    def debug(self, message):
        self._logger.debug(message)

logger = Logger