import os, caesar
from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)

@app.route('/favicon.ico')

def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/', methods=["GET", "POST"])

def index():
   return render_template("web-caesar.html")


if __name__ == '__main__':
    app.run(debug = True)