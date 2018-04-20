import qrtools


def get_qr_text(image_name):
    qr = qrtools.QR()
    qr.decode(image_name)
    print(qr.data)
    return qr.data
