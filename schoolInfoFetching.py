#read
import xlrd
from sortingAndRelatedFunctions import findSchoolPostalCode, getLatLong

wbCCA = xlrd.open_workbook('ccaOffered.xls')
wsCCA = wbCCA.sheet_by_name('ccaOffered')
wbSubject = xlrd.open_workbook('subjectsOffered.xls')
wsSubject = wbSubject.sheet_by_name('subjectsOffered')
wbSchoolInfo = xlrd.open_workbook('generalSchoolInfo.xls')
wsSchoolInfo = wbSchoolInfo.sheet_by_name('generalSchoolInfo')
wbFocus = xlrd.open_workbook('schoolDistinctiveProgs.xls')
wsFocus = wbFocus.sheet_by_name('schoolDistinctiveProgs')

#return the url for a map
def getMap(name):

    #Get the schools postal code
    postal = findSchoolPostalCode(name)

    #Get the latitude and Longitude of the school
    coordinates = getLatLong(postal)

    #Get the latitude of the school
    latitude = coordinates[0]

    #Get the longitude of the school
    longitude = coordinates[1]

    url='https://tools.onemap.sg/minimap/minimap.html?mWidth=440&mHeight=445&latLng='+latitude+','+longitude+'&zoomLevl=17&iwt=<b>'+name+'</b>&popupWidth=200&popupHeight=500&includePopup=true&onloadPopup=true&design=original'



    return url

#<iframe src="{{ url }}" height=450px width=450px scrolling='no' frameborder='0' allowfullscreen='allowfullscreen'></iframe>


#get school website
def website(school):
    for i in range(1, 100):
        website = wsSchoolInfo.cell(i,38).value
        schoolName = wsSchoolInfo.cell(i,30).value

        #if school name match, return its website
        if schoolName.lower() == school.lower():
            return website
        
#get general information of school
def generalInformation(school):
    
    #instantiate empty return list
    returnlist = []
    for i in range(1, 100):
        schoolName = wsSchoolInfo.cell(i,30).value

        #if school name match
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
        
#get list of subjects offered
def subjectsOffered(school):
    
    #instantiate empty subject list
    subjectList = []
    for i in range(1, 3665):
        schoolName = wsSubject.cell(i,3).value

        #if school name match append subject to subject list
        if schoolName.lower() == school.lower():
            subjectName = wsSubject.cell(i,2).value
            subjectList.append(subjectName)
    
    return subjectList

#get list of sports cca
def physicalCCAs(school):
    
    #instantiate empty cca list
    ccaList = []
    for i in range(1, 1456):
        schoolName = wsCCA.cell(i,2).value
        
        #if school name match a
        if schoolName.lower() == school.lower():
            ccaName = wsCCA.cell(i,6).value
            grouping = wsCCA.cell(i,4).value
            desired = "PHYSICAL SPORTS"

            #if cca grouping matches, append to cca list
            if grouping.lower() == desired.lower():
                ccaList.append(ccaName)

    return ccaList

#get list of arts cca
def artsCCAs(school):
    
    #instantiate empty cca list
    ccaList = []
    for i in range(1, 1456):
        schoolName = wsCCA.cell(i,2).value
        
        #if school name match
        if schoolName.lower() == school.lower():
            ccaName = wsCCA.cell(i,6).value
            grouping = wsCCA.cell(i,4).value
            desired = "VISUAL AND PERFORMING ARTS"
            
            #if cca grouping matches, append to cca list
            if grouping.lower() == desired.lower():
                ccaList.append(ccaName)

    return ccaList

#get list of club and society ccas
def clubCCAs(school):

    #instantiate empty cca list
    ccaList = []
    for i in range(1, 1456):
        schoolName = wsCCA.cell(i,2).value
        
        #if school name match
        if schoolName.lower() == school.lower():
            ccaName = wsCCA.cell(i,6).value
            grouping = wsCCA.cell(i,4).value
            desired = "CLUBS AND SOCIETIES"
            
            #if cca grouping matches, append to cca list
            if grouping.lower() == desired.lower():
                ccaList.append(ccaName)

    return ccaList

#get list of uniformed group ccas
def uniformCCAs(school):
    
    #instantiate empty cca list
    ccaList = []
    for i in range(1, 1456):
        schoolName = wsCCA.cell(i,2).value
        
        #if school name match
        if schoolName.lower() == school.lower():
            ccaName = wsCCA.cell(i,6).value
            grouping = wsCCA.cell(i,4).value
            desired = "UNIFORMED GROUPS"
            
            #if cca grouping matches, append to cca list
            if grouping.lower() == desired.lower():
                ccaList.append(ccaName)

    return ccaList

#get list contact info 
def contactInfo(school):
    
    #instantiate empty contact list
    contactList = []
    for i in range(1, 100):
        schoolName = wsSchoolInfo.cell(i,30).value

        #if school name match
        if schoolName.lower() == school.lower():
            
            #get desired contact info
            email = wsSchoolInfo.cell(i,11).value
            telephone = wsSchoolInfo.cell(i,19).value
            fax = wsSchoolInfo.cell(i,1).value

            #append desired info to contact list
            contactList.append(email)
            contactList.append(telephone)
            contactList.append(fax)

            return contactList
        
#get list of getting there info
def gettingThere(school):
    
    #instantiate empty getting there list
    gettingThere = []
    
    for i in range(1, 100):
        schoolName = wsSchoolInfo.cell(i,30).value
        
        #if school name match
        if schoolName.lower() == school.lower():
            
            #get desired getting there info
            address = wsSchoolInfo.cell(i,32).value
            postalcode = wsSchoolInfo.cell(i,6).value
            nearestMRT = wsSchoolInfo.cell(i,16).value
            buses = wsSchoolInfo.cell(i,17).value

            #append desired info to getting there list
            gettingThere.append(address)
            gettingThere.append(postalcode)
            gettingThere.append(nearestMRT)
            gettingThere.append(buses)

            return gettingThere
        







    
