import pprint
from pathlib import Path
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
catsFile = Path.cwd() / Path('file/cats94.py')
catsFile.write_text('cats='+pprint.pformat(cats))


import file.cats94
cats = file.cats94.cats
pprint.pprint(cats)


import shelve
catsDataPath = Path.cwd() / Path('shelve/catsData')
sl = shelve.open(str(catsDataPath))
sl['cats'] = cats
print(sl['cats'])
sl.close()


