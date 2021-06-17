import time
from os import environ
from pathlib import Path

import psycopg2
from dotenv import load_dotenv
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def create_table(cursor, connection):
    # SQL-запрос для создания новой таблицы
    create_table_query = '''CREATE TABLE mobile
                              (ID INT PRIMARY KEY     NOT NULL,
                              MODEL           TEXT    NOT NULL,
                              PRICE         REAL); '''
    # Выполнение команды: это создает новую таблицу
    result = cursor.execute(create_table_query)
    connection.commit()

def connect(user, password, host, port, database):
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(
            user=user,  # "postgres",
            password=password,  # "1111",
            host=host,
            port=port,  # "5432"
            database=database
        )

        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        # Распечатать сведения о PostgreSQL
        # Выполнение SQL-запроса
        create_table(cursor, connection)
    except Exception as error:
        print(error)
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
    # while True:
    #     print('I am sleeping', user)
    #     time.sleep(10)
    #     pass


if __name__ == '__main__':
    env_path = Path(__file__).resolve(strict=True).parent / '.postgresql'
    load_dotenv(dotenv_path=env_path)
    POSTGRES_HOST = environ.get('POSTGRES_HOST')
    POSTGRES_PORT = environ.get('POSTGRES_PORT')
    POSTGRES_DB = environ.get('POSTGRES_DB')
    POSTGRES_USER = environ.get('POSTGRES_USER')
    POSTGRES_PASSWORD = environ.get('POSTGRES_PASSWORD')
    connect(POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB)
