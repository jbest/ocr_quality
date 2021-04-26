# adapted from https://cloud.google.com/vision/docs/ocr

from google.protobuf.json_format import MessageToJson
from pathlib import Path
import glob

#image_directory = '/home/jbest/specimen_segmentation_tests/datasets/BRIT/images/primary_labels/'
#image_directory = '/home/jbest/git/ocr_quality/data/datasets/BRIT/images/primary_label/'
image_directory = '/home/jbest/git/ocr_quality/data/datasets/BRIT/images/primary_label/'
ocr_directory = '/home/jbest/git/ocr_quality/data/datasets/BRIT/ocr/primary_label/'
#ocr_directory_path = Path(ocr_directory)
images_glob_string = image_directory + '*.jpg'

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    annotations = response.text_annotations
    full_annotation = str(response.full_text_annotation)
    # get plain text
    if len(annotations) > 0:
        text = annotations[0].description

    else:
        text = ''

    return text

#image_path = '/home/jbest/specimen_segmentation_tests/datasets/BRIT/images/primary_labels/BRIT01310_370-symbiota_data_14231876_primary_label.jpg'
#images= ['/home/jbest/specimen_segmentation_tests/datasets/BRIT/images/primary_labels/BRIT01310_370-symbiota_data_14231876_primary_label.jpg']

# create list of ocred images

ocr_directory_path = Path(ocr_directory)
images_ocred = []
images_ocred_glob_string = ocr_directory + '*.txt'
images_ocred_glob = glob.glob(images_ocred_glob_string)
for image_ocred in images_ocred_glob:
    images_ocred.append(image_ocred)

#images_ocred = ['/home/jbest/git/ocr_quality/data/datasets/BRIT/ocr/BRIT397154_370-symbiota_data_26796018_ocr.txt', '/home/jbest/git/ocr_quality/data/datasets/BRIT/ocr/BRIT397154_370-symbiota_data_26796018_ocr.txt'] 
    # images with OCR results already in the destination folder
images = glob.glob(images_glob_string)

for image in images:
    #print(image)
    image_path = Path(image)

    result_file = image_path.stem + '_ocr.txt'

    # check if result file is already in destination folder
    result_file_path = ocr_directory_path.joinpath(result_file)
    #print(result_file_path)
    #result_json = MessageToJson(result)
    #print('result type:', type(result))
    
    
    if str(result_file_path) in images_ocred:
        print('image already ocred:', result_file_path)
    else:
        #perform OCR
        print('OCR:', image)
        result = detect_text(image_path)
        #print(result_file_path)
        with open(result_file_path, 'w') as result_file:
            result_file.write(str(result))
