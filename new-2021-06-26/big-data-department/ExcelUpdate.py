import xlrd
from openpyxl import load_workbook
from functools import reduce


path = 'D:/答辩结果表.xlsx'
#用于读
worksheet = xlrd.open_workbook(path)
#用于写入
workbook = load_workbook(path)

# 学生sheet内容
STUDENT = "Sheet1"
# 答辩内容
BUT = "Sheet2"
STUDENT_BUT = "Sheet3"
START_ROW = 1


# 应该从数据库上查找比较方便,从单元表里扣，并且写入数据
def update_sheet3():
    student = worksheet.sheet_by_name(STUDENT)
    name = student.col_values(0, START_ROW)
    student_id = student.col_values(2, START_ROW)
    s = dict(zip(name, student_id))
    print(s)
    but = worksheet.sheet_by_name(BUT)
    but_id = but.col_values(0, START_ROW)
    but_name = but.col_values(5, START_ROW)
    q = list(zip(but_id, but_name))
    print(q)
    result = []
    # 获取result元祖，前面为学号，后面为答辩id
    for i in q:
        tmp = str(i[1]).strip()
        if tmp in s.keys():
            student_idd = s[tmp]
            but_idd = i[0]
            result.append((student_idd, but_idd))
    print(result)
    sheet3 = workbook[STUDENT_BUT]
    for i in result:
        print(list(i))
        sheet3.append(list(i))
    workbook.save(path)


update_sheet3()
