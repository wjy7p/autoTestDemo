# coding=utf-8
import base64
import json
import requests
from RootPath import RootPath
from objects.interface.utils.PropertiesUtil import PropertiesUtil
from Crypto.Cipher import AES
import base64
from Crypto.Util.Padding import pad


class BaseObj(object):

    @staticmethod
    def do_post(url, params, headers={'Content-Type': 'application/json'}):
        try:
            response = requests.post(url, data=json.dumps(params), headers=headers)
            print("*******************************************************************************")
            print("Request: " + url)
            print(json.dumps(params))
            if response.status_code != 200:
                raise Exception("请求失败，status_code=" + str(response.status_code))
            print("-------------------------------------------------------------------------------")
            result = json.loads(str(response.content, 'utf-8'))
            print("Response: ")
            print(result)
            print("*******************************************************************************")
            return result
        except Exception as e:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(e)

    @staticmethod
    def do_postwithoutheader(url, params):
        try:
            response = requests.post(url, data=json.dumps(params))
            print("*******************************************************************************")
            print("Request: " + url)
            print(json.dumps(params))
            if response.status_code != 200:
                raise Exception("请求失败，status_code=" + str(response.status_code))
            print("-------------------------------------------------------------------------------")
            result = json.loads(str(response.content, 'utf-8'))
            print("Response: ")
            print(result)
            print("*******************************************************************************")
            return result
        except Exception as e:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(e)

    @staticmethod
    def do_paramspost(url,params,headers={'Content-Type': 'application/json'}):
        try:
            response = requests.post(url, params=params, headers=headers)
            print("*******************************************************************************")
            print("Request: " + url)
            print(json.dumps(params))
            if response.status_code != 200:
                raise Exception("请求失败，status_code=" + str(response.status_code))
            print("-------------------------------------------------------------------------------")
            result = json.loads(str(response.content, 'utf-8'))
            print("Response: ")
            print(result)
            print("*******************************************************************************")
            return result
        except Exception as e:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(e)

    @staticmethod
    def do_fielpost(url, data, headers):
        try:
            response = requests.post(url, data=data, headers=headers)
            print("*******************************************************************************")
            print("Request: " + url)
            # print(json.dumps(data))
            if response.status_code != 200:
                raise Exception("请求失败，status_code=" + str(response.status_code))
            print("-------------------------------------------------------------------------------")
            result = json.loads(str(response.content, 'utf-8'))
            print("Response: ")
            print(result)
            print("*******************************************************************************")
            return result
        except Exception as e:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(e)

    @staticmethod
    def do_post_base64encode(url, params,headers={'Content-Type': 'application/json'}):
        """
        入参base64加密，出参正常
        """
        try:
            body_str = json.dumps(params)  # 将dic转换成str
            body_b = body_str.encode("utf-8")  # 将str转换成二进制
            body_encode = base64.b64encode(body_b)  # 进行base64加密
            response = requests.post(url, data=body_encode, headers=headers)
            if response.status_code != 200:
                raise Exception("请求失败，status_code=" + str(response.status_code))
            response = response.text

            print()
            print("*******************************************************************************")
            print("Request: " + url)
            print(json.dumps(params))
            print("-------------------------------------------------------------------------------")
            result = json.loads(response)
            print("Response: ")

            print(result)

            print("*******************************************************************************")
            return result
        except Exception as e:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(e)

    @staticmethod
    def do_get(url, header={'Content-Type': 'application/json'}):
        try:
            response = requests.get(url, headers=header)
            if response.status_code != 200:
                raise Exception("请求失败，status_code=" + str(response.status_code))
            print("*******************************************************************************")
            print("Request: " + url)
            print("-------------------------------------------------------------------------------")
            result = json.loads(response.text)
            print("Response: ")
            print(result)
            print("*******************************************************************************")
            return result

        except Exception as e:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(e)

    @staticmethod
    def doparams_get(url, params, headers):
        print(params)
        try:
            response = requests.get(url, params=params, headers=headers)
            if response.status_code != 200:
                raise Exception("请求失败，status_code=" + str(response.status_code))
            print("*******************************************************************************")
            print("Request: " + url)
            print(json.dumps(params))
            print("-------------------------------------------------------------------------------")
            result = json.loads(response.text)
            # 供应链特殊处理
            # result = result[0]
            print("Response: ")
            print(result)
            print("*******************************************************************************")
            return result

        except Exception as e:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(e)

    @staticmethod
    def doparams_getwithoutheader(url, params):
        try:
            response = requests.get(url, params=params)
            if response.status_code != 200:
                raise Exception("请求失败，status_code=" + str(response.status_code))
            print("*******************************************************************************")
            print("Request: " + url)
            print(json.dumps(params))
            print("-------------------------------------------------------------------------------")
            result = json.loads(response.text)
            # 供应链特殊处理
            # result = result[0]
            print("Response: ")
            print(result)
            print("*******************************************************************************")
            return result

        except Exception as e:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(e)

    @staticmethod
    def do_get_canshu(url, params, headers):
        try:
            response = requests.get(url=url, params=json.dumps(params), headers=headers)
            if response.status_code != 200:
                raise Exception("请求失败，status_code=" + str(response.status_code))
            print("*******************************************************************************")
            print("Request: " + url)
            print("-------------------------------------------------------------------------------")
            result = json.loads(response.text)
            # # 供应链特殊处理
            # result = result[0]
            print("Response: ")
            print(result)
            print("*******************************************************************************")
            return result

        except Exception as e:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(e)


    @staticmethod
    def do_get_base64decode(url):
        try:
            response_base64 = requests.get(url)
            if response_base64.status_code != 200:
                raise Exception("请求失败，status_code=" + str(response_base64.status_code))
            response = str(base64.b64decode(response_base64.text, ), 'utf-8')
            print("*******************************************************************************")
            print("Request: " + url)
            print("-------------------------------------------------------------------------------")
            result = json.loads(response)
            print("Response: ")
            print(result)
            print("*******************************************************************************")
            return result
        except Exception as e:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(e)

    @staticmethod
    def getParas(yamlName, key, paraName=None):
        '''
        读取yaml文件具体参数值,
        path,key必填，
        para不传时会把key下面所有参数获取(返回字典类型)，para传值会返回参数对应的值
        '''
        path = RootPath.getInterfaceIniPath()
        Parameter = PropertiesUtil.loadLocatorValueFromYml(path=path + yamlName, key=key, para=paraName)
        return Parameter

    @staticmethod
    def do_post_base64decode(url, params, headers={'Content-Type': 'application/json'}):
        """
        入参正常，出参base64加密
        """

        try:
            response_base64 = requests.post(url, data=json.dumps(params), headers=headers)
            if response_base64.status_code != 200:
                raise Exception("请求失败，status_code=" + str(response_base64.status_code))
            response = str(base64.b64decode(response_base64.content, ), 'utf-8')
            print()
            print("*******************************************************************************")
            print("Request: " + url)
            print(json.dumps(params))
            print("-------------------------------------------------------------------------------")
            result = json.loads(response)
            print("Response: ")

            print(result)

            print("*******************************************************************************")
            return result
        except Exception as e:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(e)

    @staticmethod
    def do_put(url, params, headers) -> dict:
        try:
            print("*******************************************************************************")
            print("Request: " + url)
            response = requests.put(url, json=params,headers=headers)
            if response.status_code != 200:
                raise Exception("请求失败，status_code=" + str(response.status_code))
            print("-------------------------------------------------------------------------------")
            print("Response: ")
            print(response.json())
            print("*******************************************************************************")
            return response.json()
        except Exception as e:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(e)

    @staticmethod
    def do_delete(url, headers) -> dict:
        try:
            print("*******************************************************************************")
            print("Request: " + url)
            response = requests.delete(url,headers=headers)
            if response.status_code != 200:
                raise Exception("请求失败，status_code=" + str(response.status_code))
            print("-------------------------------------------------------------------------------")
            print("Response: ")
            print(response.json())
            print("*******************************************************************************")
            return response.json()
        except Exception as e:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(e)

    @staticmethod
    def do_deleteparams(url, headers={'Content-Type': 'application/json'}):
        try:
            response = requests.delete(url, headers=headers)
            print("*******************************************************************************")
            print("Request: " + url)
            if response.status_code != 200:
                raise Exception("请求失败，status_code=" + str(response.status_code))
            print("-------------------------------------------------------------------------------")
            result = json.loads(str(response.content, 'utf-8'))
            print("Response: ")
            print(result)
            print("*******************************************************************************")
            return result
        except Exception as e:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(e)


    @staticmethod
    # 加密
    def aes_ecb_encrypt_text(decrypt_text, key):
        """
        加密AES_ECB明文
        :param decrypt_text: 待加密的字符串
        :param key: 密钥
        :return:  加密后的数据
        """
        aes2 = AES.new(key.encode('utf-8'), AES.MODE_ECB)
        encrypt_text = aes2.encrypt(pad(decrypt_text.encode('utf-8'), AES.block_size, style='pkcs7'))
        encrypt_text = str(base64.encodebytes(encrypt_text), encoding='utf-8').replace("\n", "")
        return encrypt_text

