from tkinter import W
import pandas as pd
import os

# -------------view


def displayNumTables(Students):
    """展示程序空间中已经读入的课表

    Args:
        Students (list[Student]): 输入学生列表
    """
    for student_i in Students:
        print(student_i.getNumTable())


def importTable():
    """导入课表
    """
    file = 'initVenv.ps1'
    file = os.path.realpath(file)
    print(file)
    os.system(f'explorer /select, {file}')
    # table = pd.read_excel(filepath, header=0, index_col=0)
    # return table


def clearOutFile():
    """清空输出文件
    """
    for i in os.listdir(os.getcwd() + "\\strTable"):
        if (i.endswith(".xlsx")):
            print("del:strTable\\ " + i)
            os.remove(os.getcwd() + "\\strTable\\" + i)
    for i in os.listdir(os.getcwd() + "\\numTable"):
        if (i.endswith(".xlsx")):
            print("del:numTable\\" + i)
            os.remove(os.getcwd() + "\\numTable\\" + i)
    return


class Student(object):
    """学生类, 存储名字、值班时间、数值化的课表、原始字符课表
    """
    name = str
    dutyTime = list
    numTable = pd.DataFrame
    strTable = pd.DataFrame
    tableRow = 0
    tableColumn = 0

    def __init__(self, name=None, numTable=None, strTable=None):
        self.name = name
        self.dutyTime = []  # 存放学生的值班时间，每个元素为一个二元列表例如用[0,4]表示['周一', '9-10节']，用append()方法添加,用len()方法获取长度
        self.numTable = numTable
        self.strTable = strTable
        # self.tableRow, self.tableColumn = self.numTable.shape

    def getName(self):
        return self.name

    def getDutyTime(self):
        return self.dutyTime

    def getNumTable(self):
        return self.numTable

    def getStrTable(self):
        return self.strTable

    def setDutyTime(self, row_num, column_num):
        """设置值班时间

        Args:
            row_tag (str): 行标签
            column_tag (str): 列标签
        """
        self.dutyTime.append([row_num, column_num])


def initFiles(base=os.getcwd()):
    """初始化文件
    """
    # 初始化数据
    clearOutFile()
    inputpath = base + '\\input'
    for f in os.listdir(inputpath):
        fullname = os.path.join(inputpath, f)
        to_numTable(fullname)

# '\\numTable'


def initStudents(base=os.getcwd()):
    """初始化学生列表
    初始化使用浅拷贝

    Args:
        base (str, optional): 基路径. Defaults to os.getcwd().

    Yields:
        Student: 学生迭代器中的元
    """
    for f in os.listdir(base + "\\input"):
        # os.path.splitext会截断文件名和后缀产生长为2的元组('fileName', '.txt')
        name = os.path.splitext(f)[0]
        numTable = pd.read_excel(base+'\\numTable\\'+f, header=0, index_col=0)
        strTable = pd.read_excel(base+'\\strTable\\'+f, header=0, index_col=0)
        strTable.fillna('', inplace=True)
        yield Student(name, numTable, strTable)

# initStudents()不直接使用，一般通过getStudentsList()获取列表


def getStudentsList():
    """获得学生列表

    Returns:
        list[Student]: 学生列表
    """
    students = []
    for i in initStudents():
        students.append(i)
    return students
# 生成迭代器和返回列表的区别：迭代器不能通过[]访问某个内容也不能直接赋值给列表，传参不便，而列表可以通过[]访问某个内容，其他区别


# -----------dao

def to_freeTable(students, sumkey=False):
    """将学生列表转化为空闲课表

    Args:
        students (list(students)): 学生列表
        sumkey (bool, optional): 标志是否要在freeTable_str的每个单元格添加总计信息. Defaults to False.

    Returns:
        freeTable_str, freeTable_obj: 保存到文件，并且返回一个字符串表和一个对象表 
    """
    freeTable = pd.DataFrame(data='', index=students[0].getNumTable(
    ).index, columns=students[0].getNumTable().columns)
    row, column = students[0].getNumTable().shape

    # 初始化一个freeTable每个单元格存储的是对象类型
    freeTable_obj = freeTable.copy()
    for i in range(row):
        for j in range(column):
            freeTable_obj.iloc[i, j] = list()
    print(freeTable_obj) 

    
    for i in range(row):
        for j in range(column):
            singular_num = 0
            even_num = 0
            # 每个单元格刷新计数
            for student_i in students:

                if(student_i.getNumTable().iloc[i, j] == 0):  # 单双都有空就加入
                    freeTable.iloc[i, j] += student_i.getName() + '\n'
                    singular_num += 1
                    even_num += 1

                    freeTable_obj.iloc[i, j].append(student_i) # 这里对象表没有考虑单双周，留作后面改进

                elif student_i.getNumTable().iloc[i, j] == 2:  # 双数周有课，单数周没课
                    freeTable.iloc[i, j] += student_i.getName() + '(单数周空闲)\n'
                    singular_num += 1

                    freeTable_obj.iloc[i, j].append(student_i)

                elif student_i.getNumTable().iloc[i, j] == 1:  # 单数周有课，双数周没课
                    freeTable.iloc[i, j] += student_i.getName() + '(双数周空闲)\n'
                    even_num += 1

                    freeTable_obj.iloc[i, j].append(student_i)

                elif student_i.getNumTable().iloc[i, j] == 3:
                    pass
                else:
                    freeTable.iloc[i,
                                   j] += '错误课表:  {}'.format(student_i.getName())
                    print('错误课表:  {}'.format(student_i.getName()))
            # 统计信息
            if sumkey:
                freeTable.iloc[i, j] += '-------\n无课：\n单周{}人\n双周{}人\n-------\n'.format(
                    singular_num, even_num)
            else:
                pass
            # if students[0].getNumTable().index[i] == '7-8节' and students[0].getNumTable().columns[j] == '星期五':
            #     print(freeTable.loc['7-8节', '星期五'])

    freeTable.to_excel(".\\freeTable\\freeTable.xlsx")

    print(freeTable)  # 输出显示freeTable
    return freeTable, freeTable_obj


