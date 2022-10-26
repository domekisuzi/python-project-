from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from fake_useragent import UserAgent
import random
import re
import  json


colorList = [[
    '#ff7f50', '#87cefa', '#da70d6', '#32cd32', '#6495ed',
    '#ff69b4', '#ba55d3', '#cd5c5c', '#ffa500', '#40e0d0',
    '#1e90ff', '#ff6347', '#7b68ee', '#d0648a', '#ffd700',
    '#6b8e23', '#4ea397', '#3cb371', '#b8860b', '#7bd9a5'
    ],
    [
    '#ff7f50', '#87cefa', '#da70d6', '#32cd32', '#6495ed',
    '#ff69b4', '#ba55d3', '#cd5c5c', '#ffa500', '#40e0d0',
    '#1e90ff', '#ff6347', '#7b68ee', '#00fa9a', '#ffd700',
    '#6b8e23', '#ff00ff', '#3cb371', '#b8860b', '#30e0e0'
    ],
    [
    '#929fff', '#9de0ff', '#ffa897', '#af87fe', '#7dc3fe',
    '#bb60b2', '#433e7c', '#f47a75', '#009db2', '#024b51',
    '#0780cf', '#765005', '#e75840', '#26ccd8', '#3685fe',
    '#9977ef', '#f5616f', '#f7b13f', '#f9e264', '#50c48f'
    ]][2]

random.choice(colorList)

f = open('D:\\Compressed\\shixun_name\\part-r-00000.txt',encoding='utf-8')
name = []
for line in f:
    name.append(line.strip())
f.close()

for i in name:
    s =  {
            "name": i,
            "value": random.randint(1,1000),
            "symbolSize": random.randint(1,100),
            "draggable": 'true',
            "itemStyle": {
                "normal": {
                    "shadowBlur": 100,
                    "shadowColor": random.choice(colorList),
                    "color": random.choice(colorList)
                }
            }
        }
    q = open('name.json','a+')
    str = json.dumps(s,ensure_ascii=False)+ ",\n"
    q.write(str)
