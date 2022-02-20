from openpyxl import Workbook

wb = Workbook()



ws = wb.active


ws1 = wb.create_sheet("Mysheet")

ws2 = wb.create_sheet("Mysheet", 0)

ws3 = wb.create_sheet("Mysheet", -1)


ws1.title = "New Title"

ws.sheet_properties.tabColor = "1072BA"


ws3 = wb["New Title"]


print(wb.sheetnames)


for sheet in wb:
    print(sheet.title)


source = wb.active

target = wb.copy_worksheet(source)

print(target)


c = ws['A4']

ws['A4'] = 4

print(c)

d = ws.cell(row=4, column=2, value=10)

print(d)



