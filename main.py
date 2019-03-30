from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/" method="POST">
            <label for"rot">Rotate by:</label>
            <input type="text" name="rot">
            <br>
            <textarea name="text"></textarea>
            <br>
            <input type="submit">
        </form>
    </body>
</html>

"""

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form.get('rot'))
    text = str(request.form.get('text'))
    final_string = rotate_string(text, rot)
    return '<h1>' + final_string + '</h1>'


@app.route("/")
def index():
    return form

app.run()