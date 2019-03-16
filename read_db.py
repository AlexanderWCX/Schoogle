#read
import xlrd

wb = xlrd.open_workbook('generalSchoolInfo.xls')
ws = wb.sheet_by_name('generalSchoolInfo')

schoolToFind = "ST. GABRIEL'S SECONDARY SCHOOL"
#find school name

#school names are in column 30
for i in range(1, 100):
    schoolName = ws.cell(i, 30).value
    if schoolName == schoolToFind:
        break

#get the postal code
postalCode = ws.cell(i, 6).value
print(postalCode)