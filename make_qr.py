import qrcode

# Ссылка на твой локальный сайт (берём адрес из твоего терминала)
data = "http://192.168.100.59:5000"

# Настройки внешнего вида QR-кода
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

# Создаем картинку (черный код на белом фоне)
img = qr.make_image(fill_color="black", back_color="white")

# Сохраняем сразу в папку static нашего сайта под именем qr.png
img.save("static/qr.png")
print("QR-код успешно создан и сохранен в static/qr.png!")
