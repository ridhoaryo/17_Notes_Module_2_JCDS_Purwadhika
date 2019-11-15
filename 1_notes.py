import xlsxwriter

file = xlsxwriter.Workbook('z.xlsx')
sheet = file.add_worksheet('data')

# sheet.write(0,0,1)
# sheet.write(0,1,'=A1+200')
# sheet.write(0,2,'=SUM(A1:B1)')

for i in range(10):
    sheet.write(i,0,i)

file.close()

import xlrd
file = xlrd.open_workbook('z.xlsx')
sheet = file.sheet_by_name('data')
for i in range(sheet.nrows):
    print(sheet.cell_value(i,0))