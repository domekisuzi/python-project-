# -*-coding:utf-8-*-

import logging
import sys

from shixun.settings  import LOG_FMT, LOG_LEVEL, LOG_FILENAME, LOG_DATEFMT


class Logger(object):

    def __init__(self):
        # 获取一个logger对象
        self._logger = logging.getLogger()
        # 设置format对象
        self.formatter = logging.Formatter(fmt=LOG_FMT, datefmt=LOG_DATEFMT)
        # 设置日志输出模式
        # 设置文件日志模式
        self._logger.addHandler(self._get_file_handler(LOG_FILENAME))
        # 设置终端日志模式
        self._logger.addHandler(self._get_console_handler())
        # 设置日志等级
        self._logger.setLevel(LOG_LEVEL)

    def _get_file_handler(self, filename):
        '''返回一个文件日志handler'''
        # 获取一个文件日志handler
        filehandler = logging.FileHandler(filename=filename, encoding="utf-8")
        # 设置日志格式
        filehandler.setFormatter(self.formatter)
        return filehandler

    def _get_console_handler(self):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        return console_handler

    @property
    def logger(self):
        return self._logger


logger = Logger().logger

if __name__ == '__main__':
    logging.debug('调试信息')
    logging.info('logger info message')
    logging.warning('logger warning message')
    logging.error('logger error message')
    logging.critical('logger critical message')
