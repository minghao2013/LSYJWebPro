# 登录成功后的数据大屏也

import pages
from base.base import Base


class DataPage(Base):
    # 点击进入操作也的按钮
    def go_to_operate_btn(self):
        self.expected_conditions_enable_click(pages.go_to_operate_page)

    # 进入操作页的断言,用于跳转成功的断言
    def get_operate_text(self):
        return self.get_element_text(pages.operate_page)

    # 业务流程方法
    def go_to_operate_page(self):
        self.go_to_operate_btn()
