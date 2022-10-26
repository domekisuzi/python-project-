from bs4 import BeautifulSoup
import requests

url = requests.get("http://quotes.money.163.com/1002230.html#01a02")
soup = BeautifulSoup(url.text, 'lxml')
# print(soup)
s = soup.findAll('li', class_="clearfix")
print(s)
for i in s:
    print(i)

