import inspect
import logging


class LogGenerator:

    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler('D:\\Classes\\Framework_Practice\\Logs\\Automation_logs.log')
        logformat = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s ")
        logfile.setFormatter(logformat)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger















