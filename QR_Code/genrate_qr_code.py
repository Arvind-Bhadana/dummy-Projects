import qrcode  
import PIL
# generating a QR code using the make() function  
qr_img = qrcode.make("https://www.google.com")  
# saving the image file  
qr_img.save("qr-img.jpg")  