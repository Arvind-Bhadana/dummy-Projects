from asyncio import constants
from ensurepip import version
from textwrap import fill
import qrcode


qr_scanner= qrcode.QRCode(version=1,
error_correction = qrcode.constants.ERROR_CORRECT_H,
box_size=10,
border=4)
qr_scanner.add_data("https://www.google.com")
qr_scanner.make(fit=True)
qr_image = qr_scanner.make_image(fill_color='cyan',back_color ='black')
qr_image.save('qr_image.png')