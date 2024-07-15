# В цьому файлі ми ініціалізуємо нашу програму та базу даних
# Імпортуємо клас Flask з бібліотеки flask та клас SQLAlchemy з бібліотеки flask_sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Створюємо екземпляр класу Flask
app = Flask(__name__)
# Встановлюємо конфігурацію для бази даних та секретного ключа
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/flaskblog.sqlite'
app.config['SECRET_KEY'] = 'your_secret_key'
# Ініціалізуємо базу даних
db = SQLAlchemy(app)
with app.app_context():
    from app import routes, models
    db.create_all()
