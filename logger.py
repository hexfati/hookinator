import logging
import time
from auxFunctions import calculateMD5
def init(filepath):
    global console_logger
    global file_logger

    console_logger = logging.getLogger("console_logger")
    logFormatter = logging.Formatter("%(message)s")
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    console_logger.addHandler(consoleHandler)
    console_logger.setLevel(logging.DEBUG)
    console_logger.propagate = False

    md5 = calculateMD5(filepath)
    file_logger = logging.getLogger("file_logger")
    logFormatter = logging.Formatter("%(message)s")
    consoleHandler = logging.FileHandler(md5+'_hookinator.log')
    consoleHandler.setFormatter(logFormatter)
    file_logger.addHandler(consoleHandler)
    file_logger.setLevel(logging.WARNING)
    file_logger.propagate = False

def log(level, string):
    console_logger.log(level=level, msg=string)
    file_logger.log(level, msg=string)