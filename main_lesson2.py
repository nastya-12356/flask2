from flask import Flask, url_for, request, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
answers = {
    'title': 'Анкета',
    'surname': 'Watny',
    'name': 'Mark',
    'education': 'выше среднего',
    'profession': 'штурман марсохода',
    'sex': 'male',
    'motivation': 'Всегда мечтал застрять на Марсе!',
    'ready': 'True'
}


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    param = {}
    param['title'] = title
    return render_template('index.html', **param)


@app.route('/training/<prof>')
def training(prof):
    param = {}
    param['profession'] = prof
    return render_template('index.html', **param)


@app.route('/list_prof/<listing>')
def spisok(listing):
    param = {}
    param['how'] = listing
    return render_template('prof_listing.html', **param)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    return render_template('auto_answer.html', **answers)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        print(request.form['id_astronaut'], '')
        print(request.form['password_astronaut'], '')
        print(request.form['id_captain'], '')
        print(request.form['password_captain'], '')

        return "Доступ разрешен"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
