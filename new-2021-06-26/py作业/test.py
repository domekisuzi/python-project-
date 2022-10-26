import os
import time

import requests
from bs4 import BeautifulSoup
import re
import pickle
from selenium import webdriver

'''
1信息序列化
2代码运行过程中(try catch)不停,
3爬取一定数量的信息
4把握好休眠时间
5熟练运用爬虫
'''
class game:
    def __init__(self, BT, img, name, message):
        self.BT = BT
        self.img = img
        self.name = name
        self.message = message


header = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Mobile Safari/537.36'}
# Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Mobile Safari/537.36
# url = "https://byrut.org/page/12/"
url = "https://byrut.org/25156-9-nine-newepisode.html"
base_url = 'https://byrut.org/page/860/'
res = requests.get(url=base_url, headers=header)
soup = BeautifulSoup(res.text, 'lxml')


# #获取一页中所有游戏的url   具体到页
# onePage = []
# name =  soup.findAll('div',class_='short_img')
# for i in name:
#         urls = i.findAll('a')[0].get('href')
#         onePage.append(urls)
# print(onePage)

# 具体到细节,获取单个游戏的详细信息
# msg = soup.findAll('div', class_='game_desc')[0].get_text()  # 介绍
# name = soup.findAll('div', class_='game_desc')[0].findAll('b')[0].string.strip() # 名字
#
# print(msg,name)

# 具体到细节,获取单个游戏的详细信息

def get_name_information_and_serialization(game_information_soup):
    msg = ''
    name = ''
    imgSrc = ''
    imgHeader = 'https://byrut.org'
    BT = ''
    try:
        msg = game_information_soup.findAll('div', class_='game_desc')[0].get_text()  # 介绍
    except IndexError:
        print(IndexError, '当前游戏没有介绍')
    try:
        name = game_information_soup.findAll('div', class_='game_desc')[0].findAll('b')[0].string.strip().replace(':',
                                                                                                                  '-').replace(
            '/', '-').replace('?', '-').replace('*', '-')  # 名字,处理掉中间带冒号的游戏,防止产生奇怪的错误,!!记得做笔记
    except IndexError:
        print(IndexError, '当前游戏没有名字')
    except AttributeError:
        print(AttributeError, '当前游戏没有名字')
    try:
        BT = game_information_soup.findAll('a', class_='itemdown_games')[::]
    except IndexError:
        print(IndexError, '当前游戏没有种子')
    try:
        imgDiv = game_information_soup.findAll('div', class_='poster-imgbox')[::]
        imgSrc = imgDiv[0].findAll('img')[0].get('src')
    except IndexError:
        print(IndexError, '当前游戏没有图片')
    BTUrl = ''
    if BT:  # 判断BT是否为空,无种子则无需存储该游戏
        try:
            BTUrl = imgHeader + BT[0].get('href')  # 种子
        except IndexError:
            print(IndexError, '当前游戏种子格式特殊')
            print(BTUrl)
        serialization(BT=BTUrl, img=imgSrc, name=name, message=msg)


# #获取一页中所有游戏的url   具体到页
def get_game_url(page_soup):
    onePage = []
    name = page_soup.findAll('div', class_='short_img')
    for i in name:
        try:
            urls = i.findAll('a')[0].get('href')
            onePage.append(urls)
        except IndexError:
            print(IndexError, '当前游戏没有对应的url')

    return onePage


# 获取某一页的页数
def print_current_page(page_soup):
    try:
        page = page_soup.findAll('span', class_='page-navi')[0].findAll('span', class_='')[0].string
        print('当前页数为' + str(page))
    except IndexError:
        print(IndexError, '页面获取获取失败')


def serialization(BT, img, name, message):
    nowGame = game(BT, img, name, message)
    path = 'e:/热门'
    if not os.path.exists(path):
        os.mkdir(path)
    try:
        f = open((path + '/' + nowGame.name.strip() + '.pkl'), 'wb')
        try:
            pickle.dump(nowGame, f)
        except BaseException as e:
            print(e)
            print('游戏' + name + '在序列化途中发生异常')
        finally:
            f.close()
    except FileNotFoundError:
        print("游戏中出现了/导致路径创建错误")
    except BaseException:
        print("创建路径时出现了其他错误")


def request_block(url):
    while True:
        try:
            return requests.get(url=url, headers=header, timeout=20)
        except requests.exceptions.ConnectionError:
            print("断网,正在尝试连接..." + str(url))
            time.sleep(3)
        except:
            print("未知错误,正在尝试连接" + str(url))
            time.sleep(3)


# 最外层循环,用于获取每一页的数据
next_page_url = '第一个'
next_page_url_set = set()
next_page_url_set.add(base_url)
next_page_soup = soup
all_start_time = time.time()

try:
    while next_page_url:
        once_start_time = time.time()
        next_page_url = next_page_soup.findAll('div', class_='bottom-page clearfix')[0].findAll('a')[-1].get(
            'href')  # 获取下一页的url
        game_url = get_game_url(page_soup=next_page_soup)  # 获取该页所有游戏url
        for i in game_url:
            time.sleep(1)
            game_re = request_block(i)
            game_soup = BeautifulSoup(game_re.text, 'lxml')
            get_name_information_and_serialization(game_information_soup=game_soup)  # 对游戏信息进行序列化
        # 切换到下一页url
        if next_page_url_set.__contains__(next_page_url):
            print('已经到了最后一页了')
            break
        else:
            next_page_url_set.add(next_page_url)
        next_page_result = request_block(next_page_url)
        next_page_soup = BeautifulSoup(next_page_result.text, 'lxml')
        time.sleep(1)
        once_stop_time = time.time()
        print_current_page(next_page_soup)
        print('该轮所使用时间为' + str(once_start_time - once_stop_time))
except IndexError as e:
    print(e)
except BaseException:
    print(BaseException)
finally:
    all_stop_time = time.time()
    print('运行结束,总共花费时间为' + str(all_start_time - all_stop_time))



# 178
# my_url = 'https://byrut.org/24935-operation-lovecraft-fallen-doll.html'
# res = requests.get(my_url,headers=header)
# game_information_soup = BeautifulSoup(res.text,'lxml')
# name = game_information_soup.findAll('div', class_='game_desc')[0].findAll('b')[0].string.strip().replace(':','-').replace('/','-')# 名字
# print(name)
# serialization('','yy',name,'')
