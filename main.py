from flask import Flask, render_template, request, redirect
from QRGenerate import generate_qr_code
from SendImage import send_mail
import time
app = Flask(__name__)
app.secret_key = 'mysteries world full of f**kers'


@app.route('/', methods=["GET", "POST"])
def home_page():
    if request.method == 'GET':
        return render_template('home.html')


@app.route('/send_image', methods=['GET', 'POST'])
def sendImage():
    if request.method == 'GET':
         email = request.args.get('email')
         print(email)
         image_name = request.args.get('image_name')
         send_mail(image_name, email)
         return redirect('/generate')


@app.route('/generate', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        id = str(int(time.time()))
        generate_qr_code(request.form['text'], id)
        path = '/static/images/'+id+'.png'
        return render_template('success.html', image_name=path)
    elif request.method == 'GET':
        return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)


