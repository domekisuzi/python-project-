import xlrd
import pandas as pd
from functools import reduce

path = 'E:/OneDrive - stu.csust.edu.cn/桌面/答辩结果表.xlsx'
# path =  "https://docs.qq.com/sheet/DZVltSWFnSXFzUFZn?fileMD5=6563316533313766623837323239333262646235653833306431326336386366&chatId=429800269&chatType=2&groupUin=n%25252FoKBLXSVopyNhFEhJ3aMQ%25253D%25253D&ADUIN=1076839874&ADSESSION=1659595600&ADTAG=CLIENT.QQ.5905_.0&ADPUBNO=27230&tab=BB08J3&u=86b0257247f84b399757f0669ecf0076"
worksheet = xlrd.open_workbook(path)

# 学生sheet内容
STUDENT = "Sheet1"
# 答辩内容
BUT = "Sheet2"
# 答辩，学生关联表
STUDENT_BUT = "Sheet3"
START_ROW = 1

def get_student_information():
    student = worksheet.sheet_by_name(STUDENT)
    name = student.col_values(0, START_ROW)
    way = student.col_values(1, START_ROW)
    id = student.col_values(2, START_ROW)
    id_number = student.col_values(3, START_ROW)

    # map,把所有的信息都缝合起来
    s = map(lambda x, y, z, q: (x, y, z, q), name, way, id, id_number)
    result = []
    for i in s:
        result.append(i)
    return result

# 获得信息元祖
def get_information_by_sheet_name(sheet_name):
    sheet = worksheet.sheet_by_name(sheet_name)
    cols_number = sheet.ncols
    content = []
    for x in range(0, cols_number):
        content.append(sheet.col_values(x, START_ROW))
    # map,把所有的信息都缝合起来,多序列,把信息用，连接成字符串，后面通过split分割为元祖
    s = reduce(lambda x, y: map(lambda a, b: str(a) + "," + str(b), x, y), content)

    result = []
    for i in s:
        result.append(tuple(i.split(",")))
    print(result)
    return result


# 获取所有人名字
def get_name():
    df = pd.read_excel(path)
    df_li = df.values.tolist()
    results = []
    for s_li in df_li:
        results.append(s_li[0])
    print(results)
    return results


# get_student_information()
# get_name()
# get_information_by_sheet_name(STUDENT)
get_information_by_sheet_name(BUT)
# get_information_by_sheet_name(STUDENT_BUT)