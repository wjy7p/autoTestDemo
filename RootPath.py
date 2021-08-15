import os


class RootPath:
  
    @classmethod
    def getYSPlatPath(cls):
        """
        获取测试资源地址
        """
        return os.path.join(RootPath.getRootPath(), "resources/interface/YS/")


if __name__ == '__main__':
    res = RootPath.getYSPlatPath()
    print(res)
