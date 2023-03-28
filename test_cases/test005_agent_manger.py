import allure
import pytest

from pages import manger_url
from pages.pagein import PageIn
from tools.get_data import get_data
from tools.get_driver import GetWebDriver


@allure.feature("经销商管理")
class TestAgent:
    __ADD_AGENT = get_data("add_agent")
    __SEARCH_AGENT = get_data("search_agent")

    # 初始化driver方法
    def setup(self):
        self.driver = GetWebDriver.get_web_driver(manger_url)
        self.login_page = PageIn(self.driver).get_login_page()

    # 关闭driver
    def teardown(self):
        GetWebDriver.close_driver()

    @allure.title("添加普通用户测试用例")
    @pytest.mark.parametrize("user_name,phone_number,expect", __ADD_AGENT.get("add_agent"),
                             ids=__ADD_AGENT.get("ids"))
    def test_add_agent(self, user_name, phone_number, expect):
        msg = self.login_page.login(). \
            go_to_agent_list(). \
            goto_agent_list(). \
            goto_add_agent_page(). \
            set_agent_content(user_name, phone_number). \
            get_tip_msg()
        assert expect in msg

    @allure.title("搜索经销商")
    @pytest.mark.parametrize("keyword,expect", __SEARCH_AGENT.get("search_agent"),
                             ids=__SEARCH_AGENT.get("ids"))
    def test_search_agent(self, keyword, expect):
        res = self.login_page.login(). \
            go_to_agent_list(). \
            goto_agent_list(). \
            search_agent(keyword). \
            get_search_result()
        assert str(expect) in res
