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
    nome = ''
    raca = ''
    classe = ''
    valores_rolados = []
    bloquear_campos = False
    personagem_criado = None

    if request.method == 'POST':
        acao = request.form.get('acao')
        nome = request.form.get('nome')
        estilo = request.form.get('estilo')
        raca = request.form.get('raca')
        classe = request.form.get('classe')

        if acao == 'definir':
            if estilo == 'classico':
                valores_rolados = ClassicoController().rolar_dados()
            elif estilo == 'aventureiro':
                valores_rolados = AventureiroController().rolar_dados()
            elif estilo == 'heroico':
                valores_rolados = HeroicoController().rolar_dados()
            bloquear_campos = True

        elif acao == 'criar':
            atributos = {}
            if estilo == 'classico':
                atributos = ClassicoController().rolar_dados()
            else:
                nomes = ['forca', 'destreza', 'constituicao', 'inteligencia', 'sabedoria', 'carisma']
                for nome_atributo in nomes:
                    atributos[nome_atributo] = request.form.get(nome_atributo)

            personagem_criado = {
                'nome': nome,
                'estilo': estilo,
                'raca': raca,
                'classe': classe,
                'atributos': atributos
            }

    return render_template('criacao_personagem.html', estilo=estilo, nome=nome, raca=raca, classe=classe,
            valores_rolados=valores_rolados, bloquear_campos=bloquear_campos, personagem_criado=personagem_criado
)

if __name__ == '__main__':
    app.run(debug=True)