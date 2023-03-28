from selenium.webdriver.common.by import By

"""
良师雅集后台管理系统的url
"""
manger_url = "http://liangshiyaji.51tests.net/admin/login/login.html"

"""
良师雅集管理后天登录信息的
"""

search_master_name = ""

# 登录名(账号)
manger_login_name = By.CSS_SELECTOR, '[name="username"]'

# 密码
manger_pass = (By.CSS_SELECTOR, '[name="password"]')

# 登录按钮
login_btn = (By.CLASS_NAME, 'login-submit-button')

# 密码错误提示信息
username_error_msg_tag = (By.CLASS_NAME, "toast-error")

# 账号错误提示信息
password_error_msg_tag = (By.CLASS_NAME, "toast-message")

# 进入数据大屏页断言文本
assert_ele = (By.CLASS_NAME, "pop_title")

# 进入首页按钮
go_to_operate_page = (By.XPATH, "//*[@class='login']")

# 进入操作页成功的断言
operate_page = (By.CLASS_NAME, "welcome-message")
"""
以下是大师管理的相关内容
"""
# 大师管理标签
master_manger_tag = (By.XPATH, '//*[text()="大师管理"]')
# 大师列表标签
master_list_tag = (By.XPATH, '//*[text()="大师列表"]')
# 大师搜索页开始时间
master_search_start_date_tag = (By.XPATH, '//*[@name="start_date"]')
# 大师搜索页结束时间
master_search_end_date_tag = (By.XPATH, '//*[@name="end_date"]')
# 大师搜索页状态
master_search_status_tag = (By.XPATH, '//*[@name="status"]')
# 大师搜索页课程类别
master_search_class_type_tag = (By.XPATH, '//*[@name="lessons_type"]')
# 新增大师按钮
master_add_tag = (By.XPATH, '//*[text()=" 新 增"]')
"""
大师添加的页面信息
"""
# 大师列表页 名称
master_name_tag = (By.XPATH, '//*[@name="master_name"]')

# 设置大师头像的标签
master_pic_tag = (By.CSS_SELECTOR, "#upload_picture_cover_id #select_btn_1")

# 老师横图的图片
master_horizontal_pic_tag = (By.CSS_SELECTOR, "#upload_picture_picture_id #select_btn_1")

# 老师竖图的图片
master_vertical_pic_tag = (By.CSS_SELECTOR, "#upload_picture_picture_vertical_id #select_btn_1")

# 老师课程图片
master_lesson_pic_tag = (By.CSS_SELECTOR, "#upload_picture_lessons_cover_id #select_btn_1")

# 老师课程分享图片
master_lesson_share_pic_tag = (By.CSS_SELECTOR, "#upload_picture_share_img #select_btn_1")

# 老师领域内容
master_skill_tag = (By.CSS_SELECTOR, "[name='skill_area']")

# 老师分享内容
master_share_content_tag = (By.CSS_SELECTOR, '[name="share_statement"]')

# 老师课程排序值
master_sort_tag = (By.CSS_SELECTOR, '[name="sort"]')

# 老师课程亮点
master_bright_point_tag = (By.CSS_SELECTOR, '[name="bright_point"]')

# 老师课程介绍
master_desc_tag = (By.CSS_SELECTOR, '[name="master_desc"]')

# 老师添加成功提示信息
master_add_success_msg = (By.CLASS_NAME, "toast-message")

# 线上课checkbox
master_add_online_tag = (By.XPATH, "//*[@value='1']")  # 这个元素上面可能有遮罩,用js点击试一下就好了

# 确定按钮
master_add_btn = (By.CSS_SELECTOR, '.btn-save-subject')

"""
一下是删除的标签
"""
# 大师搜索关键字
search_keyword_tag = (By.CLASS_NAME, "search-input")

# 搜索按钮
search_btn = (By.XPATH, "//a[text()='搜索']")

# 删除按钮
delete_btn_tag = (By.XPATH, "//*[contains(text(),'删 除')]")

# 登出的标签
sign_out_tag = (By.CSS_SELECTOR, '.logout')
