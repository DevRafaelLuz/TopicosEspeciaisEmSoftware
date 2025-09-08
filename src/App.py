from flask import Flask, render_template, request

from controllers.AventureiroController import AventureiroController
from controllers.ClassicoController import ClassicoController
from controllers.HeroicoController import HeroicoController

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/criacao-personagem', methods=['GET', 'POST'])
def criacao_personagem():
    estilo = ''
    valores_rolados = []
    bloquear_campos = False

    if request.method == 'POST':
        estilo = request.form.get('estilo', '').lower()

        if estilo == "classico":
            valores_rolados = ClassicoController().rolar_dados()
            bloquear_campos = True
        elif estilo == 'aventureiro':
            valores_rolados = AventureiroController().rolar_dados()
            bloquear_campos = True
        elif estilo == 'heroico':
            valores_rolados = HeroicoController().rolar_dados()
            bloquear_campos = True

    return render_template('criacao_personagem.html', estilo=estilo, valores_rolados=valores_rolados, 
                           bloquear_campos=bloquear_campos)


if __name__ == '__main__':
    app.run(debug=True)