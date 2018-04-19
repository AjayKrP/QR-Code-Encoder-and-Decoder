import pyqrcode
import os


def generate_qr_code(text, id):
    path = os.getcwd()
    print(path)
    os.chdir(path+'/static/images')
    image = pyqrcode.create(text)
    image.png(id+'.png', scale=10*2)
    os.chdir('../')