# # times表示一人一周值班次数， 且一人一日最多只会值一班
# 这个函数的功能可以等价为算法题：有一个空闲表，同名只能出现一次，怎么放能保证最大覆盖率？
# def outputDutyTable(students=getStudentsList(), times=2):
#     row, column = students[0].getNumTable().shape
#     DutyTable = pd.DataFrame()
#     # 第一轮，不考虑单双周，只考虑有无课，并且一人不会出现超过
#     # 将i，j倒置，外层遍历列，里层遍历行，最里层遍历表，是为了方便保证每人每天最多值班一次
#     for j in range(column):
#         for i in range(row):
#             for student_i in students:
#                 names = student_i.iloc[i,j].split('\n')
#                 if names[0]

def to_dutyTable(students):
    import random as rd
    # 获得一个freeTable（DataFrame类型，表中元素为student列表类型）的对象
    freeTable_str, freeTable_obj = to_freeTable(students)
    # 用来记录每个单元格的空闲人数，sort_list中每个单元的元素为三元列表，[i, j, num]，i, j用来定位该时间快在表中的行列数，num为空闲人数
    sort_list = []
    for i in range(5):
        for j in range(7):
            # 存入三元列表
            sort_list.append([i, j, len(freeTable_obj.iloc[i, j])])
    # 按照空闲人数排序，从小到大，以便后面先安排空闲人数最少的时间块
    sort_list.sort(key=lambda x: x[2])
    # 空闲人数为0的时间块无法排班，直接栈出
    while sort_list[0][2] == 0:
        sort_list.pop(0)
    print(sort_list)

    res = []
    # 从sort_list中顺次pop出来进行处理，保证先安排空闲人数少的时间块，在安排空闲人数多的时间块
    while len(sort_list) > 0:
        # 如果num为0就pop出来，也是该循环的退出条件，保证不会死循环
        if sort_list[0][2] == 0:
            sort_list.pop(0)
            continue
        # 在i, j位置随机选择一个同学值班
        i, j, num = sort_list[0]
        # 随机选择一个同学放在该位置值班
        selected_student = Student()
        selected_student = freeTable_obj.iloc[i, j][rd.choice(range(num))]

        # 一个同学不能一天值班多次，一周最多值班2次
        if len(selected_student.getDutyTime()) < 2:
            if len(selected_student.getDutyTime()) == 0:
                selected_student.setDutyTime(i, j)
                print(selected_student.getName())
                print(selected_student.getDutyTime())
                res.append([i, j, selected_student])
                
                # 从freeTable中删除该同学
                freeTable_obj.iloc[i, j].remove(selected_student)
                freeTable_obj
                sort_list.pop(0)
                continue
            if abs(selected_student.getDutyTime()[0][1] - j) > 1:
                # 如果同学上一次值班不是在同一天，则可以值班
                selected_student.setDutyTime(i, j)
                print(selected_student.getName())
                print(selected_student.getDutyTime())
                res.append([i, j, selected_student])

                # 从freeTable中删除该同学
                freeTable_obj.iloc[i, j].remove(selected_student)
                sort_list.pop(0)
            else:
                # 从对象表中移除该同学
                freeTable_obj.iloc[i, j].remove(selected_student)
                # 更新该区可选人数
                sort_list[0][2] = len(freeTable_obj.iloc[i, j])
                continue
        else:
            # 从对象表中移除该同学
            freeTable_obj.iloc[i, j].remove(selected_student)
            # 更新该区可选人数
            sort_list[0][2] = len(freeTable_obj.iloc[i, j])
            continue
    return res, students


       


    


