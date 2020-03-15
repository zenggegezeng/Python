from day01_python基础.utils import DriverUtil
class MusicPlayer(object):
    #全局变量
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        # 如果不返回任何结果，
        return cls._instance

    def __init__(self):
        print("初始化⾳乐播放对象")


player1 = MusicPlayer()

player2 = MusicPlayer()
print(player1)
print(player2)

driver1 = DriverUtil.get_driver()
print(driver1)
driver2 = DriverUtil.get_driver()
print(driver2)


