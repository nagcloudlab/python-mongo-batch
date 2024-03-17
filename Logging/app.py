
import logging

# level of logs

# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL


logging.basicConfig(filename='app.log', level=logging.WARNING, format='%(asctime)s:%(levelname)s:%(message)s')

def foo():
    logging.info('foo started')
    print("Hello World")
    logging.warning('This is a warning message')
    logging.info('foo ended')



foo()
