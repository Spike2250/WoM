import boto3


BUCKET_MAIN = 'omrdbjson'


# Yandex Object Storage Access
os = boto3.client(
    's3',
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
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
def upload_to_bucket(bucket_name, object_name):
    os.upload_file(f"wom/JSON/{object_name}", bucket_name, object_name)
    print(f'{object_name} успешно загружен в bucket YandexCloud')


# Загрузить объект из бакета
def download_from_bucket(bucket_name, object_name):
    os.download_file(bucket_name, object_name, f"wom/JSON/{object_name}")
    print(f'{object_name} успешно скачан из bucket YandexCloud')


# Удалить объект из бакета
def delete_from_bucket(bucket_name, object_name):
    os.delete_object(Bucket=bucket_name, Key=object_name)


# Запись БД в бакет
def upload_db_to_bucket(bucket_name, db_name):
    os.upload_file(db_name, bucket_name, db_name)
    print(f'База данных {db_name} успешно загружена в bucket YandexCloud')


# Загрузить БД из бакета
def download_db_from_bucket(bucket_name, db_name):
    os.download_file(bucket_name, db_name, db_name)
    print(f'База данных {db_name} успешно скачана из bucket YandexCloud')
