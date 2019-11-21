from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/create/', methods=['GET', 'POST'])
def create():
    return render_template('create.html')


@app.route('/gallery/', methods=['GET', 'POST'])
def gallery():
    return render_template('gallery.html')


if __name__ == '__main__':
    app.run(debug=True)
