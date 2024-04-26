from flask import Flask, request, render_template, make_response, jsonify, redirect
from flask_restful import reqparse, abort, Api, Resource
from data import db_session
from data.users import User
from data.weather_api import Data
from forms.forms import RegisterForm, LoginForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_restful import reqparse, abort, Api, Resource
from pyowm import OWM

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
# login_manager = LoginManager()
# login_manager.init_app(app)



@app.route('/')
@app.route('/index')
def index():
    with open('templates/index.html', 'r', encoding='utf-8') as stream:
        return stream.read()


@app.route('/reg_form', methods=['POST', 'GET'])
def reg_form():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            email=form.email.data,
            country=form.country.data,
            city=form.city.data,
            sex=form.sex.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('register.html', title='Регистрация', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route('/index.html/<home>')
def data_weather(home):
    owm = OWM('a99967bc9ee70d5b4bd387902982f400')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(f'{home}, RU').weather
    temp_dict = observation.temperature('celsius')
    tempreture = int(temp_dict['temp'])
    wind_dict_in_meters_per_sec = observation.wind()
    speed = int(wind_dict_in_meters_per_sec['speed'])
    status = observation.detailed_status
    if 'snow' not in status and 'rain' not in status:
        precipitation = 'нет'
    elif 'snow' in status:
        precipitation = 'снег'
    else:
        precipitation = 'дождь'
    pressure_dict = observation.barometric_pressure(unit='inHg')
    pressure = int(pressure_dict['press'])
    humi = observation.humidity
    sunrise_date = observation.sunrise_time(timeformat='date')
    sunrset_date = observation.sunset_time(timeformat='date')
    sunrise = str(sunrise_date).split()[1].split(':')[0]
    sunrset = str(sunrset_date).split()[1].split(':')[0]
    db_sess = db_session.create_session()
    data = Data(
        tempreture=tempreture,
        speed=speed,
        precipitation=precipitation,
        pressure=pressure,
        humidity=humi,
        home=home
    )
    db_sess.add(data)
    db_sess.commit()
    return render_template('index.html', home=home, tempreture=tempreture, speed=speed,
                           precipitation=precipitation, pressure=pressure, humi=humi)




def main():
    db_session.global_init("db/info.db")
    app.run(host='127.0.0.1', port=8080)


if __name__ == '__main__':
    main()
