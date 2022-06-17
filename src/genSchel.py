from main import *
students = []
students = getStudentsList()
print(students[0].getNumTable())

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

