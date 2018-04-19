import pyqrcode
import os


def generate_qr_code(text, id):
    path = os.getcwd()
    os.chdir(path + '/images')
    image = pyqrcode.create(text)
    image.png(id+'.png')
    os.chdir('../')