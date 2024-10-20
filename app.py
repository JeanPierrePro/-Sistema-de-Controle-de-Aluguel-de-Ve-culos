from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista em memória para armazenar os carros (simulando um "banco de dados")
carros = [
    {'id': 1, 'modelo': 'Fiat Uno', 'ano': 2019, 'disponivel': True},
    {'id': 2, 'modelo': 'Chevrolet Onix', 'ano': 2020, 'disponivel': True},
    {'id': 3, 'modelo': 'Volkswagen Gol', 'ano': 2018, 'disponivel': True},
]

# Rota principal que lista os carros
@app.route('/')
def index():
    return render_template('index.html', carros=carros)

# Rota para alugar um carro
@app.route('/alugar/<int:carro_id>', methods=['POST'])
def alugar_carro(carro_id):
    for carro in carros:
        if carro['id'] == carro_id and carro['disponivel']:
            carro['disponivel'] = False  # Aluga o carro, alterando sua disponibilidade
            break
    return redirect(url_for('index'))

# Rota para devolver o carro
@app.route('/devolver/<int:carro_id>', methods=['POST'])
def devolver_carro(carro_id):
    for carro in carros:
        if carro['id'] == carro_id and not carro['disponivel']:
            carro['disponivel'] = True  # Devolve o carro, tornando-o disponível
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
