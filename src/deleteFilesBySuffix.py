# 功能：删除全部带有某格式的文件
import os
  
def matchFile(base, endswith):
    for root, ds, fs in os.walk(base):
        for f in fs:
            if f.endswith(endswith):
                fullname = os.path.join(root,f)
                yield fullname
            
def deleteFiles(endswith, base=os.getcwd()):
    key = 0
    for f in matchFile(base, endswith):
        print('remove '+f.replace(base,''))
        os.remove(f)
        key = 1
    if key == 0:
        print('未删除任何文件')

def displayFiles(endswith, base=os.getcwd()):
    print('\n将删除：')
    print('-----------------------------')
    for f in matchFile(base, endswith):
        print(f.replace(base,'')) #  去掉base,只显示相对路径
    print('-----------------------------')
    print('当前脚本操作目录为：'+base+'\n')
    


if __name__ == "__main__":
    print('注意：本脚本也会将所有子目录下符合后缀的文件全部删除')
    base = input("请输入要操作的根目录,不输入则默认为当前执行目录(例：C:\\readme)：")
    endswith = input("请输入要删除的文件后缀，不输入则立刻结束脚本(例：.exe)：")
    if endswith == '':
        print('未删除任何文件')
    elif base != '':
        displayFiles(endswith, base)
        key = input("确定删除(y/n):")
        if key == 'y':
            deleteFiles(endswith, base)
        else:
            print('未删除任何文件')
    else:
        # base 为空时，默认为执行目录
        displayFiles(endswith)
        key = input("确定删除(y/n):")
        if key == 'y':
            deleteFiles(endswith)
        else:
            print('未删除任何文件')
  