# 使用方法：目前暂时没有实现文件存储和修改后缀操作，得在代码中修改要操作的后缀
import os

def matchFile(endswith, base=os.getcwd()):
    for f in os.listdir(base):
        for end in endswith:
            if f.endswith(end):
                fullname = os.path.join(base,f)
                yield fullname

def displayFiles(opkind, endswith, base=os.getcwd()):
    print('\n将'+opkind+'：')
    print('-----------------------------')
    for f in matchFile(endswith, base):
        print(f.replace(base,'')) # 去掉base,只显示相对路径
    print('-----------------------------')
    print('当前脚本操作目录为：'+base+'\n')

def displayEnds(opkind, endswith):
    print('\n将'+opkind+'：')
    print('-----------------------------')
    for end in endswith:
        print(end)
    print('-----------------------------')
    
def moveTo(endswith, base=os.getcwd(), newpath='F:\\mycache'):
    key = 0
    for f in matchFile(endswith, base):
        print('move '+ f.replace(base, ''))
        os.system("powershell ; move-item " + '\'' + f + '\'' + ' ' + '\'' + newpath + '\'') # 用'包住路径，能避免路径中有空格导致的错误
        key = 1
    if key == 0:
        print('没有文件被操作')
        
#  改进，通过文本文件来指定需要放入缓存的文件
if __name__ == "__main__":
    opkind = '移动'
    endswith = ['.xlsx', '.xls' ]
    print('注意：本脚本只会在将当前目录下同级的文件中查找，不会深入到子目录中')
    base = input("请输入要操作的根目录,不输入则默认为当前执行目录(例：C:\\readme)：")
    displayEnds(opkind, endswith)
    yOrn = input("请确认要移动的文件后缀，选否则立刻结束脚本(y/n)：")
    if yOrn == '':
        print('未' + opkind + '任何文件')
    elif yOrn != 'y':
        print('未' + opkind + '任何文件')
    else:
    # yOrn非空且为y
        if base != '':
            # 使用输入的base
            displayFiles(opkind, endswith, base)
            key = input("确定" + opkind + "(y/n):")
            if key == 'y':
                newpath = input("输入目标路径，不输入则移动到默认路径mycache(F:\mycache)：")
                if newpath == '':
                    moveTo(endswith, base)
                else:
                    moveTo(endswith, base, newpath)
            else:
                print('未' + opkind + '任何文件')
        else:
            # base 为空时，默认为执行目录
            displayFiles(opkind, endswith)
            key = input("确定" + opkind + "(y/n):")
            if key == 'y':
                newpath = input("输入目标路径，不输入则默认移动到默认路径mycache(F:\mycache)：")
                if newpath == '':
                    moveTo(endswith)
                else:
                    moveTo(endswith, newpath=newpath) # 需要指明给哪个参数，不然会导致按照顺序传参
            else:
                print('未'+ opkind + '任何文件')
  