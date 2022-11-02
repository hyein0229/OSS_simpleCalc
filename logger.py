import logging

class Logger:

    def __init__(self, logger_name, file_name, level):

        self.logger = logging.getLogger(logger_name)
        self.level = level

        if self.level == 1:
            self.logger.setLevel(logging.INFO)
        elif self.level == 2:
            self.logger.setLevel(logging.ERROR)

        log_format = logging.Formatter(fmt = "%(asctime)s - %(levelname)s - %(message)s")

        file_handler = logging.FileHandler(filename = file_name)
        file_handler.setFormatter(log_format)

        self.logger.addHandler(file_handler)

    def log(self, message):
        if self.level == 1:
            self.logger.info(message)
        elif self.level == 2:
            self.logger.error(message)

    def get_stream(self):
        console = logging.StreamHandler()
        self.logger.addHandler(console)


    




