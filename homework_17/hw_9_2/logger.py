import logging
import os
import sys


logger = logging.getLogger('Logger')
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
c_format = logging.Formatter('%(levelname)s - %(message)s')
stream_handler.setFormatter(c_format)
logger.addHandler(stream_handler)

f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_log = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log_file.log')
file_handler = logging.FileHandler(file_log,  encoding='utf8')
file_handler.setFormatter(f_format)
logger.addHandler(file_handler)
