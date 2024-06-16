import os
from pathlib import Path

for folderName, subFolders, filenames in os.walk(Path.cwd()):
    print(folderName)
    print(subFolders)
    print(filenames)
    print("---")

