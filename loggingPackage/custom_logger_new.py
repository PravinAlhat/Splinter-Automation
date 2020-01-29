import logging
import inspect

def cust_log(logLevel='DEBUG'):

    # Create Logger
    loggerName = inspect.stack()[1][3]
    logObj = logging.getLogger(loggerName)
    logObj.setLevel(logging.DEBUG)

    # Create file handler
    fileHandler = logging.FileHandler('{0}.log'.format(loggerName))

    #Create formatter
    formatter = logging.Formatter('%(asctime)s -%(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

    # Add formatter to file handler
    fileHandler.setFormatter(formatter)

    # Add file handler to logger
    logObj.addHandler(fileHandler)

    return logObj



