import pytest

from pages import manger_url
from pages.pagein import PageIn
from tools.except_fixture import exception_assert
from tools.get_data import get_data
from tools.get_driver import GetWebDriver


class TestLogin:
    __LOGIN_SUCCESS_DATA = get_data("login")
    __LOGIN_FAILED_DATA = get_data("login_error")

    # 初始化driver方法
    def setup(self):
        self.driver = GetWebDriver.get_web_driver(manger_url)
        self.login_page = PageIn(self.driver).get_login_page()

    # 关闭driver
    def teardown(self):
        GetWebDriver.close_driver()

    # 测试业务流程
    @pytest.mark.parametrize("username,password,expect,fact", __LOGIN_SUCCESS_DATA.get("login"),
                             ids=__LOGIN_SUCCESS_DATA.get("ids"))
    @exception_assert
    def test_login(self, username, password, expect, fact):
        self.login_page.login(username, password)
        assert_text = self.login_page.get_assert()
        assert expect in assert_text

    @pytest.mark.parametrize("username,password,expect,fact", __LOGIN_FAILED_DATA.get("login_error"),
                             ids=__LOGIN_FAILED_DATA.get("ids"))
    @exception_assert
    def test_login_failed(self, username, password, expect, fact):
        assert_text = self.login_page.login_failed(username, password).get_login_failed_text()
        assert expect in assert_text
