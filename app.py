from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {"id": 1, "titulo": "Engenharia de Software Moderna", "autor": "Valente"},
    {"id": 2, "titulo": "Clean Architecture", "autor": "Robert C. Martin"}
]

@app.route('/')
def hello_world():
    return 'API da Livraria Mackenzie Rodando na Nuvem!'

@app.route('/api/livros', methods=['GET', 'POST'])
def gerenciar_livros():
    if request.method == 'GET':
        return jsonify({"livros": livros}), 200

    elif request.method == 'POST':
        novo_livro = request.get_json()
        novo_livro["id"] = len(livros) + 1
        livros.append(novo_livro)
        return jsonify({"mensagem": "Livro adicionado com sucesso!", "livro": novo_livro}), 201

@app.route('/api/livros/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def gerenciar_livro_unico(id):
    livro = next((l for l in livros if l["id"] == id), None)

    if not livro:
        return jsonify({"erro": "Livro não encontrado"}), 404

    if request.method == 'GET':
        return jsonify(livro), 200

    elif request.method == 'PUT':
        dados_atualizados = request.get_json()
        livro.update(dados_atualizados)
        return jsonify({"mensagem": "Livro atualizado com sucesso!", "livro": livro}), 200

    elif request.method == 'DELETE':
        livros.remove(livro)
        return jsonify({"mensagem": "Livro removido com sucesso!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)