import shelve
from pathlib import Path
filePath = str(Path.cwd() / 'shelve' / 'mydata')
shelfFile = shelve.open(filePath)

# 写入二进制文件
# cats = ['Zophie', 'Pooka', 'Simon']
# shelfFile['cats'] = cats


# 读取二进制文件
print(shelfFile['cats'])

# 关闭
shelfFile.close()