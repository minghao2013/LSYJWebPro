from selenium.webdriver.common.by import By

from base.web_base import WebBase


class AddAgentPage(WebBase):
    # 经销商
    __AGENT_TYPE_TAG = (By.CSS_SELECTOR, '[name="agent_type_id"]')
    # 选择个代经销商
    __PERSONAL_AGENT_TAG = (By.XPATH, '//*[text()="个代"]')
    # 经销商身份法人或者自然人
    __AGENT_JURIDICAL_OR_NATURAL = (By.XPATH, '//input[@value="2" and @class="agent_style"]')
    # 选择省份
    __PROVINCE_TAG = (By.ID, "province_id")
    # 选择省份的值
    __PROVINCE_VALUE_TAG = (By.CSS_SELECTOR, '#province_id [value="4"]')
    # 选择城市省份
    __CITY_TAG = (By.ID, "city_id")
    # 选择城市的值
    __CITY_VALUE_TAG = (By.CSS_SELECTOR, '#city_id [value="75"]')
    # 姓名
    __REAL_NAME = (By.CSS_SELECTOR, "[name='real_name']")
    # 手机号码
    __PHONE_NUMBER = (By.CSS_SELECTOR, '[name="mobile"]')
    # 经销商有效期
    __AGENT_DATE = (By.CSS_SELECTOR, '[name="end_date"]')
    # 经销商有效时间为两年
    __AGENT_END_DATE = (By.XPATH, '//option[text()="二年"]')
    # 登录密码
    __AGENT_PASS = (By.CSS_SELECTOR, '[name="password"]')
    # 是否付清代理费用
    __IS_FU_SCRIPT = "document.querySelector('[name=\"is_fu\"]').click()"  # (By.CSS_SELECTOR, ['])
    # 加成功提示信息
    __ADD_SUCCESS_MSG = (By.CLASS_NAME, "toast-message")
    __ADD_BTN = (By.XPATH, '//a[text()="确 定"]')

    def set_agent_content(self, user_name, phone_num):
        """
        设置添加经销的信息
        :param user_name: 用户名
        :param phone_num: 手机号码
        :return: self
        """
        # 点击经销商类型下拉列表
        self.do_click(self.__AGENT_TYPE_TAG)
        # 选择个代
        self.do_click(self.__PERSONAL_AGENT_TAG)
        # 选择自然人
        self.do_click(self.__AGENT_JURIDICAL_OR_NATURAL)
        # 点击省份选择
        self.do_click(self.__PROVINCE_TAG)
        self.do_click(self.__PROVINCE_VALUE_TAG)
        # 选择省份和城市
        self.do_click(self.__CITY_TAG)
        self.do_click(self.__CITY_VALUE_TAG)
        # 填写姓名
        self.do_send_keys(self.__REAL_NAME, user_name)
        # 填写电话
        self.do_send_keys(self.__PHONE_NUMBER, phone_num)
        # 选择经销商权限有效期
        self.do_click(self.__AGENT_DATE)
        self.do_click(self.__AGENT_END_DATE)
        # 填写登录密码
        self.do_send_keys(self.__AGENT_PASS, "123456")
        # 选择是否支付代理费
        self.do_execute_script(self.__IS_FU_SCRIPT)
        # 点击确定按钮
        self.do_click(self.__ADD_BTN)
        return self

    # 获取添加成功的msg
    def get_tip_msg(self):
        msg = self.get_element_text(self.__ADD_SUCCESS_MSG)
        return msg
