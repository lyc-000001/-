# encoding=utf-8

import logging
import logging.handlers
import os
import time


class Msg:

    def __init__(self, name=None, logger_name='MMK'):
        self.name = name

        # 定义一个日志收集器
        self.logger = logging.getLogger(logger_name)
        # 设置收集器的级别，不设定的话，默认收集warning及以上级别的日志
        self.logger.setLevel('DEBUG')
        # 设置日志格式
        self.fmt = logging.Formatter('%(filename)s-%(lineno)d-%(asctime)s-%(levelname)s-%(message)s')
        # 日志文件输出位置+格式
        date_time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # 默认当前目录为工程的根目录
        path = os.getcwd()
        log_path = os.path.join(path, 'TestReport', 'TestLog')
        if not os.path.exists(log_path):
            # os.mkdir(log_path)
            os.makedirs(log_path)
        log_name = date_time + '_' + self.name + '.log'
        self.log_name = os.path.join(log_path, log_name)

    def __console(self, level, message):
        # 设置日志处理器-输出到文件
        file_handler = logging.FileHandler(self.log_name, mode='a+', encoding='utf-8')
        # 设置日志处理器级别
        file_handler.setLevel("DEBUG")
        # 处理器按指定格式输出日志
        file_handler.setFormatter(self.fmt)

        # 输出到控制台
        ch = logging.StreamHandler()
        # 设置日志处理器级别
        ch.setLevel("DEBUG")
        # 处理器按指定格式输出日志
        ch.setFormatter(self.fmt)

        # 收集器和处理器对接，指定输出渠道
        # 日志输出到文件
        self.logger.addHandler(file_handler)
        # 日志输出到控制台
        self.logger.addHandler(ch)

        if level == 'debug':
            self.logger.debug(message)
        elif level == 'info':
            self.logger.info(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        # 避免日志重复输出问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(file_handler)

        # 关闭打开得文件
        file_handler.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)


if __name__ == '__main__':
    log_msg = Msg(name='001')
    log_msg.debug('自定义的debug日志')
    log_msg.info('自定义的info日志')
    log_msg.warning('自定义的warning日志')
    log_msg.error('自定义的error日志')
