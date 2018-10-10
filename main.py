import os, caesar
from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)

@app.route('/favicon.ico')

def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/', methods=["GET", "POST"])

def index():
    error = "Oops... something went wrong..."
    if request.method == "POST":
        rot = int(request.form["rot"])
        msg = request.form["msg"]
        cipher_msg = caesar.rotate_string(msg, rot)
        return render_template("web-caesar.html", rotation=rot, user_message=cipher_msg)
    else:
        return render_template("web-caesar.html", rotation=0, user_message="")

    return error
    

if __name__ == '__main__':
    app.run(debug = True)