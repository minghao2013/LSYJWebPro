from time import sleep

import pages
from base.web_base import WebBase
from pages.data_page import DataPage


class LoginPage(WebBase):
    # # 输入账号
    # def input_account(self, username):
    #    self

    # # 输入密码
    # def input_pass(self, password):

    # # 点击登录
    # def click_login_btn(self):
    #     self.do_click(pages.login_btn)

    # 获取断言,用于跳转成功的断言
    def get_assert(self):
        return self.get_element_text(pages.assert_ele)

    # 综合业务调用方法
    def login(self, username="admin", password="LSYJ14001"):
        self.do_send_keys(pages.manger_login_name, username)
        self.do_send_keys(pages.manger_pass, password)
        self.do_click(pages.login_btn)
        return DataPage(self.driver)

    # 综合业务调用方法-->登录成功依赖方法
    def login_failed(self, username, password):
        self.do_send_keys(pages.manger_login_name, username)
        self.do_send_keys(pages.manger_pass, password)
        self.do_click(pages.login_btn)
        return self
        # 获取断言,用于跳转成功的断言

    def get_login_failed_text(self):
        sleep(1)
        return self.get_element_text(pages.master_add_success_msg)
