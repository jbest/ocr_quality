"""
Generate a data sample from full project dataset


"""

from pathlib import Path
import pandas as pd
import requests

rootdir = Path('../data/dataset_expanded/') # path of directory containing unzipped data
sample_size = 10
random_state = 1 # used to keep random seed value constant to make reproducible samples from dataset


dir_list = [d for d in rootdir.iterdir() if d.is_dir()]

print(dir_list)
df_occurrences = pd.DataFrame()
df_images = pd.DataFrame()
for d in dir_list:
    print(d)
    dataset_directory = d.name
    # get dataset identifier
    #dataset_id = dataset_directory.split('-')[0] #changed directory name convention
    dataset_id = dataset_directory
    print(dataset_id)
    occurrences_path = d.joinpath('occurrences.csv')
    images_path = d.joinpath('images.csv')
    # load the occurrences file from a Darwin Core Archive
    df_occurrences_temp = pd.read_csv(occurrences_path, low_memory=False)
    print(df_occurrences_temp.shape)
    # add datset id
    df_occurrences_temp['dataset_id'] = dataset_id
    # append to existing occurrence data
    df_occurrences = pd.concat([df_occurrences, df_occurrences_temp])
    print(df_occurrences.shape)
    # load the images file from a Darwin Core Archive
    df_images_temp = pd.read_csv(images_path, low_memory=False)
    print(df_images_temp.shape)
    df_images_temp['dataset_id'] = dataset_id
    # append to existing image data
    df_images = pd.concat([df_images, df_images_temp])
    print(df_images.shape)

# Occurrences with images
df_occurrences_with_images = df_occurrences[df_occurrences['id'].isin(df_images['coreid'])]
print(df_occurrences_with_images.shape)

# Get sample from each collection dataset
df_occurrences_sample = df_occurrences_with_images.groupby('dataset_id').sample(n=sample_size, random_state=random_state)

# Get image records corresponding to occurrence sample
df_images_sample = df_images[df_images['coreid'].isin(df_occurrences_sample['id'])]
print(df_images_sample.shape)

#dup_images = df_images_sample.duplicated(subset='coreid')
#print(dup_images.sum())

df_occurrences_sample.to_csv('occurrences_sample.csv', index=False)
df_images_sample.to_csv('images_sample.csv', index=False)

"""
# get URLs of images from each sample
for i, row in df_occurrences_sample.iterrows():
    occurrence_id = row['id']
    catalog_number = row['catalogNumber']
    image_record = df_images.loc[df_images['coreid'] == occurrence_id]
    # download image
    image_url = image_record['accessURI'].values[0]
    print(catalog_number, image_url)
    file_name = catalog_number + '.jpg'
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(response.content)
"""