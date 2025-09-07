from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/criacao-personagem')
def criacao_personagem():
    return render_template('criacao_personagem.html')

if __name__ == '__main__':
    app.run(debug=True)