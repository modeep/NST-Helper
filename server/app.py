from flask import Flask, request

app = Flask(__name__)

@app.route('/uploadImage', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        f = request.files['file']
        return '

if __name__ == '__main__':
    app.run(debug=True)