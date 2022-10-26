'''
    made by @domekisuzi
    2022/3/26
'''
import os
import requests
from bs4 import BeautifulSoup
import re

'''
    全局变量,其中header为头部,headerStr为处理字符串使用的头部,url为北京大学计算机院士的界面
'''

header = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Mobile Safari/537.36'}
url = "http://cs.pku.edu.cn/szdw1/ys.htm"  # 所有院士页面
headerStr = "http://cs.pku.edu.cn"
res = requests.get(url=url, headers=header)
res.encoding = 'UTF-8'
soup \
    = BeautifulSoup(res.text, 'lxml')
path = 'E:/python作业数据'
'''
    获取院士详细信息的url,方便进行跳转进一步得到院士的详细信息,得到的信息是../info/1208/1731.htm形式,需要去除前面的..
'''
def getDetailURL():
    details = set()
    detail = soup.findAll('li',id=re.compile('line_'))[0].findAllNext('div',class_='pic')[0].findAllNext('a')
    for i in detail:
        if re.match('../',i.get('href')):
            details.add(headerStr + i.get('href')[1:])
    # print(details)#打印所有院士的详细信息的URL列表
    return details
'''
    根据所给出的URL,获取所有院士的详细信息并将其写入文本
'''

def getDetails(urls):
    if not os.path.exists(path):
        os.mkdir(path)
    for i in urls:
        content =""
        res = requests.get(url=i, headers=header)
        res.encoding = 'UTF-8'#指定编码方式为utf-8
        soup = BeautifulSoup(res.text,'lxml')
        # 获取名字
        name = soup.findAll('div', class_=re.compile('M2_1R$'))[0].findAll('h1')[0].string
        print(name)
        content+=name+'\n'
        # 获取详细信息
        res = soup.findAll('div', class_=re.compile('M2_1R$'))[::]
        for i in res:
            # print(i)
            # print(p)#获取整个详细信息所在tags
            p = i.findAll('p')
        for i in p:
            if (i.string != None):
                print(i.string)
                content+=i.string+'\n'
        information = soup.findAll('span')[::]
        for i in information:
            if i.string != None:
                print(i.string,'')
                content+=i.string
        with open(path+'/'+name+".txt",'w',encoding='utf-8') as file:#以utf-8的形式写入文件
            file.write(content)
        # print(content)

def downLoadPictures():
    #若没有该文件夹,则创建文件
    if not os.path.exists(path):
        os.mkdir(path)
    # 查找院士
    teachers = []
    names = soup.findAll('div', class_='txt')[0].findAllNext('h4')
    for i in names:
        teachers.append(i.string)
    # 查找图片
    imagesList = []
    images = soup.findAll('div', class_='pic')[0].findAllNext('img')
    for i in images:
        if (re.match('/__', i.get('src'))):
            imagesList.append('http://cs.pku.edu.cn' + i.get('src'))
            # print(i.get('src'))#打印未经处理的图片的URL
    dict = {}
    for i in range(0, 6):
        dict[teachers[i]] = imagesList[i]
    # print(dict)#打印人物与图片相对应的字典
    # 下载对应图片,并将图片与文字一一对应
    for i in dict.keys():
        r = requests.get(dict[i])
        with open(path+'/'+ i + '.png', 'wb') as f:
            f.write(r.content)



if __name__ == '__main__':
    details = getDetailURL()
    getDetails(details)
    downLoadPictures()

