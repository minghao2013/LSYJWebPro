from pages import manger_url
from pages.login_page import LoginPage
from pages.pagein import PageIn
from tools.get_driver import GetWebDriver


class TestDataPage:
    # 初始化driver方法
    def setup_class(self):
        self.driver = GetWebDriver.get_web_driver(manger_url)
        self.page_in = PageIn(self.driver)
        self.login_page: LoginPage = self.page_in.get_login_page()

    # 关闭driver
    def teardown(self):
        GetWebDriver.close_driver()

    # 测试业务流程
    def test_data_page(self, assert_result_text="admin", username="admin", password="LSYJ14001"):
        assert_text = self.login_page.get_assert()
        assert assert_result_text in assert_text
