from flask import Flask, request, render_template

app = Flask(__name__)


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
    return render_template('main_page.html')


@app.route('/reg_form', methods=['POST', 'GET'])
def reg_form():
    if request.method == 'GET':
        return render_template('reg_form.html')
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
