import xlwt

workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet('sheet1')

for i in range (1,10):
	for j in range (1,i+1):
			worksheet.write(i-1,j-1,'%d*%d=%d'%(i,j,i*j))	# (行，列，内容)


workbook.save('student.xls')


