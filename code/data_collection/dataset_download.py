# Modified from https://github.com/jbest/symbiota_tools
"""
Retrieve CSV/ZIP dataset from a Symbiota portal

This script downloads botanical specimen data from data portals which are based
on the Symbiota web application.

The search and download process generally starts at the collection search interface:
https://portal.torcherbaria.org/portal/collections/list.php
This is where the collection(s) is/are selected which provide the db value(s) which 
are hidden in the download form.
The search criteria form:
https://portal.torcherbaria.org/portal/collections/harvestparams.php
is where other parameters are input (taxonomy, geography, etc)
The results page:
https://portal.torcherbaria.org/portal/collections/list.php
displays a list of the matches. On this page is the download link which opens
the download form and the form handler which is used by this script.

"""
import requests
import urllib.parse

# Query parameters
# All collection db IDs in the TORCH portal
db_list = [158, 175, 223, 264, 309, 354, 365, 366, 370, 387, 422, 456, 459, 463, 473, 474, 475, 483, 485, 488, 491]

for db_id in db_list:
    db = str(db_id)

    hasimages = 1
    #search_params = {'db': db, 'state': state, 'county': county, 'hasimages': hasimages}
    search_params = {'db': db, 'hasimages': hasimages}

    searchvar = urllib.parse.urlencode(search_params)
    print(searchvar)
    #searchvar = 'db=370&state=Texas&county=Tarrant&hasimages=1'

    # Download format parameters
    url = 'https://portal.torcherbaria.org/portal/collections/download/downloadhandler.php'
    schema = 'dwc' # Darwin Core
    file_format = 'csv' #form field name is 'format'
    cset = 'utf-8'
    publicsearch = '1'
    taxonFilterCode = '0'
    sourcepage = 'specimen'
    images = '1' # include images - 1, only includes image records
    zip_file = '0' # form field name is zip, default to not zip file
    if images == '1': # results must be zipped to get both specimen and image records
        zip_file = '1' # form field name is zip


    r = requests.post(url, data={'schema': schema, 'format': file_format, 
        'cset': cset, 'publicsearch': publicsearch, 
        'taxonFilterCode': taxonFilterCode, 
        'images': images, 'zip':zip_file,
        'sourcepage': sourcepage, 'searchvar': searchvar},
        stream=True)

    # Save data
    if zip_file == '0':
        #Save CSV
        filename = db + '-symbiota_data.csv'
        with open(filename, 'w') as data_file:
            data_file.write(r.text)
        print(f'File {filename} saved.')

    if zip_file =='1':
          # Save ZIP
          filename = db + '-symbiota_data.zip'
          with open(filename, 'wb') as zip_file:
            for chunk in r.iter_content(chunk_size=128):
                zip_file.write(chunk)
          print(f'File {filename} saved.')


  