from google.cloud import vision
from google.cloud.vision import types
import io

import sys
from os import listdir, makedirs
from os.path import isfile, join, exists
from shutil import copyfile

def create_folder(path):
    if not exists(path):
        makedirs(path)

def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()
    # [START migration_text_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.text_detection(image=image)
    res = 'None'
    texts = response.text_annotations
    try:
        res = texts[0].description
    except:
        print('error string at file: ' + path)

    return res

if __name__ == '__main__':
    path_out_false = '../output_false'
    path_out_true = '../output_true'
    create_folder(path_out_false)
    create_folder(path_out_true)
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        path = '../input'
    files = [f for f in listdir(path) if isfile(join(path, f))]
    if len(files) == 0:
        sys.stderr.write('2ERROR: Could not file in folder "%s"\n' % path)
        exit(1)
    file_csv = '../DateCropped_0107_M.csv'
    n_exactly = 0
    n_image = 0
    for file in files:
        # print(file)
        out_str = detect_text(join(path, file))
        out_str = out_str.replace(' ', '').replace('\n', '')
        out_str = ''.join(e for e in out_str if e.isalnum())
        data_file_csv = open(file_csv, 'a')
        data_file_csv.write(file.split('.')[0].split('__')[1] + ',' + out_str + '\n')
        if out_str.replace('年', '_').replace('月', '_').replace('日', '').replace('平成', 'H') == \
                file.split('.')[0].split('__')[1].replace('~', ''):
            n_exactly = n_exactly + 1
            copyfile(join(path, file), join(path_out_true, file))
        else:
            copyfile(join(path, file), join(path_out_false, file))
        n_image = n_image + 1
        print('acc = ' + str(n_exactly) + ' / ' + str(n_image))
    print('precision = ' + str(n_exactly * 100.0 / n_image))