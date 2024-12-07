import logging


class Logger:
    _logger = None

    @classmethod
    def _initialize_logger(cls):
        if cls._logger is None:
            cls._logger = logging.getLogger("AppLogger")
            cls._logger.setLevel(logging.DEBUG)

            # Formatter for logs
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

            # Console Handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            console_handler.setFormatter(formatter)
            cls._logger.addHandler(console_handler)

            # File Handler
            file_handler = logging.FileHandler('app.log')
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            cls._logger.addHandler(file_handler)

    @classmethod
    def debug(cls, message):
        cls._initialize_logger()
        cls._logger.debug(message)

    @classmethod
    def info(cls, message):
        cls._initialize_logger()
        cls._logger.info(message)

    @classmethod
    def warning(cls, message):
        cls._initialize_logger()
        cls._logger.warning(message)

    @classmethod
    def error(cls, message):
        cls._initialize_logger()
        cls._logger.error(message)

    @classmethod
    def critical(cls, message):
        cls._initialize_logger()
        cls._logger.critical(message)
