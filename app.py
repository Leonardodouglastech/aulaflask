from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_word():
    return ('<form>      '
            '<label> Primeiro Nome: </label>'
            '<input type="text"><br><br>'
            '<label> Segundo Nome: </label>'
            '<input type="text"><br><br>'
            '<input type="submit" value="Enviar">'
            '</form>')