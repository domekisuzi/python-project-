import pymysql
import GetInformation

connect = pymysql.connect(host='domekisuzi.fun', user="shixun", password="123456", database="shixun")
cur = connect.cursor()


def insert_but(result):
    for i in result:
        order = i[1]
        id = eval(i[0])
        context = i[2]
        remark = i[3]
        score = i[4]
        sql = "insert ignore into but(`id`,`order`,`context`,`remark`,`score`) values(%(id)s,%(order)s ,%(context)s,%(remark)s, " \
              "%(score)s) "
        params = {'id': id, 'order': order, 'context': context, 'remark': remark, 'score': score}
        print(params)
        try:
            print(cur.execute(sql, params))
            connect.commit()
        except:
            pass
            connect.rollback()
    connect.close()


# 做了一个忽略重复项，你得把所有的东西（包括）id填进去
def insert_student(result):
    for i in result:
        name = i[0]
        way = i[1]
        id = eval(i[2])
        id_number = i[3]
        grade =  eval(i[5])
        sql = "insert ignore into student(`id`,`name`,`id_number`,`way`,`grade`) values(%(id)s,%(name)s ,%(id_number)s, %(way)s,%(grade)s)"
        params = {'id': id, 'name': name, 'id_number': id_number, 'way': way,'grade':grade}
        print(params)
        try:
            print(cur.execute(sql, params))
            connect.commit()
        except:
            connect.rollback()
    connect.close()


def insert_but_student(result):
    for i in result:
        student = i[0]
        but = i[1]
        sql = "insert ignore into student_but(`but_id`,`student_id`) values(%(but_id)s,%(student_id)s)"
        params = {'but_id': but, 'student_id': student}
        print(params)
        try:
            print(cur.execute(sql, params))
            connect.commit()
        except:
            connect.rollback()
    connect.close()

#只能一个个来，不能同时插入
# 插入学生信息
# insert_student(GetInformation.get_information_by_sheet_name(GetInformation.STUDENT))


# 插入管理信息
insert_but_student(GetInformation.get_information_by_sheet_name(GetInformation.STUDENT_BUT))

# 插入答辩信息
# insert_but(GetInformation.get_information_by_sheet_name(GetInformation.BUT))
