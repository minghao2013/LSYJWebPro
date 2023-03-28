import functools
import os
import time

import allure
from selenium.common import JavascriptException

from tools.logs_utils import logger


# 查找元素异常截图日志的装饰器
def exception_record(func):
    """
    :param func:
    :return:
    """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            driver = args[0].driver
            logger.error("查找元素{}没有找到".format(args[1]))
            timestamp = int(time.time())
            # 获取当前工具文件所在的路径
            root_path = os.path.dirname(os.path.abspath(__file__))
            # 拼接当前要输出日志的路径
            log_dir_path = os.sep.join([root_path, "..", f'/images/'])
            if not os.path.isdir(log_dir_path):
                os.mkdir(log_dir_path)
            image_path = log_dir_path + f"images_{timestamp}.PNG"
            driver.save_screenshot(image_path)
            allure.attach.file(image_path, name="picture", attachment_type=allure.attachment_type.PNG)
            raise e

    return inner


# 断言异常截图日志的装饰器
def exception_assert(func):
    """
    :param func:
    :return:
    """

    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            driver = args[0].driver
            timestamp = int(time.time())
            # 获取当前工具文件所在的路径
            root_path = os.path.dirname(os.path.abspath(__file__))
            # 拼接当前要输出日志的路径
            log_dir_path = os.sep.join([root_path, "..", f'/images/'])
            if not os.path.isdir(log_dir_path):
                os.mkdir(log_dir_path)
            image_path = log_dir_path + f"images_{timestamp}.PNG"
            driver.save_screenshot(image_path)
            allure.attach.file(image_path, name="picture", attachment_type=allure.attachment_type.PNG)
            logger.error("逾期结果错误,逾期结果 {} 和实际结果 {},不相等".format(kwargs.get("expect"), kwargs.get("fact")))
            raise e

    return inner


def execute_js_exception(fun):
    def inner(*args, **kwargs):

        try:
            return fun(*args, **kwargs)
        except JavascriptException as e:
            logger.error("执行javascript错误{}".format())
            raise e

    return inner
