"""
良师雅集后台管理系统的url
"""
manger_url = "http://liangshiyaji.51tests.net/admin/login/login.html"

"""
良师雅集管理后天登录信息的
"""
from selenium.webdriver.common.by import By

# 登录名(账号)
manger_login_name = By.CSS_SELECTOR, '[name="username"]'

# 密码
manger_pass = (By.CSS_SELECTOR, '[name="password"]')

# 登录按钮
login_btn = (By.CLASS_NAME, 'login-submit-button')

# 进入数据大屏页断言文本
asster_ele = (By.CLASS_NAME, "pop_title")

# 进入首页按钮
go_to_operate_page = (By.XPATH, "//*[@class='login']")

# 进入操作页成功的断言
operate_page = (By.CLASS_NAME, "welcome-message")
