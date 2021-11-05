from openpyxl import load_workbook
from datetime import datetime
wb1 = load_workbook('numbers.xlsx')
ws1 = wb1.active
for x in ws1.iter_rows():
    chip_id = str(x[0].value)
    datestring = (chip_id[0:6])
    dt = datetime.strptime(datestring, '%y%m%d')
    chip_date = dt.isoformat()
    x[0].value = chip_date
print("Ta dam!")
wb1.save('dates.xlsx')
idle = input("")