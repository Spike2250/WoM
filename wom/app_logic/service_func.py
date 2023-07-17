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


# РАЗНДАТ (для дней нетрудоспособности)
def datedif(date1, date2):
    ''' Функция принимает 2 числа в формате 'дд.мм.гггг'
        date1 дата от которой считаем
        date2 дата до которой считаем

        Вычисление количества дней между двумя датами с
        включением первого и последнего дня
        Например для вычисление количества дней нетрудоспособности
        от дня открытия больничного листа до даты ВК
    '''
    # конвертируем даты в datetime.datetime
    date1, date2 = convert_date(date1), convert_date(date2)

    delta = date2 - date1  # считаем разницу дат
    # выводим разницу дат + 1 (для включения дня отсчета)
    return delta.days + 1


def create_mkb_nmu_dict():
    # import json-файлов с МКБ-10 и Номенклатурой мед.услуг
    file_path_mkb10 = Path(__file__).parent / "handbooks/mkb10.json"
    file_path_nmu = Path(__file__).parent / "handbooks/nmu.json"

    with open(file_path_mkb10, 'r') as file:
        mkb10 = json.load(file)
    with open(file_path_nmu, 'r') as file:
        nmu = json.load(file)

    return mkb10, nmu


# расшифровка МКБ и НМУ (подписи для кодов)
def add_mkb10_nmu(d):
    '''
    Функция добавления к словарю расшифровок услуги и кода по МКБ-10
    '''
    mkb10, nmu = create_mkb_nmu_dict()
    # Добавляем расшифровки
    d['услуга_расшифровка'] = nmu[d['услуга']]
    d['МКБ10_расшифровка'] = mkb10[d['МКБ']]


def create_short_name(full_name):
    '''
    Создает из строки 'Иванов Иван Иванович'
         'Иванов_ИИ'
    '''
    # Разделяем строку на список слов
    splited_name = full_name.split(' ')
    short_name = ''
    for i in range(len(splited_name)):
        if i == 0:  # Берем целиком первое слово
            short_name = splited_name[i] + ' '
        else:  # И по первой букве от остальных
            short_name = short_name + splited_name[i][0]

    return short_name


# посчитать возраст на сегодня()
def count_age(d):
    '''
    Получение возраста в полных годах
        от даты рождения до сегодня (date.today())
    '''
    today = datetime.today()
    birthday = convert_date(d['дата_рождения'])
    age = today.year - birthday.year
    if today.month < birthday.month:
        age -= 1
    elif today.month == birthday.month and today.day < birthday.day:
        age -= 1

    return str(age)
