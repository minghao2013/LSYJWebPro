from selenium import webdriver


class GetDriver:
    # 声明web_driver变量
    __web_driver: webdriver = None

    # app_driver定义
    __app_driver = None

    # 初始化driver
    @classmethod
    def get_web_driver(cls, url):
        if cls.__web_driver is None:
            cls.__web_driver = webdriver.Chrome()
            cls.__web_driver.maximize_window()
            cls.__web_driver.implicitly_wait(5)
            cls.__web_driver.get(url)
        return cls.__web_driver

    # 关闭driver
    @classmethod
    def close_driver(cls):
        if cls.__web_driver is not None:
            cls.__web_driver.quit()
            cls.__web_driver = None


