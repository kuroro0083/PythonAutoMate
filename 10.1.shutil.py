import shutil, os
from pathlib import Path

p = Path('file/10')
i = 1
for filename in p.iterdir():
    newFilename = Path(f'file/10/{i}.txt')
    shutil.move(filename, newFilename)
    i += 1
    print(str(filename) + ' ==> ' + str(newFilename))
