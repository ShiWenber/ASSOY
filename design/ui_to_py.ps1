# 对文件夹下的所有.ui文件执行 pyuic5 -o filename.py filename.ui
Get-ChildItem -Name "*.ui" | foreach-object{$_ -replace ".ui", ""}  | foreach-object{Invoke-Expression "pyuic5 -o $_.py $_.ui"}
# Get-ChildItem -Name "*.ui" | foreach-object{$_ -replace ".ui", ""}  | foreach-object{pyuic5 -o $_.py $_.ui} 无效