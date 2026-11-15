from flask import Flask, render_template

app = Flask(__name__)

# Маршрут для отображения главной страницы твоего новогоднего лендинга
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Запуск сервера на порту 5000, открытом для внешнего мира
    app.run(debug=True, host='0.0.0.0', port=5000)
