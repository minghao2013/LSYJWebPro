from selenium.webdriver.common.by import By

from base.web_base import WebBase
from pages.add_agent_page import AddAgentPage


class AgentListPage(WebBase):
    # 经销商管理标签
    __AGENT_MANGER_TAG = (By.XPATH, '//*[text()="经销商管理"]')

    # 经销商列表标签
    __AGENT_LIST_TAG = (By.XPATH, '//*[text()="经销商列表"]')

    # 搜索关键字
    __SEARCH_KEY_WORD = (By.CSS_SELECTOR, "[name='name']")

    # 新增经销商按钮
    __ADD_AGENT_BTN = (By.XPATH, '//*[text()=" 新 增"]')

    # 经销商搜索keyweord
    __KEY_WORD = (By.CSS_SELECTOR, '[name="name"]')

    # 搜索按钮
    __SEARCH_BTN = (By.ID, "search")

    # 搜索经销商的搜索结果
    __SEARCH_RESULT_SCRIPT = "return document.querySelector(\".table-bordered tbody\").innerText"

    # 打开经销商列表页面
    def goto_agent_list(self):
        self.do_click(self.__AGENT_MANGER_TAG)
        self.do_click(self.__AGENT_LIST_TAG)
        return self

    # 跳转添加经销商页面
    def goto_add_agent_page(self):
        self.do_click(self.__ADD_AGENT_BTN)
        return AddAgentPage(self.driver)

    # 搜索经销商
    def search_agent(self, key_word):
        self.do_send_keys(self.__KEY_WORD, key_word)
        self.do_click(self.__SEARCH_BTN)
        return self

    # 获取搜索结果
    def get_search_result(self):
        msg = self.do_return_execute_script(self.__SEARCH_RESULT_SCRIPT)
        return msg
