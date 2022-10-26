import json

import requests
base_url = "http://127.0.0.1:7777/shixun"
RESPONSE =  "/response"
FEEDBACK = "/feedback"
ADMIN  = "/admin"

# post_data = {"name":"公共管理员","passwd":"大数据规划部"}
# res = requests.post(url=base_url+"/admin/login",data=post_data)
# print(res.text)
# data1 = {"name":"肖砥城","passwd":"これで勝ちのは思わないよう"}
# res = requests.post(url=base_url+"/admin/insert" ,data=data1)
# print(res.text)
# post_data = {"content":"测试content","name":"肖砥城","response_id":"","pictures":""}
#
# res = requests.post(url=base_url+FEEDBACK+"/createFeedback",json=post_data)
#
post_data = {"content":"测试回复","name":"肖砥城"}
res = requests.post(url=base_url+FEEDBACK+"/responseFeedback/4",json=post_data)

# data={"id":"4"}
# res = requests.get(url=base_url+FEEDBACK+"/subAll" , params=data)

# data={"id":"4"}
# res = requests.get(url=base_url+FEEDBACK+"/delete",params=data)
print(res.text)
