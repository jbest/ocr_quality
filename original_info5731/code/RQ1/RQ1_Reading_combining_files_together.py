# reading all the txt files and saving them as one csv file

import requests
import os

data_directories = ['data'] # don't need the rest of the directories, they are created by unzipping data files
#,'data/google','data/tesseract']
#,'data/google/primary_label','data/google/full','data/tesseract/primary_label','data/tesseract/full']

# make directory to store data
for data_directory in data_directories:
  try:
    os.mkdir(data_directory)
  except FileExistsError:
    print(f'Directory \'{data_directory}\' already exists.')


# download Google OCR zip file
url = 'https://github.com/jbest/ocr_quality/raw/main/data/datasets/BRIT/ocr/BRIT_ocr_google.zip'
r = requests.get(url, allow_redirects=True)
with open('data/BRIT_ocr_google.zip', 'wb') as zip_file:
  zip_file.write(r.content)

""""
# download Tesseract OCR zip file 
url = 'https://github.com/jbest/ocr_quality/raw/main/data/datasets/BRIT/ocr/BRIT_ocr_tesseract.zip'
r = requests.get(url, allow_redirects=True)
with open('data/BRIT_ocr_tesseract.zip', 'wb') as zip_file:
  zip_file.write(r.content)
  """
from zipfile import ZipFile

# unzip Google OCR
zip_path = 'data/BRIT_ocr_google.zip'
data_path = 'data/'

with ZipFile(zip_path, 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall(path=data_path)

import glob
from pathlib import Path


all_txt=''
# print OCR data
for name in glob.glob('data/google/primary_label/*.txt'):
    file_path = Path(name)
    print(file_path.name, file_path.suffix, file_path.stem)
    with open(file_path) as doc_file:
        text = doc_file.read()
        all_txt = all_txt+text
        print(all_txt)
    with open('combined.csv', "w") as f1:
        f1.write(all_txt)

