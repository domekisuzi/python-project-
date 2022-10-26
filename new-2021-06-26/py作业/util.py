import requests
import time
from fake_useragent import UserAgent
import os
import random
import re
def verify_one_proxy(proxy):
    u = UserAgent()
    s = requests.get("https://www.baidu.com", proxies=proxy, timeout=1000)
    print(s.status_code)
    print(s.content)
    if s.status_code == 200:
        return True
    else:
        return False
    # while 1:
    #     try:
    #
    #     except:
    #         print("fail:" + proxy)
    #         # time.sleep(1)
    #         return False


def verify_proxy_list(proxies):
    l = []
    for proxy in proxies:
        if verify_one_proxy("http://" + proxy['ip_port']):
            l.append(proxy['ip_port'])
    return l


# 获取IP伪装
def get_fake_IP():
    ip_page = requests.get(  # 获取200条IP
        'http://www.89ip.cn/tqdl.html?num=60&address=&kill_address=&port=&kill_port=&isp=')
    proxies_list = re.findall(
        r'(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)(:-?[1-9]\d*)',
        ip_page.text)

    # 转换proxies_list的元素为list,最初为'tuple'元组格式
    proxies_list = list(map(list, proxies_list))
    # 格式化ip  ('112', '111', '217', '188', ':9999')  --->  112.111.217.188:9999
    for u in range(0, len(proxies_list)):
        # 通过小数点来连接为字符
        proxies_list[u] = '.'.join(proxies_list[u])
        # 用rindex()查找最后一个小数点的位置，
        index = proxies_list[u].rindex('.')
        # 将元素转换为list格式
        proxies_list[u] = list(proxies_list[u])
        # 修改位置为index的字符为空白（去除最后一个小数点）
        proxies_list[u][index] = ''
        # 重新通过空白符连接为字符
        proxies_list[u] = ''.join(proxies_list[u])
    print("代理为" + str(proxies_list))

    # proxies = {'协议':'协议://IP:端口号'}
    # 'https':'https://59.172.27.6:38380'

    return "'" + random.choice(proxies_list) + "'"


# 获取随机User_Agent伪装
def get_fake_User_Agent():
    # 随机获取User_Agent
    ua = UserAgent()
    user_anget = ua.random
    return user_anget


# 解析网址
def get_html(url):
    headers = {
        'User-Agent': get_fake_User_Agent()
    }
    proxies = {'http': get_fake_IP()}
    print(proxies)
    resp = requests.get(url, headers=headers, proxies=proxies).status_code
    return resp

print(verify_one_proxy('http://127.0.0.1:10809'))

