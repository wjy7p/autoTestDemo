
import os, sys
import jenkins
from RootPath import RootPath
import json
import requests

"""
将jenkins生成的allure报告发送到钉钉群
"""
# 获取jenkins信息
jenkins_info = sys.argv
# job_name = jenkins_info[1]
job_name = "job/site"
# sys_name = jenkins_info[2]
sys_name = "营业收费系统"
# dd_url = jenkins_info[3]
dd_url = 'https://oapi.dingtalk.com/robot/send?access_token=ca45a2dc7d075ffd2dc4561f592ec977291dd2702e6b0e097d693813119343c0'


jenkins_url = "http://10.10.15.170:30080/"
server = jenkins.Jenkins(jenkins_url, username='admin', password='admin')


job_url = jenkins_url + job_name
print(job_url)
# 获取最后一次构建数
job_last_number = server.get_info(job_name)['lastBuild']['number']
print(job_last_number)
report_url = job_url + str(job_last_number) + '/allure'
#print(22, report_url)



def send_dd():
    report_data = {}
    RootDir = os.path.dirname((__file__))
    RootDir=os.path.dirname(RootPath.getYSPlatPath()).replace("resources", "reports")

    print(RootDir)
    # RootDir = os.path.abspath(os.path.dirname((__file__)))
    # 测试使用
    f = open(RootDir+'/export/prometheusData.txt', 'r')
    for lines in f:
        for c in lines:
            launch_name = lines.strip('\n').split(' ')[0]
            num = lines.strip('\n').split(' ')[1]
            report_data.update({launch_name: num})
    f.close()
    total_num = report_data.get('launch_retries_run')
    passed_num = report_data.get('launch_status_passed')
    failed_num = report_data.get('launch_status_failed')

    if int(total_num) == 0:
        rate = 0
    else:
        rate = round(int(passed_num)/int(total_num), 4)*100


    content = {"msgtype": "text",
               "text": {
                   "content": "营销体系"+"\n"+"《" + sys_name + "》" + "接口自动化测试脚本执行完毕\n运行成功率： " + str(rate) + "%" + "\n运行总数： " + total_num + "\n通过数量： " + passed_num +
                              "\n失败数量： " + failed_num + "\n报告地址：\n" + report_url + "\n构建地址：\n" + job_url}
               }


    try:
        response = requests.post(url=dd_url, data=json.dumps(content), headers={'Content-Type': 'application/json'})
        print(response.content)
    except Exception as e:
        print("钉钉连接失败")
        print(e)


if __name__ == '__main__':
    send_dd()

