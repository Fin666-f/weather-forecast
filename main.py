from flask import Flask, request, render_template

icons = ["bi bi-cloud-snow-fill", "bi bi-cloud-drizzle-fill", "bi bi-cloud-fog-fill", "bi bi-cloud-lightning-rain-fill",
         "bi bi-cloud-moon-fill", "bi bi-cloud-sun-fill", "bi bi-sun-fill", "bi bi-moon-fill", "bi bi-snow3", "bi bi-sun-fill"]
icons_day = []
icon_paths = []
app = Flask(__name__)


def icons_day():
    global icons
    global icons_day
    for i in icons:
        icons_day.append(i)

def icons_week():
    pass

def temps_day():
    pass

def temps_week():
    pass

@app.route('/')
@app.route('/index')
def index():
    with open('templates/index.html', 'r', encoding='utf-8') as stream:
        return stream.read()


@app.route('/t')
def t():
    with open('t.html', 'r', encoding='utf-8') as stream:
        return stream.read()

@app.route('/main_page')
def main_page():
    temp_day = 50
    temps_day = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]#temps_day()
    temps_week = [0, 1, 2, 3, 4, 5, 6]#temps_week()
    home = 'Москва'
    humidity = 60
    rainfall = 0
    speed = 20
    return render_template('main_page.html', temps_day=temps_day,
                           temp_day=temp_day, home=home, humidity=humidity, rainfall=rainfall, speed=speed,
                           icons_day=icons_day, temps_week=temps_week)


@app.route('/reg_form', methods=['POST', 'GET'])
def reg_form():
    if request.method == 'GET':
        return render_template('reg_form.html')
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['name'])
        print(request.form['surname'])
        print(request.form['country'])
        print(request.form['home'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
