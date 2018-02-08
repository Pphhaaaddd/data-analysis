import xlrd
import numpy as np
import pandas as pd
workbook = xlrd.open_workbook("May17.xlsx")
sheet = workbook.sheet_by_index(0)
print("Number of Rows : ",sheet.nrows)
print("Number of Columns",sheet.ncols)


## Printing the sheet
# for row in range(sheet.nrows):
#     for col in range(sheet.ncols):
#         print(sheet.cell_value(row,col),'\t',end='')
#     print()

d = [[sheet.cell_value(r,c) for c in range(sheet.ncols) for r in range(sheet.nrows)]]
df = pd.DataFrame(data=d)
print(df)
