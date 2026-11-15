from flask import Flask, render_template, send_from_directory, request, jsonify

app = Flask(__name__)

# Хранилище текущего состояния гирлянды (по умолчанию: режим 0, белый цвет, макс. яркость)
led_state = {
    "mode": 0,
    "r": 255,
    "g": 255,
    "b": 255,
    "brightness": 255
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def download_file():
    return send_from_directory('static', 'app.apk', as_attachment=True)

# --- API ДЛЯ СВЯЗИ С UNITY И ESP32 ---

# Скрипт Unity отправляет сюда новые настройки при нажатии кнопок
@app.route('/api/set_state', methods=['POST'])
def set_state():
    global led_state
    data = request.get_json()
    
    if not data:
        return jsonify({"status": "error", "message": "No data received"}), 400
        
    # Обновляем только те параметры, которые пришли
    for key in led_state:
        if key in data:
            led_state[key] = int(data[key])
            
    return jsonify({"status": "success", "current_state": led_state})

# Плата ESP32 постоянно опрашивает этот адрес, чтобы узнать, что включить
@app.route('/api/get_state', methods=['GET'])
def get_state():
    return jsonify(led_state)

if __name__ == '__main__':
    # Запуск на порту 5000, доступном во всей Wi-Fi сети
    app.run(debug=True, host='0.0.0.0', port=5000)
