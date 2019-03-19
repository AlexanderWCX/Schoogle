# import relevant stuff 
import xlrd
from xlutils.copy import copy

def writeNewUserToDB(email, password, postalCode):
	# open the userInformation workbook
	wb = xlrd.open_workbook('userInformation.xls')

	# open the userInformation worksheet
	ws = wb.sheet_by_name('userInformation')
	
	# read the number of records stored in this cell
	numOfRecords = int(ws.cell(0, 1).value)
	
	# if the email already exists inside the database, return False 
	# loop through each record to check
	for i in range(numOfRecords):
		# calculate the row
		row = 2 + i*4 
		
		# if email matches the email stored in that record
		if email == ws.cell(row, 0).value:
			# return False
			return False 

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
	



