from flask import Flask, url_for, request, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/index/<name>')
def index(name):
    return render_template('base.html', title=name)


@app.route('/training/<prof>')
def training(prof):
    return render_template('base.html', proffesion=prof)


@app.route('/list_prof/<list>')
def spisok(list):
    return render_template('base.html', how=list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
