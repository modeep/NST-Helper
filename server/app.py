import os

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/uploadImage', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        b, s = request.files['base'], request.files['style']
        b_filename = os.path.join('base/', b.filename)
        s_filename = os.path.join('style/', s.filename)
        b.save(os.path.join('./static/', b_filename))
        s.save(os.path.join('./static/', s_filename))
        return render_template('uploaded.html', b_filename=b_filename, s_filename=s_filename)


@app.route('/start', methods=['GET'])
def start():
    pass


if __name__ == '__main__':
    app.run(debug=True)