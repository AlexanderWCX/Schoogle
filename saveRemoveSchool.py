# import relevant libraries
import xlrd
from xlutils.copy import copy
from verifyEmailAndPassword import findEmailInDB 

# save school
def saveSchool(email, schoolName, savedDate): 
	wb = xlrd.open_workbook('userInformation.xls')
	ws = wb.sheet_by_name('userInformation')
	newWB = copy(wb)
	newWS = newWB.get_sheet(0)
	
	# gives the row index where that email is stored 
	row = findEmailInDB(email)  
	
	# if row == -1, the email is not in the database 
	if row == -1:
		# cannot save that school
		return False 
		
	# retrieve number of schools stored in that record
	numOfSchools = int(ws.cell(row + 1, 0).value) 
	
	# increment the number of schools saved
	numOfSchools += 1

	# write the new number of schools saved to the record
	newWS.write(row + 1, 0, numOfSchools) 
	
	# at the matching column index, write the new school and its saved date
	newWS.write(row + 1, numOfSchools, schoolName)
	newWS.write(row + 2, numOfSchools, savedDate)

	# move one cell to the right and write 'end' to it
	newWS.write(row + 1, numOfSchools + 1, 'end')
	newWS.write(row + 2, numOfSchools + 1, 'end') 
	
	newWB.save('userInformation.xls') 
	
	# school is successfully saved 
	return True 
	
# delete school 
def deleteSavedSchool(email, schoolName):
	# make a copy of the workbook and make changes to it
	wb = xlrd.open_workbook('userInformation.xls') 
	ws = wb.sheet_by_name('userInformation') 
	newWB = copy(wb)
	newWS = newWB.get_sheet(0)
	
	# gives the row index where the email is stored 
	row = findEmailInDB(email)
	
	# if email does not exist in the database 
	if row == -1:
		# cannot delete 
		return False
		
	# retrieve number of schools stored in that record
	numOfSchools = int(ws.cell(row + 1, 0).value)
	
	# decrement the number of schools saved
	numOfSchools -= 1

	# write the new number of schools saved to the record
	newWS.write(row + 1, 0, numOfSchools)
	
	# initialize col
	col = 1

	# initialize sn
	sn = ws.cell(row + 1, col).value

	# while we have not reached 'end'
	while (sn != 'end'):

		# compare sn with schoolName
		if sn == schoolName:
			break

		else:
			col += 1
			sn = ws.cell(row + 1, col).value
			
	# if sn == 'end'
	if (sn == 'end'):
		print('The school is not saved!')
		return False

	# increment col
	col += 1
	
	# get the next sn
	sn = ws.cell(row + 1, col).value
	sd = ws.cell(row + 2, col).value

	# loop through the remaining cells till 'end' and shift them left by one column each
	while (sn != 'end'):

		# shift the school name left by one cell
		newWS.write(row + 1, col - 1, sn)

		# shift the saved date left by one cell
		newWS.write(row + 2, col - 1, sd)

		# move on to the next school
		col += 1
		sn = ws.cell(row + 1, col).value
		sd = ws.cell(row + 2, col).value

	# shift 'end' left by one cell
	newWS.write(row + 1, col - 1, 'end')
	newWS.write(row + 2, col - 1, 'end')
	newWS.write(row + 1, col, '')
	newWS.write(row + 2, col, '')

	newWB.save('userInformation.xls') 
	
	# removal successful 
	return True
	