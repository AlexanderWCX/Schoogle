import xlrd 

# if email found, return the row index it is stored in
# else, return false 
def findEmailInDB(email):
	# open the userInformation workbook
	wb = xlrd.open_workbook('userInformation.xls')
	
	# open the userInformation worksheet
	ws = wb.sheet_by_name('userInformation')
	
	# read the number of records stored from this cell
	numOfRecords = int(ws.cell(0, 1).value)
	
	# loop through each record to check
	for i in range(numOfRecords):
		# calculate the row
		row = 2 + i*4 
		
		# if email matches the email stored in that record
		if email == ws.cell(row, 0).value:
			# return row index that holds that email 
			return row 
			
	# if exit the for loop without returning the row, it means that the email is not stored in the database 
	# hence, we return -1 
	return -1 
	
	
def passwordMatchesThatPairedWithEmailInDB(password, emailRow):
	# open the userInformation workbook
	wb = xlrd.open_workbook('userInformation.xls')
	
	# open the userInformation worksheet
	ws = wb.sheet_by_name('userInformation')
	
	# get the password stored in that record
	pw = ws.cell(emailRow, 1).value 
	
	# match that password with that passed as an argument into this function 
	if pw == password:
		# if match, return true
		return True 
	
	# else, return false 
	else: 
		return False 
	
	
	