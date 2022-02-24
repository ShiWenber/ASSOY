
        
# csv文件转为excel文件
def csv_to_xlsx(self,path,file_name):   # 图形界面中不可使用input输入，会导致死循环
    csv_1 = pd.read_csv(path, encoding='utf-8')
    sheet_name = "Sheet1"
    csv_1.to_excel(f'{file_name}.xlsx', sheet_name=f'{sheet_name}')
    self.label_3.setText("成功")

    
# excel文件转换为csv文件
def xlsx_to_csv(self,path,name):
    workbook = xlrd.open_workbook(path)
    table = workbook.sheet_by_index(0)
    with codecs.open(f'{name}.csv', 'w', encoding='utf-8') as f:
        write = csv.writer(f)
        for row_num in range(table.nrows):
            row_value = table.row_values(row_num)
            write.writerow(row_value)

if __name__ == "__mian__":
    csv_to_xlsx()