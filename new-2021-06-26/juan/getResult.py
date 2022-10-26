# class Student:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#
#     def __repr__(self):
#
#         return self.name+":"+self.score
#
# res = []
# with open("./score.txt",encoding='utf-8') as file_object:
#       # line =  file_object.readline()
#       for line in file_object:
#         res.append(Student (line.split(" ")[1],line.split(" ")[2]))
#
#
# res.sort(key=lambda  x: x.score)
# print(res)

# 36 + 0.68 + 0.2
# 团体：2院1校   4
# 学科 省级 机设: 省二省三 14 机器人与人工智能 省三6    院级 互联网+ 校3 院1 8
# 三下乡 2
# 献血 2
# 习惯的力量 0.68
import random


student = ["罗","寇"  ,"刘","李"]
res = []
res.append(random.sample(student,3))
res.append(random.sample(student,3))
res.append(random.sample(student,3))
print(res)
