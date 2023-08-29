import os
import json
from pathlib import Path


# чтение альманаха из json в словарь
def read_almanac():
    '''
    '''
    json_dict_name = f'Almanac.json'
    file_path_d_json = Path(Path.cwd(), 'wom/Almanac', json_dict_name)
    # проверяем наличие такого файла в директории
    if os.path.exists(file_path_d_json):
        with open(file_path_d_json, 'r') as file:
            d = json.load(file)
        return d
    else:
        return None


# запись альманаха в json
def almanac_json_recording(d):
    # записываем словарь в отдельный файл в формате json
    json_dict_name = f'Almanac.json'
    json_file_path = Path(Path.cwd(), 'Almanac', json_dict_name)
    with open(json_file_path, 'w') as file:
        json.dump(d, file, indent=4)
