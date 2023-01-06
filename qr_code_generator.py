import qrcode as qr
from PIL import Image

qr_object = qr.QRCode(version=1,
                    error_correction= qr.ERROR_CORRECT_H,
                    box_size= 10, border= 4,
                    )
qr_object.add_data("https://www.linkedin.com/in/manjeet-kumar-09236b58/")
qr_object.make(fit= True)
img = qr_object.make_image(fill_color = 'red', back_color = 'blue')
img.save("./outputs/linkedin profile QR.png")

# Simple code below can also be used
# qr_data = qr.make("https://www.linkedin.com/in/manjeet-kumar-09236b58/")
# qr_data.save("./outputs/linkedin profile QR.png")