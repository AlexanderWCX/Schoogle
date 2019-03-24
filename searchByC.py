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

## Ignore below. They are just for code testing.
#ccaList = ['Taekwondo']
#subjectList = []
#typeList = []
#genderList = []
#focusList = []


def searchByC(ccaList, subjectList, typeList, genderList, focusList):

    ccaResultsList = []
    subjectResultsList = []
    typeResultsList = []
    genderResultsList = []
    focusResultsList = []
    finalResultsList = []

    filledList = []
    allList = [ccaResultsList, subjectResultsList, typeResultsList, genderResultsList, focusResultsList]
    
    for n in range(0,len(typeList)):
        if typeList[n] == "Government-Aided School":
            typeList[n] = "Government-Aided Sch"
    
    
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

#Gender matching
    for n in range(0,len(genderList)):
        for i in range(1, 100):
            schoolType = wsSchoolInfo.cell(i,24).value
            schoolName = wsSchoolInfo.cell(i,30).value
            if genderList[n].lower() == schoolType.lower():
                genderResultsList.append(schoolName)

#Focus area matching
    for n in range(0,len(focusList)):
        for i in range(1, 99):
            focusArea = wsFocus.cell(i,3).value
            schoolName = wsFocus.cell(i,4).value
            if focusList[n].lower() == focusArea.lower():
                focusResultsList.append(schoolName)            

#Get common schools from all lists
    for n in range (0,len(allList)):
        testList = allList[n]
        length = len(testList)
        if length != 0:
            filledList.append(testList)

    for m in range (0,len(filledList)):
        currentList = filledList[m]
        if m == 0: 
            for k in range (0,len(currentList)):
                finalResultsList.append(currentList[k])

        if m != 0:
            for x in range (0,len(finalResultsList)):
                for y in range (0,len(currentList)):
                    if finalResultsList[x] == currentList[y]:
                        break
                    else:
                        if y == len(currentList):
                            del finalResultsList[x]
                
        
    finalResultsList = list(dict.fromkeys(finalResultsList))
    #print(finalResultsList)
    return finalResultsList


##Ignore below. They are just for code testing.
#searchByC(ccaList,subjectList,typeList,genderList,focusList)

