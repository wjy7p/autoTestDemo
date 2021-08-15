import allure

from RootPath import RootPath
from objects.interface.Login.LoginPO import LoginPO
import pytest

from objects.interface.utils.PropertiesUtil import *


@allure.feature("系统登录测试")
class TestLogin(LoginPO):

    public_path = RootPath.getYSPlatPath() + "/PublicCase.yml"
    pos_logincase = PropertiesUtil.loadLocatorValueFromYml(path=public_path, key="positive_logincase")
    neg_logincase = PropertiesUtil.loadLocatorValueFromYml(path=public_path, key="negative_logincase")

    @pytest.mark.parametrize("positive", pos_logincase)  # 参数化，每组参数独立运行一次
    @allure.story("登录成功")
    def test_posilogin(self, positive):
        res = self.getToken(**self.pos_logincase[positive])  # **字典，*元组
        # 断言请求状态
        assert res["status"] == 'complete'
        return res
        # 断言数据库
        # sql = "select * FROM org_user where login_name = '%s'" % self.pos_logincase[positive]["loginName"]
        # db_result = self.get_DB_data(sql=sql)
        # print(db_result)
        # assert db_result[0]["login_name"] == self.pos_logincase[positive]["loginName"]

    @pytest.mark.parametrize("negative", neg_logincase)
    @allure.story("登录失败")
    def test_negalogin(self, negative):
        res = self.getToken(**self.neg_logincase[negative])
        # 断言请求状态
        assert res["status"] == 'error'




