import re

# 18题
# numRegex = re.compile(r'\d+')
# newStr = numRegex.sub('X', '12drummers, 11 pipers, five rings, 3 hens')
# print(newStr)

# 20题
rexStr = r'^\d{1,3}(,{3})*$'
rexValue = re.compile(rexStr)
testStrList = ['42', '1,234', '6,368,745', '12,34,567', '1234']
# for tsl in testStrList:
#     mo = rexValue.search(tsl)
#     print(mo.group() if mo is not None else 'no')
testStr = '1,234'
mo = rexValue.search(testStr)
print(mo)
