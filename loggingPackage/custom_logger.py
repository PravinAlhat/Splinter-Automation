import logging
import logging.config
import inspect
from datetime import datetime

def customlogger(loglevel):
    # To get the name of the class/method from where this method is called.
    now = datetime.now()
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    # Print all log message
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler('{0}'.format(loggerName)+'_'+str(now.strftime("%Y%m%d%H%M%S")) + '.log', mode='w')
    fileHandler.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s -%(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    return logger



