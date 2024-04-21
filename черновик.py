from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/main_page')
def main_page():
    return render_template('ченовик.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)