import openpyxl, pprint

print('loading xlsx file')
wb = openpyxl.load_workbook('./file/13/censuspopdata.xlsx')
sheet =  wb['Population by Census Tract']

countyData = {}

print('analying file')
for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)

print('writing file')
resultFile = open('13.census2021.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
print('done')
