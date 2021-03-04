import os
from pathlib import Path
import zipfile

pathlist = Path('../data/torch_dataset_original/').glob('**/*.zip')
print(pathlist)

for path in pathlist:
    if zipfile.is_zipfile(str(path)):
        db_id = path.stem[:3]
        print('Reading:', db_id, path.stem)
        with zipfile.ZipFile(path) as zip:
            for filename in zip.namelist():
                zip.extract(filename, path=db_id)
    else:
        print(path, 'NOT a valid zip file')