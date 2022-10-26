import requests
url='http://127.0.0.1:6543/polyp/patient/query/1'
res = requests.get(url)
print(res.text)