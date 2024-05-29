import re

idCardStr = "身份证号码是:440509198710292013，请确认。"
idRex = re.compile(r'(\d{6})(\d{8})(\d{4})')
mo = idRex.search(idCardStr)
# print([mo.group(1), mo.group(2), mo.group(3)])

newIdStr = idRex.sub(r'\1******\3', idCardStr)
print(newIdStr)

# agentNamesRegex = re.compile(r'Agent (\w)\w*')
# s = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
# print(s)

