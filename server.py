from flask import Flask
from flask import url_for
import os

app = Flask(__name__)


@app.route('/')
def index_1():
    return """<title>Привет, Марс!</title>
<h1>Миссия Колонизация Марса<h1>"""


@app.route('/index')
def index():
    return """<title>Привет, Марс!</title>
<h1>И на Марсе будут яблони цвести!<h1>"""


@app.route('/promotion')
def promotion():
    return '''<title>Привет, Марс!</title>
    <pre>Человечество вырастает из детства.
Человечеству мала одна планета.
Мы сделаем обитаемыми безжизненные пока планеты.
И начнем с Марса!
Присоединяйся!</pre>'''


@app.route('/image_mars')
def image_mars():
    return '''<title>Привет, Марс!</title>
<h1>Жди нас, Марс!</h1>
<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQFRXfsvWCzaY6AEP1hPu0Nu0MPeDK5KuGbQ&s' alt='Картинка Марса'>
<h3>Вот она какая, красная планета.</h3>'''


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />  
                    <integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/image.jpg" alt="Картинка Марса">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <div class="alert alert-secondary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)