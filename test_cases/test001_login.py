from pages import manger_url
from pages.pagein import Pagein
from tools.get_driver import GetDriver


class TestLogin:
    # 初始化driver方法
    def setup_class(self):
        self.driver = GetDriver.get_web_driver(manger_url)
        self.login_page = Pagein(self.driver).get_login_page()

    # 关闭driver
    def teardown_class(self):
        # self.login_page.quit_driver()
        pass

    # 测试业务流程
    def test_login(self):
        self.login_page.login("admin", "LSYJ14001")
        assert_text = self.login_page.get_assert()
        assert "全国经销商" in assert_text
