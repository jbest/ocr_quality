import os
from pathlib import Path
import zipfile
#from zipfile import ZipFile

#directory = os.fsencode('../data/torch_dataset_original/')
pathlist = Path('../data/torch_dataset_original/').glob('**/*.zip')
print(pathlist)

for path in pathlist:
    #file_path_string = str(os.path.join(directory, filename))
    #file_path = Path(file_path_string)
    
    if zipfile.is_zipfile(str(path)):
        db_id = path.stem[:3]
        print('Reading:', db_id, path.stem)
        with zipfile.ZipFile(path) as zip:
            #zip.printdir()
            print(zip)
            for filename in zip.namelist():
                print(filename)
                zip.extract(filename, path=db_id)


    else:
        print(path, 'NOT a valid zip file')