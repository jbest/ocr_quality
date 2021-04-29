import requests
import pandas as pd

images_sample_path = 'images_sample.csv'
occurrences_sample_path = 'occurrences_sample.csv'

df_images_sample = pd.read_csv(images_sample_path, low_memory=False)
df_occurrences_sample = pd.read_csv(occurrences_sample_path, low_memory=False)

# get URLs of images from each sample
for i, row in df_images_sample.iterrows():
    #occurrence_id = row['id']
    #catalog_number = row['catalogNumber']
    #image_record = df_images.loc[df_images['coreid'] == occurrence_id]
    # download image
    dataset_id = row['dataset_id']
    image_coreid = row['coreid']
    image_url = row['accessURI']

    occurrence_record = df_occurrences_sample.loc[df_occurrences_sample['id'] == image_coreid]
    catalog_number = occurrence_record['catalogNumber'].values[0]
    file_name = str(catalog_number) + '_' +  str(dataset_id) + '_' + str(image_coreid) + '.jpg'
    print(catalog_number, file_name, image_url)
    try:
        response = requests.get(image_url)
    except Exception as e:
        print('Failed:', image_url, e)
        response = None

    if response is not None:
        if response.status_code == 200:
            with open(file_name, 'wb') as f:
                f.write(response.content)
