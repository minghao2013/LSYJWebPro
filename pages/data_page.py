# 登录成功后的数据大屏也
import pages
from base.web_base import WebBase
from pages.agent_list_page import AgentListPage
from pages.master_list_page import MasterListPage
from pages.user_list_page import UserListPage


class DataPage(WebBase):
    # 点击进入操作也的按钮
    def go_to_operate_btn(self):
        self.expected_conditions_enable_click(pages.go_to_operate_page)
        return MasterListPage(self.driver)

    # 进入操作页的断言,用于跳转成功的断言
    def get_operate_text(self):
        return self.get_element_text(pages.operate_page)

    # 点击进入管理页面的按钮
    def go_to_user_list_btn(self):
        self.expected_conditions_enable_click(pages.go_to_operate_page)
        return UserListPage(self.driver)

    # 进入经销商列表页
    def go_to_agent_list(self):
        self.expected_conditions_enable_click(pages.go_to_operate_page)
        return AgentListPage(self.driver)
