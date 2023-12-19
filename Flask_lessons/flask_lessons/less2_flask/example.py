from flask import Flask, request, render_template, redirect, url_for, session, flash, jsonify


users = [
    'mike',
    'mishel',
    'adel',
    'keks',
    'kamila'
]


# создаем экз класса Flask и передаем в него имя модуля
app = Flask(__name__) 


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


@app.get('/users')
def get_users():
    # term = request.args.get('term')
    # res = [user for user in users if term in user]
    return render_template(
        '/users/index.html',
        # search=res,
        # term=term,
        )