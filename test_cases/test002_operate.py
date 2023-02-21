from pages import manger_url
from pages.data_page import DataPage
from pages.login_page import LoginPage
from pages.pagein import Pagein
from tools.get_driver import GetDriver


class TestDataPage:
    # 初始化driver方法
    def setup_class(self):
        self.driver = GetDriver.get_web_driver(manger_url)
        self.page_in = Pagein(self.driver)
        self.login_page: LoginPage = self.page_in.get_login_page()
        self.data_page: DataPage = self.page_in.get_data_page()

    # 关闭driver
    def teardown_class(self):
        # self.login_page.quit_driver()
        pass

    # 测试业务流程
    def test_data_page(self, assert_result_text="admin", username="admin", password="LSYJ14001"):
        self.login_page.login_success(username, password)
        self.data_page.go_to_operate_btn()
        assert_text = self.data_page.get_operate_text()
        assert assert_result_text in assert_text
