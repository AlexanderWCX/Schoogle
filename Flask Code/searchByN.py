#read
import xlrd

wb = xlrd.open_workbook('generalSchoolInfo.xls')
ws = wb.sheet_by_name('generalSchoolInfo')

def searchByN(keyword):

    resultsList = []
    
#find school name

#school names are in column 30
    for i in range(1, 100):
        schoolName = ws.cell(i, 30).value
        
        #if school name found, add to resultslist
        if keyword.lower() in schoolName.lower():
            print(schoolName)
            resultsList.append(schoolName)
            

    
    return resultsList


#searchByN("st.")
