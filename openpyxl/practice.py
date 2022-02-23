from openpyxl import load_workbook


wb = load_workbook(filename = 'List.xlsx')
print(wb)
sheet_ranges = wb['1300']

# 새롭게 저장된 형태로 변경한다. 
'''
print(sheet_ranges['C18'].value)

cell_range = sheet_ranges['C2':'C1269']
print(cell_range)

for x in cell_range:
    print(x)
colC = sheet_ranges['C']
print(colC)

'''

'''''
for row in sheet_ranges.values:
    for value in row:
        print(value)
'''

for value in sheet_ranges.iter_cols(min_row=1, max_row=1269, min_col=3, max_col=3, values_only=True):
    for i in value:
        print(i)


# print(sheet_ranges.cell(row = 3).value)


# wb2 = openpyxl.load_workbook('./List.xlsx')
# print(type(wb2.sheetnames))

