import pyqrcode
import os


def generate_qr_code(text, id):
    os.chdir('/home/Asus/PycharmProjects/SIH/static/images')
    image = pyqrcode.create(text)
    image.png(id+'.png')
    os.chdir('../')