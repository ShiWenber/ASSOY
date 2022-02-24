# 此项目py调用c的函数统一命名为CF----，和调用的dll中对应的函数同输入同输出
# 
from ctypes import *


print("hello world")
ll = cdll.LoadLibrary
lib = ll("./C/test.dll")
    
def test01():
    lib.hello()
    
def test02():
    c=lib.add(1,2)
    print(c)

def test03():
    a = (c_int) (2)
    a_p = POINTER(c_int)(a) # 指向 a
    lib.inc(a_p)
    print(a_p[0]) # a_p[0] == *(a_p+0)是c中的指针用法
    print(a.value)
    print(a)

def test04():
    arr = [1,2,3,4]
    a = (c_int*4)(*arr)# 长4的arr指针
    a_p = POINTER(c_int)(a)  # 就存的是arr首地址
    lib.printArr(a_p,4)
    lib.getArr.restype = POINTER(c_int)
    resuilt = lib.getArr(a_p, 4)
    print()
    for i in range(0,5):
        print(i)
        print(resuilt[i])
    

if __name__ == '__main__':
    test01()
    test02()
    test03()
    test04()
    # test05()