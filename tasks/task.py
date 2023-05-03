from contextlib import ContextDecorator
from datetime import datetime


class LogFile(ContextDecorator):
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.start_time = datetime.now()
        self.log_file = open(self.file_name, "a")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = datetime.now()
        execution_time = end_time - self.start_time

        if exc_type:
            self.log_file.write(f"Start: {self.start_time} | Run: {execution_time} | An error occurred: {exc_val}\n")
            self.log_file.close()
            raise exc_type(exc_val).with_traceback(exc_tb)
        else:
            self.log_file.write(f"Start: {self.start_time} | Run: {execution_time} | An error occurred: None\n")
            self.log_file.close()

