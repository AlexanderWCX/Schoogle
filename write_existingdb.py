#write to existing file
import xlrd
from xlutils.copy import copy

#make a copy of the workbook and write to it
#not possible to modify the workbook itself
wb = xlrd.open_workbook('userInfo.xls')
new_wb = copy(wb)
ws = new_wb.get_sheet(0)

ws.write(0, 3, 'pc')

new_wb.save('userInfo.xls')