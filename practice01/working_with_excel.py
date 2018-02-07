import xlrd
workbook = xlrd.open_workbook("May17.xlsx")
sheet = workbook.sheet_by_index(0)
print("Number of Rows : ",sheet.nrows)
print("Number of Columns",sheet.ncols)

for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        print(sheet.cell_value(row,col),'\t\t',end='')
    print()
