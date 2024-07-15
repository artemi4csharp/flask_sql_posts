# Опис: Файл конфігурації для додатку
# Цей файл містить клас Config, який містить налаштування для додатку
# Цей клас містить налаштування для секретного ключа та бази даних
# Якщо змінна середовища SECRET_KEY не встановлена, то використовується значення за замовчуванням
# Якщо змінна середовища DATABASE_URL не встановлена, то використовується база даних SQLite
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False