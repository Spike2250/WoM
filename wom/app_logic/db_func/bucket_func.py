import boto3
from wom.app_logic.db_func.db_omr import DATABASE
from env import aws_access_key_id, aws_secret_access_key


BUCKET_MAIN = 'omrdbjson'


# Yandex Object Storage Access
os = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name='ru-central1',
    endpoint_url='https://storage.yandexcloud.net'
)


# Перечень корзин
def print_list_buckets():
    for bucket in os.list_buckets()['Buckets']:
        print(bucket['Name'])


# Перечень объектов в бакете
def print_keys_from_bucket(bucket_name):
    for key in os.list_objects(Bucket=bucket_name)['Contents']:
        print(key['Key'])


# Создание бакета
def make_bucket(bucket_name):
    os.create_bucket(Bucket=bucket_name)


# Запись объекта в бакет
def upload_to_bucket(bucket_name, object_name, folder):
    os.upload_file(f"wom/JSON/{folder}/{object_name}",
                   bucket_name, object_name)
    print(f'{object_name} успешно загружен в bucket YandexCloud')


# Загрузить объект из бакета
def download_from_bucket(bucket_name, object_name, folder):
    os.download_file(bucket_name, object_name,
                     f"wom/JSON/{folder}/{object_name}")
    print(f'{object_name} успешно скачан из bucket YandexCloud')


# Удалить объект из бакета
def delete_from_bucket(bucket_name, object_name):
    os.delete_object(Bucket=bucket_name, Key=object_name)


# Запись БД в бакет
def upload_db_to_bucket(bucket_name, db_name):
    os.upload_file(f"databases/{db_name}", bucket_name, db_name)
    print(f'База данных {db_name} успешно загружена в bucket YandexCloud')


# Загрузить БД из бакета
def download_db_from_bucket(bucket_name, db_name):
    os.download_file(bucket_name, db_name, f"databases/{db_name}")
    print(f'База данных {db_name} успешно скачана из bucket YandexCloud')


def download_case_from_yandex_cloud_bucket(type_):
    def wrapper(read_d):
        def inner(*args, **kwargs):
            download_from_bucket(bucket_name=BUCKET_MAIN,
                                 folder=type_.upper(),
                                 object_name=f'{args[1]}.json')
            read_d(*args, **kwargs)
        return inner
    return wrapper


def upload_history_to_yandex_cloud_bucket(type_):
    def wrapper(save_history):
        def inner(d):
            # скачиваем актуальную БД из бакета
            # (для минимизации возможного расхождения с уже скачаной)
            download_db_from_bucket(bucket_name=BUCKET_MAIN,
                                    db_name=DATABASE)
            # сохраняем данные
            save_history(d)
            # загружаем в бакет
            upload_db_to_bucket(bucket_name=BUCKET_MAIN,
                                db_name=DATABASE)
            upload_to_bucket(bucket_name=BUCKET_MAIN,
                             folder=type_.upper(),
                             object_name=f"{d['unic_number']}.json")
        return inner
    return wrapper
