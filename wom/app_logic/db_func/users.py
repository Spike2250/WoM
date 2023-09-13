import sqlite3
from wom.app_logic.db_func\
    .bucket_func_users import download_user_info_from_yandex_cloud_bucket


DATABASE = 'databases/users.db'


def login_check(login, password):

    if login == '' and password == '':
        return {'result': 'not full data'}

    create_users_db()

    user = login_read_user_from_db(login)
    if user is not None:
        if password == user['password']:
            download_user_info_from_yandex_cloud_bucket(user['user_id'])
            return {
                'result': 'success',
                'user_info': read_user_info(user['user_id'])
            }
        else:
            return {'result': 'wrong password'}
    else:
        return {'result': 'wrong login'}


def create_users_db():
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute('''
            CREATE TABLE
            IF NOT EXISTS
            users (
                user_id GUID PRIMARY KEY,
                email TEXT NOT NULL,
                login TEXT NOT NULL,
                password TEXT NOT NULL,
                name TEXT NOT NULL,
                dadname TEXT NOT NULL,
                surname TEXT NOT NULL,
                birthday TEXT NOT NULL,
                status TEXT NOT NULL)''')
        con.commit()
        print("SQLite: создаем таблицу users... ", end='')
        cur.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()


def insert_into_db_users(data_to_insert):
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute('''
            INSERT INTO users (
                user_id,
                email,
                login,
                password,
                name,
                dadname,
                surname,
                birthday,
                status)
            VALUES (?, ?, ?, ?, ?,
                    ?, ?, ?, ?)
            ''', data_to_insert)
        con.commit()
        print("SQLite: данные users успешно добавлены. ")
        cur.close()

        # write_json_user_info()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()


def update_db_users(data_to_update):
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        cur.execute('''
            UPDATE users
            SET email = ?,
                login = ?,
                password = ?,
                name = ?,
                dadname = ?,
                surname = ?,
                birthday = ?,
                status = ?,
            WHERE user_id = ?
            ''', data_to_update)
        con.commit()
        print("SQLite: данные users успешно обновлены. ")
        cur.close()

        # write_json_user_info()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()


def unpacking_data(data):
    if data is None:
        return None
    else:
        # распаковываем данные
        return {
            "user_id": data[0],
            "email": data[1],
            "login": data[2],
            "password": data[3],
            "name": data[4],
            "dadname": data[5],
            "surname": data[6],
            "birthday": data[7],
            "status": data[8],
        }


def read_user_from_db(key, value):
    '''
    '''
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        query = '''
            SELECT user_id,
                   email,
                   login,
                   password,
                   name,
                   dadname,
                   surname,
                   birthday,
                   status
            FROM users WHERE ? = ?'''
        cur.execute(query, [key, value])
        data = cur.fetchone()
        cur.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()
            return unpacking_data(data)


def login_read_user_from_db(login):
    '''
    '''
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        query = '''
            SELECT user_id,
                   email,
                   login,
                   password,
                   name,
                   dadname,
                   surname,
                   birthday,
                   status
            FROM users WHERE login = ?'''
        cur.execute(query, [login])
        data = cur.fetchone()
        cur.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()
            return unpacking_data(data)


def id_read_user_from_db(user_id):
    '''
    '''
    try:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()

        query = '''
            SELECT user_id,
                   email,
                   login,
                   password,
                   name,
                   dadname,
                   surname,
                   birthday,
                   status
            FROM users WHERE user_id = ?'''
        cur.execute(query, [user_id])
        data = cur.fetchone()
        cur.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if con:
            con.close()
            return unpacking_data(data)
