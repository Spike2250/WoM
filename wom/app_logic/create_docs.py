import ast
import os
from docxtpl import DocxTemplate
from pathlib import Path
from wom.app_logic.service_func import create_short_name, convert_date
from wom.settings.config import (path_db_main_KS, path_db_main_DS,
                                 path_db_main_BTA_KS, path_db_main_BTA_DS,
                                 path_templates, path_templates_bta)


# установка пути к корневой папке
def path_main_folder_upg(d):
    path = ''
    if 'тип_стационара' in d:
        if d['тип_стационара'] in {'БТ - круглосуточный'}:
            path = path_db_main_BTA_KS
        elif d['тип_стационара'] in {'БТ - дневной'}:
            path = path_db_main_BTA_DS
        elif d['тип_стационара'] in {'Круглосуточный стационар'}:
            path = path_db_main_KS
        elif d['тип_стационара'] in {'Дневной стационар'}:
            path = path_db_main_DS
    return path


# установка пути к папке с шаблонами
def path_templates_upgrade(d):
    path = ''
    if 'тип_стационара' in d:
        if d['тип_стационара'] in {'БТ - круглосуточный', 'БТ - дневной'}:
            path = path_templates_bta
        else:
            path = path_templates
    return path


# генерация пути к файлу по файловой системе
def generate_path_to_new_file(d):
    pt_short_name = create_short_name(d['ФИО_пациента'])

    adm_date = convert_date(d['дата_поступления'])
    year_happening = f'{adm_date.strftime("%Y")} год'
    month_happening = f'{adm_date.strftime("%m")} - {adm_date.strftime("%B")}'
    date_happening = d['дата_поступления']
    folder_happening = f'{pt_short_name}, пост.{date_happening}'
    folder_name = f'{year_happening}/{month_happening}/{folder_happening}'
    if path_main_folder_upg(d) == '':
        path_new_file = f'UNKNOWN/{folder_name}'
    else:
        path_new_file = f'{path_main_folder_upg(d)}/{folder_name}'

    return path_new_file


def open_folder_with_files(d):
    os.startfile(Path(Path.cwd(), generate_path_to_new_file(d)))


# создание документов
def creating_documents(d, templates=None):
    if templates is None:
        templates = ['test']

    # перебираем список шаблонов и создаем документы
    for j in templates:
        if 'созданные_документы' not in d:
            d['созданные_документы'] = set()
            d['созданные_документы'].add(j)
        else:
            if isinstance(d['созданные_документы'], set):
                d['созданные_документы'].add(j)
            elif isinstance(d['созданные_документы'], str):
                d['созданные_документы'] = ast.literal_eval(
                    d['созданные_документы'])
                d['созданные_документы'].add(j)
        # создание имени нового файла и пути для его сохранения
        docName = f"{create_short_name(d['ФИО_пациента'])}, {j}.docx"
        # создаем путь к новому файлу
        path_new_file = generate_path_to_new_file(d)
        # формируем окончательное имя файла
        filepath = Path(Path.cwd(), path_new_file, docName)

        # создаем документ на основе шаблона
        doc = DocxTemplate(
            Path(Path.cwd(), path_templates_upgrade(d), j + '.docx'))
        # создание файла по шаблону на основе словаря
        doc.render(d)
        # создаем папок на пути к файлу
        os.makedirs(path_new_file, exist_ok=True)
        # сохранение файла по указанному пути, с указанным именем
        doc.save(filepath)