from pathlib import Path
# 写入文件
filePath = Path.cwd() / Path('file/9.2.txt')
# len = filePath.write_text('hello world', newline='\n')
# print(len)

# 写入文件2
f = filePath.open('a+')
f.write('hello world2\n')
f.write('hello world!!!\n')
f.close()

# helloFile = open(filePath)
# helloContent = helloFile.read()
# helloContentList = helloFile.readlines()
# print(helloContent)
# print(helloContentList)
