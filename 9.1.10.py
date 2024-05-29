from pathlib import Path
p = Path(Path.cwd())
for l in list(p.glob('*.py')):
    print(l)

p2 = Path('C:\win.ss')
print(p2.is_file())
