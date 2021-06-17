import time
from os import environ
from pathlib import Path

import psycopg2
from dotenv import load_dotenv
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def connect(user, password, host, port, database):
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(
            # user=user,  # "postgres",
            # password=password,  # "1111",
            # # host="0.0.0.0",
            # host="127.0.0.1",
            # # host=host,
            # port=port,  # "5432"
            # database=database
            user="ruslan",
            password="ruslan",
            # host="0.0.0.0",
            # host="127.0.0.1",
            host='postgres',
            # host='localhost',
            port="5432",
            dbname="postgres"
        )

        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        # Распечатать сведения о PostgreSQL
        print("Информация о сервере PostgreSQL")
        print(connection.get_dsn_parameters(), "\n")
        # Выполнение SQL-запроса
        cursor.execute("SELECT version();")
        # Получить результат
        record = cursor.fetchone()
        print("Вы подключены к - ", record, "\n")

    except Exception as error:
        print(error)
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")

if __name__ == '__main__':
    env_path = Path(__file__).resolve(strict=True).parent.parent / ".envs" / '.postgresql'
    load_dotenv(dotenv_path=env_path)
    POSTGRES_HOST = environ.get('POSTGRES_HOST')
    POSTGRES_PORT = environ.get('POSTGRES_PORT')
    POSTGRES_DB = environ.get('POSTGRES_DB')
    POSTGRES_USER = environ.get('POSTGRES_USER')
    POSTGRES_PASSWORD = environ.get('POSTGRES_PASSWORD')
    print(POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT)
    connect(POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB)
