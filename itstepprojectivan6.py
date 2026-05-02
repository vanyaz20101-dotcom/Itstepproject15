import logging

logging.basicConfig(level=logging.DEBUG, filename='logfile.log', filemode='a', format='%(levelname)s - %(message)s - %(asctime)s)')

logging.debug('debugging message')
logging.info('info message')
logging.warning('Warning message')
logging.error('error message')
logging.critical('critical message')

try:
    print(10/0)
except Exception as e:
    logging.exception(e)