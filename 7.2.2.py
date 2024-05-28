import re

# reStr = '\d{3}-\d{3}-\d{4}'
# phoneNumRex = re.compile(reStr)
# str = 'There is two phone number, one is 432-987-2258, another one is 212-587-2115'
# mo = phoneNumRex.findall(str)
# print(mo)

# batRegex = re.compile('Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a wheel')
# print(mo.group())
# print(mo.group(1))

endWithNumber = re.compile('\d+$')
print(endWithNumber.findall('Your number is 43'))
