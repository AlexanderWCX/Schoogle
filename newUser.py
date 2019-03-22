# import relevant stuff 
import xlrd
from xlutils.copy import copy
from verifyEmailAndPassword import findEmailInDB 

def writeNewUserToDB(email, password, postalCode):
	# if email already exists in the database, not a new user 
	# cannot create a new record for that user 
	# return false  
	if (findEmailInDB(email) > 0):
		return False 
		
	# open the userInformation workbook
	wb = xlrd.open_workbook('userInformation.xls')
	
	# make a copy of the userInformation workbook
	newWB = copy(wb)

	# use the copy to open the worksheet
	newWS = newWB.get_sheet(0)

	# calculate the index of the row to write to 
	row = 2 + (numOfRecords*4)

	# write the email
	newWS.write(row, 0, email)

	# write the password 
	newWS.write(row, 1, password)

	# if the postal code is an empty string
	if postalCode == '':
		# write postal code as 'null'
		newWS.write(row, 2, 'null')
	# else, write the actual postal code
	else:
		newWS.write(row, 2, postalCode)

	# increment the number of records and write it to the database
	newWS.write(0, 1, numOfRecords + 1) 
	
	# save the workbook
	newWB.save('userInformation.xls')
	
	return True
	



