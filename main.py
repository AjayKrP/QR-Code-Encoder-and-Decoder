from flask import Flask, render_template, request, flash
from form import QRForm
app = Flask(__name__)
app.secret_key = '_________\/R|_|S|-|/\|_i________'


@app.route('/', methods=["GET", "POST"])
def home_page():
    if request.method == 'GET':
        return render_template('home.html')

@app.route('/generate', methods=['GET', 'POST'])
def contact():
    form = QRForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash("All fields are required!!!")
            return render_template('form.html', form = form)
        else:
            render_template('success.html')
    elif request.method == 'GET':
        return render_template('form.html', form = form)


if __name__ == '__main__':
    app.run(debug=True)


