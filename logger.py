import logging

class Logger:

    def __init__(self, logger_name, file_name, level):

        Logger.logger = logging.getLogger(logger_name)
        Logger.level = level

        if Logger.level == 1:
            Logger.logger.setLevel(logging.INFO)
        elif Logger.level == 2:
            Logger.logger.setLevel(logging.ERROR)

        log_format = logging.Formatter(fmt = "%(asctime)s - %(levelname)s - %(message)s")

        file_handler = logging.FileHandler(filename = file_name)
        file_handler.setFormatter(log_format)

        Logger.logger.addHandler(file_handler)

    def log(self, message):
        if self.level == 1:
            logging.info(message)
        elif self.level == 2:
            logging.error(message)

    def get_stream(self):
        console = logging.StreamHandler()
        Logger.logger.addHandler(console)


    




