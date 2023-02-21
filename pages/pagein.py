"""
同意入口类
"""
from pages.data_page import DataPage
from pages.login_page import LoginPage


class Pagein:

    def __init__(self, driver):
        self.driver = driver

    # 获取登录页的对象
    def get_login_page(self):
        return LoginPage(self.driver)

    # 获取数据大屏页的对象
    def get_data_page(self):
        return DataPage(self.driver)