def to_numTable(inputSheet):
    """将excel表转化为数字化的矩阵表, 同时存储到文件中

    Args:
        inputSheet (DataFrame): 原始excel表
    """
    sheet = pd.read_excel(inputSheet, index_col=None,
                          header=3)  # 读取数据,不使用原表中的数据为表头,不使用原数据作为index
    sheet.dropna(axis=0, how='all', inplace=True)  # 删除全空的行
    # 重新索引,并且删除旧的index，不然会把旧的index加入数据中
    sheet.reset_index(drop=True, inplace=True)
    # 截去多余行
    key = 0
    end = 0
    for i in range(sheet.shape[0]):
        period = sheet.iloc[i, 0]
        if(period == '9-10节'):
            key = 1  # 开始判断是否到达课表结束行
        else:
            continue  # 如果没有到达课表结束行，则继续循环,不会进入条件语句，能减少复杂度
        #  开始判断，既不是9-10节，也不是空，那么一定是课表最后一行的后一行
        if(key == 1 and isinstance(period, str) and period != '9-10节'):
            end = i - 1  # 课表结束行
            break
        else:
            end = i
    sheet.drop(range(end + 1, sheet.shape[0]), inplace=True)  # 删除多余行(结束行之后的行)

    # to_strTable(sheet, tag)-----------------------------------
    """
    args: sheet(DataFrame): 做初步处理后的
    tag(num/str): 去除特定行的标识 
    
    """
    # 保存可阅读的字符串课表
    path, f = os.path.split(inputSheet)
    str_sheet = sheet.copy(deep=True)  # 深拷贝

    str_sheet.fillna('', inplace=True)  # 将空值替换为空字符串

    # 合并行，将同一时间段的课程情况合并,python的for迭代器循环无法实现代表变元i的复位,因此使用while循环
    i = 0
    tempstr = str()
    while i + 1 < str_sheet.shape[0]:
        nextPeriod = str_sheet.iloc[i + 1, 0]
        if nextPeriod == '':
            for j in range(1, str_sheet.shape[1]):
                tempstr = str_sheet.iloc[i, j] + '\n' + str_sheet.iloc[i + 1, j]
                str_sheet.iloc[i, j] = tempstr

            str_sheet.drop(str_sheet.index[i + 1], inplace=True)
            i = i - 1  # 复位，因为删除了一行，所以i要减1
        i = i + 1

    # 重新索引,并t且删除旧的index，不然会把旧的index加入数据中
    str_sheet.set_index(str_sheet.columns[0], drop=True, inplace=True)
    str_sheet.to_excel(".\\strTable\\" + f)  # 将简化的课表保存为excel
  # -----------------------

    sheet.fillna(0, inplace=True)  # 将空值替换为0

   # 将课表中的数据转换为数字，并将同一时间段合并
    for i in range(sheet.shape[0]):
        # 上课时间段没必要遍历, 故从下标1开始
        for j in range(1, sheet.shape[1]):
            temp = sheet.iloc[i, j]
            if(isinstance(temp, str)):
                line = temp
                pattern = '(双)'
                if(pattern in line):
                    sheet.iloc[i, j] = 2
                    continue

                pattern = "(单)"
                if(pattern in line):
                    sheet.iloc[i, j] = 1
                    continue

                sheet.iloc[i, j] = 3

    # 合并行，将同一时间段的课程情况合并,python的for迭代器循环无法实现代表变元i的复位,因此使用while循环
    i = 0
    temp = 0  # 初始化临时变量,用来暂存相加结果
    while i + 1 < sheet.shape[0]:
        nextPeriod = sheet.iloc[i + 1, 0]
        if nextPeriod == 0:
            for j in range(1, sheet.shape[1]):
                temp = sheet.iloc[i, j] + sheet.iloc[i + 1, j]
                # 保证每次相加最多为3
                if(temp > 3):
                    temp = 3
                sheet.iloc[i, j] = temp
            sheet.drop(sheet.index[i + 1], inplace=True)
            i = i - 1  # 复位，因为删除了一行，所以i要减1
        i = i + 1
    # 重新索引,并且删除旧的index，不然会把旧的index加入数据中
    sheet.set_index(sheet.columns[0], drop=True, inplace=True)

    # 保存数字表
    sheet.to_excel(".\\numTable\\" + f)  # 将数字化的课表保存为excel


# # 直接运行有报错
#   warn("Workbook contains no default style, apply openpyxl's default")
# Traceback (most recent call last):
#   File "f:\dataFileForAll\Pros\pyvenvPros\venvForJupyter\main.py", line 169, in <module>
#     to_freeTable()
#   File "f:\dataFileForAll\Pros\pyvenvPros\venvForJupyter\main.py", line 50, in to_freeTable
#     freeTable = pd.DataFrame(data='', index=students[0].getNumTable().index, columns=students[0].getNumTable().columns)
# IndexError: list index out of range
# 但是分两次运行先提取numTable再提取freeTable，可以解决这个问题，或者直接运行两次，猜测是文件写入尚未完成就开始输出freeTable导致的, 改进：在两操作中加时延或者等待一个标志再输出
# 可能文件读入尚未完成导致读取第一个文件的内容时报错尚未刷新需要重开进程 ？？？？？
# 实际上是默认参数在赋值时不得不运行，导致代码在函数声明部分就运行，因此读取不到
if __name__ == "__main__":
    base = os.getcwd() + '\\input'
    for f in os.listdir(base):
        fullname = os.path.join(base, f)
        to_numTable(fullname)
    to_freeTable(getStudentsList())
    print(getStudentsList()[0].getStrTable())
    print(getStudentsList()[0].getNumTable())
