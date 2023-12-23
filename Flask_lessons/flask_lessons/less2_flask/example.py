from flask import Flask, request, render_template, redirect, url_for, session, flash, jsonify, get_flashed_messages
import json
import os


# users = [
#     'mike',
#     'mishel',
#     'adel',
#     'keks',
#     'kamila'
# ]


# создаем экз класса Flask и передаем в него имя модуля
app = Flask(__name__)


app.config['SECRET_KEY'] = 'asasa' # для шифрования данных



@app.route('/') # декоратор для обработки запросов к серверу
def hello_world():
    return "Welcome to Flask" # функция обработчик возращает ответ
# который буде выведен в браузере(отправлен клиенту)

# @app.route('/users', methods=['GET', 'POST']) #процесс указания метода с помощью requests
# def users():
#     if request.method == 'POST':
#         return "Hello from POST /users"
#     else:
#         return "Hello from GET /users"

# #процесс указания метода с помощью отдельных декораторов
# @app.get('/users')
# def users_g():
#     return "Hello from GET /users"


#для каждого метода декоратор отдельный
# @app.post('/users')
# def users_p():
#     return "Users", 418


# @app.get('/users')
# def get_users():
#     term = request.args.get('term')
#     if not term:
#         res = users
#     else:
#         res = [user for user in users if term in user]
#     return render_template(
#         '/users/index.html',
#         search=res,
#         term=term,
#         )  

id = 0




def get_next_id(): # функция считает id и возвращает его для каждого пользователя 
    # если он еще не существует, то он создается и записывается в файл 
    # если он уже существует, то он просто загружается из файла и он используется 
    # для каждого пользователя 
    # если он еще не существует, то он создается и записывается в файл
    global id
    id += 1
    return id


@app.post('/users')
def user(): # функция для добавления пользователя в файл 
    # и записи его в базу данных, присваивая ему id и записывая его в файл
    user = request.form.to_dict()
    user['id'] = get_next_id()
    with open('user.json', 'w+') as file:
        file.write(json.dumps(user))
    flash('User created successfully', 'success') # функция для вывода сообщения на страницу
    return redirect('/users', code=302,)



@app.get('/users')
def get_user(): # возвращает информацию о пользователе из файла 
    # и отображает её на странице
    messages = get_flashed_messages(with_categories=True)
    print(messages)                                                                           
    with open('user.json') as file:
        user = json.loads(file.read())
    return render_template(
        'users/user.html',
        user=user,
        messages=messages,
    )
    
    

@app.route('/users/new')
def users_new():
    user = {'id': '', 
            'nickname': '', 
            'email': ''}
    return render_template(
        'users/new.html',
        user=user,
        messages=get_flashed_messages(with_categories=True),
    )