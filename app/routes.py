from flask import render_template, url_for, flash, redirect, request
from app import app, db
from app.models import Post

# Створюємо маршрут для домашньої сторінки
# Цей маршрут відображає всі пости на домашній сторінці
# Для цього ми використовуємо шаблон home.html
# Цей шаблон містить всі пости, які ми передаємо у змінній posts
# Цей маршрут використовує метод query.all(), який повертає всі пости з бази даних
# Цей метод використовується для вибору всіх записів з таблиці Post
@app.route('/')
@app.route('/home')
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)

# Створюємо маршрут для посту
# Цей маршрут відображає пост з конкретним id
# Цей маршрут використовує шаблон post.html
# Цей шаблон містить назву та текст поста
# Цей маршрут використовує метод query.get_or_404(post_id), який повертає пост з конкретним id
# Якщо пост не знайдено, то відображається сторінка 404
# Цей метод використовується для вибору запису з таблиці Post з конкретним id
@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

# Створюємо маршрут для створення нового поста
# Цей маршрут відображає форму для створення нового поста
# Цей маршрут використовує шаблон create_post.html
# Цей шаблон містить форму для створення нового поста
# Цей маршрут використовує методи GET та POST
# Якщо метод GET, то відображається форма для створення нового поста
# Якщо метод POST, то дані з форми передаються на сервер
# Після цього створюється новий пост та зберігається в базі даних
# Після цього відображається повідомлення про успішне створення поста
# Цей маршрут використовує метод request.form, який містить дані з форми
# Цей метод використовується для отримання даних з форми
@app.route('/post/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post')
# Створюємо маршрут для редагування поста
# Цей маршрут відображає форму для редагування поста з конкретним id
# Цей маршрут використовує шаблон edit_post.html
# Цей шаблон містить форму для редагування поста
# Цей маршрут використовує методи GET та POST
# Якщо метод GET, то відображається форма для редагування поста
# Якщо метод POST, то дані з форми передаються на сервер
# Після цього пост з конкретним id редагується та зберігається в базі даних
# Після цього відображається повідомлення про успішне оновлення поста
# Цей маршрут використовує метод request.form, який містить дані з форми
# Цей метод використовується для отримання даних з форми
@app.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    return render_template('edit_post.html', title='Edit Post', post=post)

# Створюємо маршрут для видалення поста
# Цей маршрут видаляє пост з конкретним id
# Після цього відображається повідомлення про успішне видалення поста
# Цей маршрут використовує методи POST
# Цей маршрут використовує метод db.session.delete(post), який видаляє пост з бази даних
# Цей метод використовується для видалення запису з таблиці Post з конкретним id
@app.route('/post/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))
