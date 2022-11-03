import logging

class Logger:

    def __init__(self, logger_name, file_name, level):

        self.logger = logging.getLogger(logger_name)   # 로거 생성
        self.level = level  # 로그 레벨 설정

        if self.level == 1:
            self.logger.setLevel(logging.INFO)
        elif self.level == 2:
            self.logger.setLevel(logging.ERROR)

        log_format = logging.Formatter(fmt = "%(asctime)s - %(levelname)s - %(message)s")  # 출력 형식 설정

        file_handler = logging.FileHandler(filename = file_name)  # 해당 파일로 로그를 출력해줄 파일 핸들러
        file_handler.setFormatter(log_format)  # 출력 포맷 설정

        self.logger.addHandler(file_handler)  

    def log(self, message):  # 로그 출력
        if self.level == 1:
            self.logger.info(message)
        elif self.level == 2:
            self.logger.error(message)

    def get_stream(self):
        console = logging.StreamHandler()  # 콘솔에 로그 출력
        self.logger.addHandler(console)


    




