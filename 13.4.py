import openpyxl

wb = openpyxl.load_workbook('./file/13/censuspopdata.xlsx')
sheet =  wb.active()

countyData = {}
