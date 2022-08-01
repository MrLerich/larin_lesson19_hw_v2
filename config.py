# файл конфигурации приложения, здесь может хранится путь к бд, ключ шифрования, что-то еще.
# Чтобы добавить новую настройку,
# допишите ее в класс

import base64


class Config:
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 4}
    PWD_HASH_SALT = base64.b64decode("salt")
    PWD_HASH_ITERATIONS = 100_000
    TOKEN_EXPIRE_MINUTES = 30
    TOKEN_EXPIRE_DAY = 3600
    ALGORITHM = "HS256"
    SECRET_KEY = '249y823r9v8238r9u'
