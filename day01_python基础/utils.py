# 公共方法类
from selenium import webdriver


# 定义获取弹窗信息的方法
def get_tips_message():
    msg = DriverUtil.get_driver().find_element_by_class_name("layui-layer-content").text
    print("msg=", msg)
    return msg


class DriverUtil(object):
    """浏览器工具类"""

    # 定义类属性浏览器对象
    _driver = None

    # 注意: 定义为类方法,为的是调用时不用在初始化实例对象
    @classmethod
    def get_driver(cls):
        """获取驱动对象"""
        # 为了保证所有调用该方法的测试类,初始化出来的浏览器对象都是同一个
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(30)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        """关闭驱动对象"""
        # 为了防止退出时,浏览器对象并不存在,需要先执行一个判断,存在再退出
        if cls._driver is not None:
            cls._driver.quit()