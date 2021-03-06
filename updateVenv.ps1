# 先退出虚拟环境
deactivate

# 如果存在.\Scripts表示虚拟环境已经存在，如果不存在则创建虚拟环境
if(-not (test-path .\Scripts))
{
    # 将当前目录创建为 python 虚拟环境
    python -m venv .
}
# 激活虚拟环境
.\Scripts\activate
# 创建存储 xlsx 表所需的文件夹
new-item .\input -ItemType "directory"
new-item .\numTable -ItemType "directory"
new-item .\strTable -ItemType "directory"
new-item .\freeTable -ItemType "directory"
# 更新当前虚拟环境的pip工具
python -m pip install --upgrade pip
# 按照requirements.txt文件中的依赖安装依赖包
pip install -r requirements.txt
