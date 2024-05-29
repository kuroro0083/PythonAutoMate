import pathlib

# 各部分元素的解释
# 锚点 anchor
# 父文件夹 parent
# 文件名 name
# 主干名 stem
# 后缀名 suffix
# 驱动器 drive（限windows）
ph = pathlib.Path('C:\Windows\Tes\kkk.txt')
print(ph.anchor)
print(ph.parent)
print(ph.name)
print(ph.stem)
print(ph.suffix)
print(ph.drive)

