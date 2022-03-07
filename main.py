import pandas as pd
import os


class Student(object):
    name = str
    dutyTime = list
    numTable = pd.DataFrame
    strTable = pd.DataFrame
    tableRow = 0
    tableColumn = 0
    def __init__(self, name, numTable, strTable = None):
        self.name = name
        self.dutyTime = [] # 存放学生的值班时间，每个元素为一个二元列表['周一', '9-10节']，用append()方法添加,用len()方法获取长度
        self.numTable = numTable
        self.strTable = strTable
        # self.tableRow, self.tableColumn = self.numTable.shape
    def getName(self):
        return self.name
    def getDutytime(self):
        return self.dutyTime
    def getNumTable(self):
        return self.numTable
    def getStrTable(self):
        return self.strTable
    


def initStudents(base=(os.getcwd()+'\\numTable')):
    for f in os.listdir(base):
        name = os.path.splitext(f)[0] # os.path.splitext会截断文件名和后缀产生长为2的元组('fileName', '.txt')
        numTable = pd.read_excel(base+'\\'+f, header=0, index_col=0)
        # strTable = pd.read_excel(base+'\\'+f, header=1) # strTable先不读，作为后续升级功能
        yield Student(name, numTable)
 
# initStudents()不直接使用，一般通过getStudentsList()获取列表    
def getStudentsList():
    students = []
    for i in initStudents():
        students.append(i)
    return students
# 生成迭代器和返回列表的区别：迭代器不能通过[]访问某个内容也不能直接赋值给列表，传参不便，而列表可以通过[]访问某个内容，其他区别
        
def displayNumTables(Students=getStudentsList()):
    for student_i in Students:
        print(student_i.getNumTable())
        

def to_freeTable(students=getStudentsList()):
    freeTable = pd.DataFrame(data='', index=students[0].getNumTable().index, columns=students[0].getNumTable().columns)  
    row, column = students[0].getNumTable().shape
    for i in range(row):
        for j in range(column):
            for student_i in students:
                if(student_i.getNumTable().iloc[i, j] == 0):
                    freeTable.iloc[i, j] += student_i.getName() + '\n'
    freeTable.to_excel(".\\freeTable\\freeTable.xlsx")
    return freeTable



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


def to_numTable(inputSheet):
    sheet = pd.read_excel(inputSheet, index_col=None, header=3)  # 读取数据,不使用原表中的数据为表头,不使用原数据作为index
    sheet.dropna(axis=0, how='all',inplace=True)  # 删除全空的行
    sheet.reset_index(drop=True, inplace=True)  # 重新索引,并且删除旧的index，不然会把旧的index加入数据中
    # 截去多余行
    key = 0
    end = 0
    for i in range(sheet.shape[0]):
        period = sheet.iloc[i, 0]
        if(period == '9-10节'):
            key = 1 # 开始判断是否到达课表结束行
        else:
            continue # 如果没有到达课表结束行，则继续循环,不会进入条件语句，能减少复杂度
        #  开始判断，既不是9-10节，也不是空，那么一定是课表最后一行的后一行
        if(key == 1 and isinstance(period, str) and period != '9-10节'):
            end = i - 1 # 课表结束行
            break
        else:
            end = i
    sheet.drop(range(end + 1, sheet.shape[0]), inplace=True)  # 删除多余行(结束行之后的行)
    sheet.fillna(0,inplace=True)  # 将空值替换为0
    
    # 保存可阅读的字符串课表，但是同一时间段不合并
    path,f = os.path.split(inputSheet)
    sheet.to_excel(".\\strTable\\" + f) # 将简化的课表保存为excel
    
    
    # 将课表中的数据转换为数字，并将同一时间段合并
    for i in range(sheet.shape[0]):
        # 上课时间段没必要遍历, 故从下标1开始
        for j in range(1, sheet.shape[1]):
            temp = sheet.iloc[i, j]
            if(isinstance(temp, str)):
                line = temp
                pattern = '(双)'
                if(pattern in line):
                    sheet.iloc[i,j] = 2
                    continue
                
                pattern="(单)"
                if(pattern in line):
                    sheet.iloc[i,j] = 1
                    continue
                
                sheet.iloc[i,j] = 3

    # 合并行，将同一时间段的课程情况合并,python的for迭代器循环无法实现代表变元i的复位,因此使用while循环
    i = 0
    temp = 0 # 初始化临时变量,用来暂存相加结果
    while i + 1 < sheet.shape[0] :
        nextPeriod = sheet.iloc[i + 1, 0]
        if nextPeriod == 0 :
            for j in range(1, sheet.shape[1]):
                temp = sheet.iloc[i,j] + sheet.iloc[i + 1,j]
                # 保证每次相加最多为3
                if(temp > 3):
                    temp = 3
                sheet.iloc[i,j] = temp
            sheet.drop(sheet.index[i + 1], inplace=True)
            i = i - 1 # 复位，因为删除了一行，所以i要减1
        i = i + 1
    sheet.set_index(sheet.columns[0], drop=True, inplace=True)  # 重新索引,并且删除旧的index，不然会把旧的index加入数据中
    
    # 保存数字表
    sheet.to_excel(".\\numTable\\" + f) # 将数字化的课表保存为excel
    
if __name__ == "__main__":
    base = os.getcwd() + '\\input'
    for f in os.listdir(base):
        fullname = os.path.join(base, f)
        to_numTable(fullname)
    to_freeTable()