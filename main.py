from flask import Flask, render_template, request, flash
from QRGenerate import generate_qr_code
import time
app = Flask(__name__)
app.secret_key = '_________\/R|_|S|-|/\|_i________'


@app.route('/', methods=["GET", "POST"])
def home_page():
    if request.method == 'GET':
        return render_template('home.html')


@app.route('/generate', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        id = str(int(time.time()))
        generate_qr_code(request.form['text'], id)
        return render_template('success.html', image_name=id+'.png')
    elif request.method == 'GET':
        return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)


