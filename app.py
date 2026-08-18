from flask import Flask, request
import json

app = Flask(__name__)


def carregar_contatos():
    with open("contatos.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_contatos(contatos):
    with open("contatos.json", "w", encoding="utf-8") as arquivo:
        json.dump(contatos, arquivo, indent=4, ensure_ascii=False)


@app.route("/")
def inicio():
    return "Minha primeira API com Flask!"


@app.route("/sobre")
def sobre():
    return {
        "projeto": "Minha API Flask",
        "linguagem": "Python",
        "framework": "Flask"
    }


@app.route("/contatos")
def contatos():
    return carregar_contatos()


@app.route("/contatos", methods=["POST"])
def adicionar_contato():
    dados = request.json
    contatos = carregar_contatos()

    dados["id"] = len(contatos) + 1
    contatos.append(dados)
    salvar_contatos(contatos)

    return {
        "mensagem": "Contato adicionado com sucesso!",
        "contato": dados
    }


@app.route("/contatos/<int:id>", methods=["DELETE"])
def excluir_contato(id):
    contatos = carregar_contatos()

    contato_encontrado = None

    for contato in contatos:
        if contato["id"] == id:
            contato_encontrado = contato
            break

    if contato_encontrado:
        contatos.remove(contato_encontrado)
        salvar_contatos(contatos)

        return {
            "mensagem": "Contato excluído com sucesso!",
            "contato": contato_encontrado
        }

    return {
        "mensagem": "Contato não encontrado!"
    }, 404


@app.route("/contatos/<int:id>", methods=["PUT"])
def editar_contato(id):
    contatos = carregar_contatos()
    dados = request.json

    for contato in contatos:
        if contato["id"] == id:
            contato["nome"] = dados["nome"]
            contato["email"] = dados["email"]

            salvar_contatos(contatos)

            return {
                "mensagem": "Contato atualizado com sucesso!",
                "contato": contato
            }

    return {
        "mensagem": "Contato não encontrado!"
    }, 404


if __name__ == "__main__":
    app.run(debug=True)