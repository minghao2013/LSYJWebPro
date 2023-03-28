from selenium.common import JavascriptException

import pages
from base.base import Base
from tools.logs_utils import logger


class WebBase(Base):

    # 上传按钮的封装 upload_file这个元素不支持clear  需要单独封装上传的方法
    def upload_file(self, by, send_text):
        self.do_find_element(by).send_keys(send_text)

    # 执行js无返回值的
    def do_execute_script(self, script):
        try:
            self.driver.execute_script(script)
        except Exception as e:
            logger.error("执行javascript错误{}".format(script))
            raise Exception

    # 执行js有返回值的
    def do_return_execute_script(self, script):
        try:
            return self.driver.execute_script(script)
        except JavascriptException as e:
            logger.error("执行javascript错误{}".format(script))
            print("这里异常报错!")

    # 切换到弹窗页面
    def switch_to_alter(self):
        self.driver.switch_to.alert.accept()

    # 退出登录
    def log_out(self):
        self.do_click(pages.sign_out_tag)
