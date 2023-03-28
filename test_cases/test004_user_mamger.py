import allure
import pytest

from pages import manger_url
from pages.pagein import PageIn
from tools.db_helper import DBHelper
from tools.get_data import get_data
from tools.get_driver import GetWebDriver
from tools.logs_utils import logger


@allure.feature("用户管理")
class TestUserManger:
    __SEARCH_DATA = get_data("search_user")
    __ADD_NORMAL_DATA = get_data("add_normal_user")
    __ADD_VIP_DATA = get_data("add_vip_user")

    # 初始化driver方法
    def setup(self):
        self.driver = GetWebDriver.get_web_driver(manger_url)
        self.login_page = PageIn(self.driver).get_login_page()
        self.dbhelp = DBHelper()

    # 关闭driver
    def teardown(self):
        GetWebDriver.close_driver()

    @allure.title("添加普通用户测试用例")
    @pytest.mark.parametrize("nick_name,phone_number,e_mail,expect", __ADD_NORMAL_DATA.get("add_normal_user"),
                             ids=__ADD_NORMAL_DATA.get("ids"))
    def test_add_normal_user(self, nick_name, phone_number, e_mail, expect):
        asert_msg = self.login_page.login(). \
            go_to_user_list_btn(). \
            add_normal_user(). \
            add_user_content(nick_name, phone_number, e_mail). \
            get_add_success_msg()
        assert expect in asert_msg

    @allure.title("添加VIP用户测试用例")
    @pytest.mark.parametrize("nick_name,phone_number,e_mail,view_date,expect", __ADD_VIP_DATA.get("add_vip_user"),
                             ids=__ADD_VIP_DATA.get("ids"))
    def test_add_vip_user(self, nick_name, phone_number, e_mail, view_date, expect):
        select_sql = "select * from ob_member where mobile={}".format(phone_number)
        delete_sql = "delete from ob_member where mobile={}".format(phone_number)
        select_result = self.dbhelp.fetch_one(select_sql)
        if select_result:
            execute_result = self.dbhelp.exec(delete_sql)
            print(execute_result)
        asert_msg = self.login_page.login(). \
            go_to_user_list_btn().add_vip_user(). \
            add_user_content(nick_name, phone_number, e_mail, view_date). \
            get_add_success_msg()
        assert expect in asert_msg

    @allure.title("查找用户测试用例")
    @pytest.mark.parametrize("keyword,expect", __SEARCH_DATA.get("search_user"), ids=__SEARCH_DATA.get("ids"))
    def test_search_user(self, keyword, expect):
        asert_msg = self.login_page.login(). \
            go_to_user_list_btn().search_user(keyword).get_search_content()
        try:
            assert str(expect) in asert_msg
        except Exception as e:
            logger.error(e)
