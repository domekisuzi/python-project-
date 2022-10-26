import sys

import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os
import pickle


class game:
    def __init__(self, BT, img, name, message):
        self.BT = BT
        self.img = img
        self.name = name
        self.message = message

    def print_message(self):
        print(self.BT)
        print(self.img)
        print(self.name)
        print(self.message)


'''
    序列化操作,将所下载内容序列化到文件并保存起来
'''

path = 'e:/热门'


def serialization(BT, img, name, message):
    nowGame = game(BT, img, name, message)
    path = 'e:/热门'
    if not os.path.exists(path):
        os.mkdir(path)
    f = open(path+'/' + nowGame.name.strip() + '.pkl', 'wb')
    pickle.dump(nowGame, f)
    f.close()


'''
    反序列化,将下载的内容存储到对象当中
'''


def deserialization():
    files = os.listdir(path)
    games = []
    for file in files:
        f = open(path + '/' + file, 'rb')
        try:  # 异常处理,防止获取空的内容导致程序终止
            Game = pickle.load(f)
            games.append(Game)
        except BaseException as e:
            print(e)
        finally:
            f.close()
    for game in games:
        game.print_message()
    print("获得的了序列化对象有" + str(len(games)))


if __name__ == '__main__':
    right_start_time = time.time()
    driver = webdriver.Chrome(executable_path='e:/bin/chromedriver.exe')
    path = 'e:/热门'
    if not os.path.exists(path):
        os.mkdir(path)
    try:
        url = 'https://byrut.org'
        url1 = 'c'
        imgHeader = 'https://byrut.org'
        # class game:
        driver.get(url=url1)
        time.sleep(1)
        # oldWindow = webdriver.current_window_handle  #获取现有窗口
        # print('当前句柄为'+str(oldWindow))
        number = len(driver.find_elements_by_class_name('short_img'))  # 获取该页面元素个数
        count = 0

        for i in range(0, number):
            timeBegin = time.time()
            items = driver.find_elements_by_class_name('short_img')  # 每次都重新获取item对象,防止因页面跳转导致的item变化
            items[i].click()
            print('当前窗口为' + str(i))

            source = driver.page_source
            soup = BeautifulSoup(source, 'lxml')

            BT = soup.findAll('a', class_='itemdown_games')[::]
            imgDiv = soup.findAll('div', class_='poster-imgbox')[::]
            imgSrc = imgDiv[0].findAll('img')[0].get('src')
            BTUrl = None
            if BT:  # 判断BT是否为空
                BTUrl = imgHeader + BT[0].get('href')  # 种子
                print(BTUrl)
            msg = soup.findAll('div', class_='game_desc')[0].get_text()  # 介绍
            name = soup.findAll('div', class_='game_desc')[0].findAll('b')[0].string.strip()  # 名字
            # name
            imgUrl = imgHeader + imgSrc  # 图片
            print(imgUrl)
            serialization(BTUrl, imgUrl, name, msg)  # 序列化

            count += 1
            driver.back()
            timeEnd = time.time()
            print('当前一轮所花费的时间为' + str(timeBegin - timeEnd))
        right_stop_time = time.time()
        print('此次一共下载了'+str(count)+'个'+'种子')
        print('共花费了'+str(right_start_time-right_stop_time))

    except BaseException as e:
        print(e)
    finally:
        driver.quit()
