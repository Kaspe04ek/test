from flask import Flask, render_template, url_for
import db

db.clear_db()
db.create()
db.insert_db()

# Создаем объект нашего приложения
app = Flask(__name__)

@app.route('/')
def index():
    '''Функция возвращает html документ
    когда мы обращаемся на главную страницу ('/') '''
    return render_template('index.html')

@app.route('/test')
def test():
    result = db.get_random_question()
    question = result[1]
    answer = result[2]
    wrong1 = result[3]
    wrong2 = result[4]
    wrong3 = result[5]
    return render_template(
        'test.html',
        question = question,
        answer=answer,
        wrong1=wrong1,
        wrong2=wrong2,
        wrong3=wrong3
    )

# Если это главный файл - запусти приложение
if __name__ == "__main__":
    app.run()