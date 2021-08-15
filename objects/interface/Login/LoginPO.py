import allure
from objects.interface.baseObjects.BaseObj import BaseObj
from objects.interface.utils.DBRequest import *
from RootPath import RootPath
from configparser import ConfigParser
import json

class LoginPO(BaseObj):
    def geturl_prefix(self):
        url_prefix =self.getParas(yamlName='YS/HomePage.yml', key='170服务器接口地址', paraName='url')
        #print(url_prefix)
        return url_prefix

    @allure.step("用户登录，获取token")
    # 获取token
    def getToken(self, **kwargs):
        """
        获取token值
        """
        url = "http://10.10.15.205:17000/auth/oauth/token"
        body = {"username": kwargs["username"], "password": kwargs["password"], "grant_type": "password"}
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': "Basic MjI5MTdkYjEyZWY0NTBkNWNjMDJiNTBjNWJiN2I2NTU6d3BnQDIwMjA="}
        try:
            response = self.do_post(url=url, params=body, headers=headers)
            return response
        except Exception as e:
            print("获取token失败")
            print(e)
    '''
    @allure.step("通过token进行登录")
    # 获取token
    def loginByToken(self, **kwargs):
        url = self.geturl_prefix() + "/cdwcenterapi/sso/loginByToken"
        body = {"loginName": kwargs["loginName"], "password": kwargs["password"], "token":  kwargs["token"]}
        try:
            response = self.do_post(url=url, params=body)
            token = response["resultData"]["token"]
            return token
        except Exception as e:
            print("登录失败")
            print(e)
    '''

    @allure.step("用户登出")
    # 用户登出
    def logout(self, token):
        url = self.geturl_prefix()+"/auth/loginOut"
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        try:
            res = self.do_get(url=url, header=headers)
            return res
        except Exception as e:
            print(e)

    def get_DB_data(self, sql) -> list:
        """
        根据sql获取数据库的值
        """
        ini_file = RootPath.getInterfaceIniPath() + "YS_GG/YS_v11.ini"
        content = ConfigParser()
        content.read(ini_file)
        db_info = content.get("INFO", "db_info")
        db_info = json.loads(db_info)
        return db_query(db_info["waterdb_ys"], sql)

