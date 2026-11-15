from flask import Flask, render_template, send_from_directory
import os
import urllib.request

app = Flask(__name__)

# Путь внутри удаленного сервера, куда скрипт скачает файл
APK_PATH = os.path.join('static', 'app.apk')

# Ссылка на твой Google Диск, откуда скрипт сам заберет файл в фоне
GOOGLE_DRIVE_URL = "https://drive.google.com/file/d/1q8A1WPQsWkzN4unw93e-ZHs21ezJ7HnP/view?usp=sharing"

def download_apk_from_drive():
    # Если файла еще нет на сервере Render, скачиваем его
    if not os.path.exists(APK_PATH):
        print("Скрипт запускает фоновое скачивание APK (50 МБ) с Google Диска...")
        try:
            os.makedirs('static', exist_ok=True)
            urllib.request.urlretrieve(GOOGLE_DRIVE_URL, APK_PATH)
            print("Файл успешно сохранен в память сервера Render!")
        except Exception as e:
            print(f"Ошибка при скачивании файла скриптом: {e}")

# Скрипт скачивает файл сразу при старте удаленного сервера
download_apk_from_drive()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def download_file():
    # Отдаем скачанный скриптом файл напрямую в один клик без переходов
    return send_from_directory('static', 'app.apk', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
