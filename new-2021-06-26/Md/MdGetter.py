import os
import pymysql

connect = pymysql.connect(host='domekisuzi.fun', user="shixun", password="123456", database="shixun")
cur = connect.cursor()
result = []


class Note:
    def __init__(self, title, context, label):
        self.title = title
        self.context = context
        self.label = label

    def __str__(self):
        return self.title + ":"+self.label


# 把md文件塞进数据库的小代码
def getAlldirInDiGui(path):
    filesList = os.listdir(path)
    # print(filesList)
    for fileName in filesList:
        # print(fileName)
        fileAbpath = os.path.join(path, fileName)
        # 如果是文件夹，则进行递归
        # print(fileAbpath)
        tmp = fileName.split('.')
        if os.path.isdir(fileAbpath):
            getAlldirInDiGui(fileAbpath)
        elif len(tmp) == 2:
            if tmp[1] == 'md':
                # print(fileName)
                f = open(fileAbpath, 'r', encoding='utf-8')
                # 内容
                try:
                    context = f.read()
                    # print(context)
                    # 标签
                    label = fileAbpath.split('\\')[-2]
                    # 标题
                    title = tmp[0]
                    t = Note(title, context, label)
                    print(t)
                    result.append(t)
                    f.close()
                except:
                    print("--------------")
                    print(fileName)
                    print("--------------")
def insert_result(result):
    for i in result:
        print(i)
        title = i.title
        context = i.context
        label = i.label
        sql = 'insert ignore into note(`context`,`title`,`label`) values(%(context)s,%(title)s,%(label)s)'
        params = {'context': context, "label": label, "title": title}
        try:
            print(cur.execute(sql, params))
            connect.commit()
        except:
            connect.rollback()

getAlldirInDiGui('E:\\OneDrive - stu.csust.edu.cn\\文档\\typora data')
insert_result(result)