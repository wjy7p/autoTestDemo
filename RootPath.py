import os


class RootPath:
    @classmethod
    def getRootPath(cls):
        return os.path.dirname(os.path.abspath(__file__))

    @classmethod
    def getWebIniPath(cls):
        return os.path.join(RootPath.getRootPath(), "resources/webpage/baidu/baidu.ini")

    @classmethod
    def getInterfaceIniPath(cls):
        return os.path.join(RootPath.getRootPath(), "resources/interface/")

    @classmethod
    def getDrinkWaterInterfaceIniPath(cls):
        """
        获取直饮水资源地址
        """
        return os.path.join(RootPath.getRootPath(), "resources/interface/DrinkWater/")

    @classmethod
    def getDrinkWaterInterfacefilePath(cls):
        """
        获取用水户导入文件的文件地址
        """
        return os.path.join(RootPath.getRootPath(), "cases/interface/DrinkWater/")

    @classmethod
    def getDevicePlatPath(cls):
        """
        获取设备平台资源地址
        """
        return os.path.join(RootPath.getRootPath(), "resources/interface/DevicePlat/")

    @classmethod
    def getPublicPlatPath(cls):
        """
        获取公共平台资源地址
        """
        return os.path.join(RootPath.getRootPath(), "resources/interface/PublicPlat/")

    @classmethod
    def getYSPlatPath(cls):
        """
        获取公共平台资源地址
        """
        return os.path.join(RootPath.getRootPath(), "resources/interface/YS/")


if __name__ == '__main__':
    res = RootPath.getYSPlatPath()
    print(res)
