from flask import Flask
import random, webbrowser

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

html_file = open("web-caesar.html", "r")
html_list = html_file.readlines()
html_file.close()
form = """<!DOCTYPE html>
<html lang="en">

<head>
    <link rel="stylesheet" href="style.css">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Web Caesar</title>
</head>

<body>
    <header>
        <h1>Web Caesar</h1>
    </header>
    <main></main>
    <footer></footer>
</body>

</html>"""

@app.route("/")

def form_html():
    html = ""
    for string in html_list:
        html += string
    return html

def index():
    wc_html = form_html()
    return wc_html


app.run()