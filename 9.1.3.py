from pathlib import Path
import os

print(Path.cwd())  # 当前工作目录

# 目录的链接
homeFolder = Path('C:/Users')
subFolder  = Path('ai')

print(homeFolder/subFolder)
