from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def start():
    return "Миссия Колонизация Марса";


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/image_mars")
def promotion():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
          integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <meta charset="UTF-8">
    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
    <title>Привет, Марс!</title>
</head>
<body>
<div class="main-block">
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='images/MARS.png')}">
</div>
</body>
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
</html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
