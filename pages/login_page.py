import pages
from base.base import Base


# 登录页


class LoginPage(Base):
    # 输入账号
    def input_account(self, username):
        self.do_send_keys(pages.manger_login_name, username)

    # 输入密码
    def input_pass(self, password):
        self.do_send_keys(pages.manger_pass, password)

    # 点击登录
    def click_login_btn(self):
        self.do_click(pages.login_btn)

    # 获取断言,用于跳转成功的断言
    def get_assert(self):
        return self.get_element_text(pages.asster_ele)

    # 综合业务调用方法
    def login(self, username, password):
        self.input_account(username)
        self.input_pass(password)
        self.click_login_btn()

    # 综合业务调用方法-->登录成功依赖方法
    def login_success(self, username, password):
        self.login(username, password)
