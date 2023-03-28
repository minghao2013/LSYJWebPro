from selenium.webdriver.common.by import By

from base.web_base import WebBase
from js_ele import vip_user_view_date


class AddVIPUserPage(WebBase):

    # 添加VIP用户页面
    def add_user_content(self, nick_name, phone_number, e_mail, view_date):
        self.do_send_keys((By.CSS_SELECTOR, '[name="nickname"]'), nick_name)
        self.do_click((By.ID, "province_id"))
        self.do_click((By.CSS_SELECTOR, '[value="4"]'))
        self.do_click((By.ID, "city_id"))
        self.do_click((By.CSS_SELECTOR, '[value="75"]'))
        self.do_send_keys((By.CSS_SELECTOR, "[name='mobile']"), phone_number)
        self.do_send_keys((By.CSS_SELECTOR, "[name='email']"), e_mail)
        self.do_send_keys((By.CSS_SELECTOR, "[name='password']"), "123456")
        self.do_execute_script(vip_user_view_date)
        self.do_send_keys((By.CSS_SELECTOR, '[name="recommend_mobile"]'), "19526201239")
        self.do_click((By.CSS_SELECTOR, '[data-style="slide-up"]'))
        return self

    # 获取添加普通用户成功的提示
    def get_add_success_msg(self):
        msg = self.get_element_text((By.CLASS_NAME, "toast-message"))
        return msg
