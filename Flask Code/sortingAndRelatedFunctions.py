# import relevant libraries
import requests
import json
import xlrd
from verifyEmailAndPassword import findEmailInDB 

# sort the schools by distance from the user's house
def sortByDistance(schoolList, userPostalCode):

    #create distanceList
    distanceList = []

    # for each school, get its distance from the user's home
    for i in range(len(schoolList)):

        # get the school's postal code
        schoolPostalCode = findSchoolPostalCode(schoolList[i])

        # get the distance between the user's home and the school
        distance = getDistance(userPostalCode, schoolPostalCode)

        #append the distance to distanceList
        distanceList.append(distance)

    #make a copy of distanceList as sortedDistancesList
    sortedDistancesList = distanceList.copy()

    #sort the distances
    sortedDistancesList.sort()

    #create sortedSchoolsList to hold the list of sorted schools
    sortedSchoolsList = []

    #for each distance in sortedDistancesList, get the index of that same distance in distanceList
    #the index corresponds to the school with that distance in schoolList
    for i in range(len(sortedDistancesList)):

        # get the distance at i
        dist = sortedDistancesList[i]

        # get the index of that same distance in distanceList
        index = distanceList.index(dist)

        # index out the school name from schoolList
        schName = schoolList[index]

        # append schName to sortedSchoolsList
        sortedSchoolsList.append(schName)

    # create a list named sortedSchoolsDistance of sortedSchoolsList and sortedDistancesList
    sortedSchoolsDistance = [sortedSchoolsList, sortedDistancesList]

    # return sortedSchoolsDistance
    return sortedSchoolsDistance

def retrieveSavedSchools(email):
    # open the userInformation workbook 
    wb = xlrd.open_workbook('userInformation.xls')

	# open the userInformation worksheet
    ws = wb.sheet_by_name('userInformation')

    # create schoolList
    schoolList = []

    # gives row index the email is stored in in the userInformation database 
    row = findEmailInDB(email) 
	
	# if email does not exist in database 
    if row == -1:
		# no record, no sorting 
        return False 

	# retrieve number of schools stored in that record
    numOfSchools = int(ws.cell(row + 1, 0).value)

	# for each school in that record
    for i in range(numOfSchools):
		# append that school into schoolList
        schoolList.append(ws.cell(row + 1, i + 1).value)

    return schoolList
    

# sort the schools by the dates on which they are saved
def sortBySavedDate(email):

    # open the userInformation workbook 
    wb = xlrd.open_workbook('userInformation.xls')

	# open the userInformation worksheet
    ws = wb.sheet_by_name('userInformation')

    # create schoolList and savedDatesList
    schoolList = []
    savedDatesList = []

    # gives row index the email is stored in in the userInformation database 
    row = findEmailInDB(email) 
	
	# if email does not exist in database 
    if row == -1:
		# no record, no sorting 
        return False 

	# retrieve number of schools stored in that record
    numOfSchools = int(ws.cell(row + 1, 0).value)

	# for each school in that record
    for i in range(numOfSchools):
		# append that school into schoolList
        schoolList.append(ws.cell(row + 1, i + 1).value)

		# append the corresponding saved date into savedDatesList
        savedDatesList.append(ws.cell(row + 2, i + 1).value)


    # create a list named sortedSchoolsSavedDates of schoolList and savedDatesList
    sortedSchoolsSavedDates = [schoolList, savedDatesList]

    # return sortedSchoolsSavedDates
    return sortedSchoolsSavedDates

def sortByAlphabetical(schoolList):
    return sorted(schoolList)


# function to get the distance between 2 locations
def getDistance(postalCode1, postalCode2):
    latLong = getLatLong(postalCode1)
    # start: starting location
    start = latLong[0] + ',' + latLong[1]
    latLong = getLatLong(postalCode2)
    # end: ending location
    end = latLong[0] + ',' + latLong[1]

    # routeType does not matter because the distance is always the same
    routeType = 'drive'

    # token
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjI0ODAsInVzZXJfaWQiOjI0ODAsImVtYWlsIjoiZGFueWkxOTk4QGdtYWlsLmNvbSIsImZvcmV2ZXIiOmZhbHNlLCJpc3MiOiJodHRwOlwvXC9vbTIuZGZlLm9uZW1hcC5zZ1wvYXBpXC92MlwvdXNlclwvc2Vzc2lvbiIsImlhdCI6MTU1NDk4ODM1NCwiZXhwIjoxNTU1NDIwMzU0LCJuYmYiOjE1NTQ5ODgzNTQsImp0aSI6ImE2MzdiZTE2M2ViMjJjYzBlOGJhNmMwZjcyMDNlMzYxIn0.t2w9TiWGlxZioqh1Cwr6TAnQ4hzk7nRUa0tEi8h_Vmg'
    # formulate the url
    url = 'https://developers.onemap.sg/privateapi/routingsvc/route?start=' + start + '&end=' + end + '&routeType=' + routeType + \
          '&token=' + token

    # perform the query
    res = requests.get(url)
    # res is in json format
    res = res.text

    # change res to dict
    res = json.loads(res)
    # extract out the distance
    distance = res['route_summary']['total_distance']

    return distance


# find the latitude and longitude of postalCode
def getLatLong(postalCode):
    # formulate the url to query
    url = 'https://developers.onemap.sg/commonapi/search?searchVal=' + str(postalCode) + '&returnGeom=Y&getAddrDetails=Y&pageNum=1'

    # perform the query
    res = requests.get(url)
    # res is in json format
    res = res.text

    # change res to dict
    res = json.loads(res)
    # extract out the latitude and longitude
    latitude = res['results'][0]['LATITUDE']
    longitude = res['results'][0]['LONGITUDE']

    return [latitude, longitude]


#find the postal code of a school
def findSchoolPostalCode(schoolName):
    #open the workbook
    wb = xlrd.open_workbook('generalSchoolInfo.xls')

    #open the worksheet
    ws = wb.sheet_by_name('generalSchoolInfo')

    #loop to find index of the record of that school
    for i in range(1, 100):
        # school names are in column 30
        sn = ws.cell(i, 30).value
        #compare sn with schoolName
        if sn == schoolName:
            break

    # get the postal code in column 6
    postalCode = ws.cell(i, 6).value

    return postalCode

def retrievePostalCode(email):
    # open the userInformation workbook 
    wb = xlrd.open_workbook('userInformation.xls')

	# open the userInformation worksheet
    ws = wb.sheet_by_name('userInformation')

    # gives row index the email is stored in in the userInformation database 
    row = findEmailInDB(email) 
	
	# if email does not exist in database 
    if row == -1:
		# no record, no sorting 
        return False 

    # retrieve postalcode
    postalCode = (ws.cell(row , 2).value)

    return postalCode

    



