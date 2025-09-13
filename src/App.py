from flask import Flask, render_template, request

from controllers.AventureiroController import AventureiroController
from controllers.ClassicoController import ClassicoController
from controllers.HeroicoController import HeroicoController
from models.racas.Humano import Humano
from models.racas.Elfo import Elfo
from models.racas.Meio_Elfo import Meio_Elfo
from models.racas.Anao import Anao
from models.racas.Gnomo import Gnomo
from models.racas.Halfling import Halfling

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

            # Instanciar a raça
            raca_obj = None
            if raca == 'humano':
                raca_obj = Humano()
            elif raca == 'elfo':
                raca_obj = Elfo()
            elif raca == 'meio-elfo':
                raca_obj = Meio_Elfo()
            elif raca == 'anao':
                raca_obj = Anao()
            elif raca == 'gnomo':
                raca_obj = Gnomo()
            elif raca == 'halfling':
                raca_obj = Halfling()

            personagem_criado = {
                'nome': nome,
                'estilo': estilo,
                'raca': raca,
                'classe': classe,
                'atributos': atributos,
                'habilidades': raca_obj.habilidades if raca_obj else []
            }


    return render_template('criacao_personagem.html', estilo=estilo, nome=nome, raca=raca, classe=classe,
            valores_rolados=valores_rolados, bloquear_campos=bloquear_campos, personagem_criado=personagem_criado
)

if __name__ == '__main__':
    app.run(debug=True)