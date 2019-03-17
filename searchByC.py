#read
import xlrd

wbCCA = xlrd.open_workbook('ccaOffered.xls')
wsCCA = wbCCA.sheet_by_name('ccaOffered')
wbSubject = xlrd.open_workbook('subjectsOffered.xls')
wsSubject = wbSubject.sheet_by_name('subjectsOffered')
wbSchoolInfo = xlrd.open_workbook('generalSchoolInfo.xls')
wsSchoolInfo = wbSchoolInfo.sheet_by_name('generalSchoolInfo')
wbFocus = xlrd.open_workbook('schoolDistinctiveProgs.xls')
wsFocus = wbFocus.sheet_by_name('schoolDistinctiveProgs')

ccaList = ['Taekwondo']
subjectList = ['Art', 'Science']
typeList = ['Government School']
focusList = ['Languages & Humanities']


def searchByC(ccaList, subjectList, typeList, focusList):

    ccaResultsList = []
    subjectResultsList = []
    typeResultsList = []
    focusResultsList = []
    finalResultsList = []
    
    
#CCA matching
    for n in range(0,len(ccaList)):
        for i in range(1, 1456):
            ccaName = wsCCA.cell(i,6).value
            schoolName = wsCCA.cell(i,2).value
            if ccaList[n].lower() == ccaName.lower():
                ccaResultsList.append(schoolName)
            
#Subject matching
    for n in range(0,len(subjectList)):
        for i in range(1, 3665):
            subjectName = wsSubject.cell(i,2).value
            schoolName = wsSubject.cell(i,3).value
            if subjectList[n].lower() == subjectName.lower():
                #print(schoolName)
                subjectResultsList.append(schoolName)

#Type matching
    for n in range(0,len(typeList)):
        for i in range(1, 100):
            schoolType = wsSchoolInfo.cell(i,7).value
            schoolName = wsSchoolInfo.cell(i,30).value
            if typeList[n].lower() == schoolType.lower():
                typeResultsList.append(schoolName)

#Focus area matching
    for n in range(0,len(focusList)):
        for i in range(1, 99):
            focusArea = wsFocus.cell(i,3).value
            schoolName = wsFocus.cell(i,4).value
            if focusList[n].lower() == focusArea.lower():
                focusResultsList.append(schoolName)            


    for i in range(0,len(ccaResultsList)):
        for j in range(0,len(subjectResultsList)):
            for k in range(0,len(typeResultsList)):
                for l in range(0,len(focusResultsList)):
                    if ccaResultsList[i] == subjectResultsList[j] == typeResultsList[k] == focusResultsList[l]:
                        finalResultsList.append(ccaResultsList[i])

    
    finalResultsList = list(dict.fromkeys(finalResultsList))
    #print(finalResultsList)
    return finalResultsList



searchByC(ccaList,subjectList,typeList,focusList)

