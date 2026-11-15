from flask import Flask, render_template
import os
import qrcode

app = Flask(__name__)

# Путь внутри сервера, куда автоматически сохранится вечный QR-код
QR_PATH = os.path.join('static', 'qr.png')
# Твой точный и неизменяемый адрес сайта в облаке
SITE_URL = "https://onrender.com"

def generate_static_qr():
    print("Скрипт проверяет и генерирует постоянный QR-код...")
    try:
        # Всегда создаем папку static, если её вдруг нет
        os.makedirs('static', exist_ok=True)
        
        # Создаем и настраиваем QR-код под твой домен
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(SITE_URL)
        qr.make(fit=True)
        
        # Сохраняем картинку прямо в проект под именем qr.png
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(QR_PATH)
        print("Постоянный QR-код успешно создан и сохранен в static/qr.png!")
    except Exception as e:
        print(f"Не удалось сгенерировать QR-код: {e}")

# Запускаем генерацию железного QR-кода прямо при старте удаленного сервера
generate_static_qr()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
