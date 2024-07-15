from app import db

# Створюємо клас Post, який наслідується від класу Model
# Цей клас містить поля id, title, content та date_posted
# Поле id є унікальним ідентифікатором кожного поста
# Поле title містить назву поста
# Поле content містить текст поста
# Поле date_posted містить дату та час створення поста
# Метод repr використовується для відображення об'єкта класу Post
# Цей метод повертає рядок, який містить назву поста та дату створення поста
# Цей метод використовується для відображення постів у консолі
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=db.func.current_timestamp())

    def repr(self):
        return f"Post('{self.title}', '{self.date_posted}')"