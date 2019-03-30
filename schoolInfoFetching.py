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

#school = "zhonghua secondary school"

def website(school):
    for i in range(1, 100):
        website = wsSchoolInfo.cell(i,38).value
        schoolName = wsSchoolInfo.cell(i,30).value
        if schoolName.lower() == school.lower():
            return website
        

def generalInformation(school):
    returnlist = []
    for i in range(1, 100):
        schoolName = wsSchoolInfo.cell(i,30).value
        if schoolName.lower() == school.lower():
            # Get desired information
            schooltype = wsSchoolInfo.cell(i,7).value
            gender = wsSchoolInfo.cell(i,24).value
            principal = wsSchoolInfo.cell(i,22).value
            vision = wsSchoolInfo.cell(i,25).value
            mission = wsSchoolInfo.cell(i,27).value
            philosophy = wsSchoolInfo.cell(i,15).value

            # Append info to returnlist
            returnlist.append(schooltype)
            returnlist.append(gender)
            returnlist.append(principal)
            returnlist.append(vision)
            returnlist.append(mission)
            returnlist.append(philosophy)
            return returnlist
        

def subjectsOffered(school):
    subjectList = []
    for i in range(1, 3665):
        schoolName = wsSubject.cell(i,3).value
        if schoolName.lower() == school.lower():
            subjectName = wsSubject.cell(i,2).value
            subjectList.append(subjectName)
    
    return subjectList

def physicalCCAs(school):
    ccaList = []
    for i in range(1, 1456):
        schoolName = wsCCA.cell(i,2).value
        if schoolName.lower() == school.lower():
            ccaName = wsCCA.cell(i,6).value
            grouping = wsCCA.cell(i,4).value
            desired = "PHYSICAL SPORTS"
            if grouping.lower() == desired.lower():
                ccaList.append(ccaName)

    return ccaList

def artsCCAs(school):
    ccaList = []
    for i in range(1, 1456):
        schoolName = wsCCA.cell(i,2).value
        if schoolName.lower() == school.lower():
            ccaName = wsCCA.cell(i,6).value
            grouping = wsCCA.cell(i,4).value
            desired = "VISUAL AND PERFORMING ARTS"
            if grouping.lower() == desired.lower():
                ccaList.append(ccaName)

    return ccaList

def clubCCAs(school):
    ccaList = []
    for i in range(1, 1456):
        schoolName = wsCCA.cell(i,2).value
        if schoolName.lower() == school.lower():
            ccaName = wsCCA.cell(i,6).value
            grouping = wsCCA.cell(i,4).value
            desired = "CLUBS AND SOCIETIES"
            if grouping.lower() == desired.lower():
                ccaList.append(ccaName)

    return ccaList


def uniformCCAs(school):
    ccaList = []
    for i in range(1, 1456):
        schoolName = wsCCA.cell(i,2).value
        if schoolName.lower() == school.lower():
            ccaName = wsCCA.cell(i,6).value
            grouping = wsCCA.cell(i,4).value
            desired = "UNIFORMED GROUPS"
            if grouping.lower() == desired.lower():
                ccaList.append(ccaName)

    return ccaList

def contactInfo(school):
    contactList = []
    for i in range(1, 100):
        schoolName = wsSchoolInfo.cell(i,30).value
    
        if schoolName.lower() == school.lower():

            email = wsSchoolInfo.cell(i,11).value
            telephone = wsSchoolInfo.cell(i,19).value
            fax = wsSchoolInfo.cell(i,1).value

            contactList.append(email)
            contactList.append(telephone)
            contactList.append(fax)

            return contactList
        

def gettingThere(school):
    gettingThere = []
    
    for i in range(1, 100):
        schoolName = wsSchoolInfo.cell(i,30).value
    
        if schoolName.lower() == school.lower():

            address = wsSchoolInfo.cell(i,32).value
            postalcode = wsSchoolInfo.cell(i,6).value
            nearestMRT = wsSchoolInfo.cell(i,16).value
            buses = wsSchoolInfo.cell(i,17).value

            gettingThere.append(address)
            gettingThere.append(postalcode)
            gettingThere.append(nearestMRT)
            gettingThere.append(buses)

            return gettingThere
        

#print(website(school))
#print('==========================')
#print(generalInformation(school))
#print('==========================')
#print(subjectsOffered(school))
#print('==========================')
#print(physicalCCAs(school))
#print('==========================')
#print(artsCCAs(school))
#print('==========================')
#print(clubCCAs(school))
#print('==========================')
#print(uniformCCAs(school))
#print('==========================')
#print(contactInfo(school))
#print('==========================')
#print(gettingThere(school))





    
