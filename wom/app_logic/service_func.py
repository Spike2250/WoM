from datetime import datetime
import json
from pathlib import Path
from decimal import Decimal


# из "дд.мм.гггг:" в datetime.datetime
def convert_date(date_string):
    # создаем список значений даты  | x = [дд, мм, гггг]
    x = [int(s) for s in date_string.split('.')]
    date = datetime(x[2], x[1], x[0])  # конвертируем формат
    return date


# запись словаря в json
def json_recording(d, type_=None):
    # записываем словарь в отдельный файл в формате json
    json_dict_name = f'{d["unic_number"]}.json'
    default_path = 'wom/JSON'
    folder_path = default_path if type_ is None else f'{default_path}/{type_}'
    json_file_path = Path(Path.cwd(), folder_path, json_dict_name)
    with open(json_file_path, 'w') as file:
        json.dump(d, file, indent=2)


def calc_percent_fullness(fullness, bta=False):
    if not bta:
        check_max = 12  # пока 12 с связи с недоделанными 3 разделами
    else:
        check_max = 7
    check = 0
    for i in fullness[0]:
        if i == '1':
            check += 1
    percent = Decimal(check * 100 / check_max).quantize(Decimal('1'))
    return int(percent)
