import xlrd
import os,sys
# data = xlrd.open_workbook('E:\python接口\AutoInterface\web\demofile\interface.xlsx')

class OperationExcel:
    def __init__(self,file_neme=None,sheet_id=None):
        if file_neme:
            self.file_neme = file_neme
            self.sheet_id = sheet_id
        else:
            # self.file_neme = 'interface.xlsx'
            self.file_neme = 'E:\python接口\AutoInterface\web\demofile\interface.xlsx'
            self.sheet_id = 0
        self.data = self.get_data()

    # 获取sheet内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_neme)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取sheet行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取某个单元格的内容
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)

if __name__ == '__main__':
    opers = OperationExcel()
    # print(opers.get_data().nrows)

    print(os.path.abspath('AutoInterface/interface.xlsx'))
    print(os.path.abspath('.'))
    print(os.path.abspath('..接下来看7.4'))

