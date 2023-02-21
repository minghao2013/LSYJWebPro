from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tools.logs_utils import logger


class Base:
    # 实例化driver
    def __init__(self, driver):
        logger.info("查正在初始化driver{}".format(driver))
        self.driver: webdriver = driver

    # 查找元素方法
    def do_find_element(self, by, val=None, timeout=30, poll_frequency=0.5):
        """
        :param by: 查找元素的定位方法
        :param val: 查找元素的表达式
        :param timeout: 查找元素的超时时间,默认20秒
        :param poll_frequency: 查找元素的等待时间,默认0.5秒
        """
        try:
            logger.error("正在查找元素元素{}没有找到".format(by))
            if val is None:
                return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
                    lambda x: x.find_element(*by), "正在查找元素元素{}没有找到".format(by))
            else:
                return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
                    lambda x: x.find_element(by, val), "正在查找元素元素{}没有找到".format(by))
        except Exception as e:
            logger.error("查找元素{}没有找到".format(by))
            raise e

    # send keys封装方法
    def do_send_keys(self, by, text):
        logger.info("正在对{}元素执行输入操作,输入内容是{}".format(by, text))
        ele = self.do_find_element(by)
        ele.clear()
        ele.send_keys(text)
        logger.info("对{}元素输入设置{}完成".format(by, text))

    # 单击方法封装
    def do_click(self, by):
        logger.info("正在对{}元素执行点击操作".format(by))
        self.do_find_element(by).click()
        logger.info("对{}元素执行点击操作完成".format(by))

    # 获取元素文本
    def get_element_text(self, by):
        logger.info("正在对{}元素执行获取文本操作".format(by))
        assert_text = self.do_find_element(by).text
        logger.info("正在对{}元素执行获取文本操作完成".format(by))
        return assert_text

    # 退出登录
    def quit_driver(self):
        logger.info("正在对driver{}清空操作".format(self.driver))
        if self.driver is not None:
            self.driver.quit()
            self.driver = None

    # 滑动查找元素方法
    def swipe_element(self, by, move_times=1):
        """
        :param by: 查找元素的方法和元素定位方式
        :param move_times: 滑动次数默认是1次
        """
        for i in range(move_times):
            try:
                return self.driver.find_element(*by)
            except:
                logger.info("开始第{}次滑动查找元素{}".format(move_times, by))
                screen_size = self.driver.get_window_size()
                start_x = screen_size.get("width") / 2
                start_y = screen_size.get("height") * 0.75
                end_x = start_x
                end_y = screen_size.get("height") * 0.3
                self.driver.swipe(start_x, start_y, end_x, end_y, 400)
            if i == move_times - 1:
                logger.error("没有找到元素{}".format(by))
                raise NoSuchElementException(f"第{move_times}次滑动没有元素")

    # 查找某个元素出现,知道可以点击
    def expected_conditions_enable_click(self, by, val=None):
        """
        :param by:
        :param val:
        """
        WebDriverWait(self.driver, timeout=20, poll_frequency=1).until(
            expected_conditions.visibility_of_element_located(by),
            "没有找到元素{}".format(by)).click()
        # print(self.driver.page_source)
