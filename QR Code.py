import qrcode
url = input("Enter The URl: " ).strip()
file_path ="C:\\Users\\admin\\Desktop\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()

img.save(file_path)

print("QR code generated")