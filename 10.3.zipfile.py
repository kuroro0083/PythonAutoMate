import zipfile, os
from pathlib import Path

# 创建zip file
# newZip = zipfile.ZipFile('./file/test.zip', 'w')
# newZip.write('./file/10', compress_type=zipfile.ZIP_DEFLATED)
# newZip.close()

# 读取zip file
# exZip = zipfile.ZipFile('./file/test.zip')

# 压缩目录
newZip = zipfile.ZipFile('./file2/test.zip', 'w')

for folderName, subFolders, filenames in os.walk(Path('./file')):
    for f in filenames:
        tmpFilename = Path(folderName) / Path(f)
        newZip.write(str(tmpFilename), compress_type=zipfile.ZIP_DEFLATED)
    # print(folderName)
    # print(subFolders)
    # print(filenames)
    # print("---")
newZip.close()