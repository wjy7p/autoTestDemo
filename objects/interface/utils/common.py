import requests

def gettoken():
    url = "http://10.10.15.168/basicinfo/auth/login"  # 构造请求
    data = {
        "loginName": "liyaoyao",
        "password": "123456",
    }
    res = requests.post(url=url, json=data)
    token = res.json().get("resultData").get("token")
    return token

def gettoken_170():
    url = "http://10.10.15.170/basicinfo/auth/login"  # 构造请求
    data = {
        "loginName": "liyaoyao",
        "password": "Lyy123456",
    }
    res = requests.post(url=url, json=data)
    token = res.json().get("resultData").get("token")
    return token

def gettoken_ys11():
    url = "http://10.10.15.205/main/auth/oauth/token"
    data = {
        "loginName": "admin",
        "password": "123456",
    }
    res = requests.post(url=url, json=data)
    token = res.json().get("resultData").get("token")
    return token



