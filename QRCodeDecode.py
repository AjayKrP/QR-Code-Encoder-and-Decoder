import qrtools


def get_qr_text(image_name):
    qr = qrtools.QR()
    try:
        qr.decode(image_name)
        print(qr.data)
        return qr.data
    except FileNotFoundError:
        print("File not Found!!!")
