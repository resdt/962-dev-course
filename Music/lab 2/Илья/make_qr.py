import qrcode

def generate_qr(data, filename):
    """Генерирует QR-код и сохраняет его в файл."""
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)

    print(f"QR-код сохранён в файл {filename}")

if __name__ == "__main__":
    text = input("Введите текст или ссылку для QR-кода: ")
    filename = input("Введите название QR-кода: ")+".png"
    generate_qr(text,filename if filename!=".png" else 'qrcode.png')

