import allure
import pytest

from pages import manger_url
from pages.pagein import PageIn
from tools.get_data import get_data
from tools.get_driver import GetWebDriver


@allure.feature("大师管理")
class TestAddMaster:
    __ADD_MASTER_DATA = get_data("add_master")
    __DELETE_MASTER_DATA = get_data("delete_master")

    # 初始化driver方法
    def setup(self):
        self.driver = GetWebDriver.get_web_driver(manger_url)
        self.login_page = PageIn(self.driver).get_login_page()

    # 返回登录首页
    # def teardown(self):
    #     self.login_page.log_out()
    #
    # # 关闭driver方法
    def teardown(self):
        GetWebDriver.close_driver()

    # 添加大师测试用例
    @allure.title("添加老师")
    @pytest.mark.parametrize("master_name, master_pic,master_horizontal_pic,master_vertical_pic,master_lesson_pic,"
                             "master_lesson_share_pic,"
                             "master_skill, master_share_content,"
                             "master_sort, master_bright_point, master_desc,expect",
                             __ADD_MASTER_DATA.get("add_master"),
                             ids=__ADD_MASTER_DATA.get("ids"))
    def test_add_master(self, master_name, master_pic, master_horizontal_pic, master_vertical_pic, master_lesson_pic,
                        master_lesson_share_pic,
                        master_skill, master_share_content,
                        master_sort, master_bright_point, master_desc, expect):
        assert_msg = self.login_page.login(). \
            go_to_operate_btn(). \
            click_add_master(). \
            add_master_content(master_name, master_pic, master_horizontal_pic, master_vertical_pic, master_lesson_pic,
                               master_lesson_share_pic,
                               master_skill, master_share_content,
                               master_sort, master_bright_point, master_desc). \
            add_success_msg()
        assert expect in assert_msg

    # 删除大师测试用例
    @allure.title("删除老师")
    @pytest.mark.parametrize("master_key_word,expect", __DELETE_MASTER_DATA.get("delete_master"),
                             ids=__DELETE_MASTER_DATA.get("ids"))
    def test_delete_master(self, master_key_word, expect):
        print(master_key_word)
        assert_msg = self.login_page.login(). \
            go_to_operate_btn().delete_master_by_name(master_key_word).delete_success_msg()
        assert expect in assert_msg
