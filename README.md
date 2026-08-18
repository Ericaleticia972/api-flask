

# API Flask

API REST desenvolvida em Python utilizando o framework Flask.

## Sobre o projeto

Este projeto foi desenvolvido para praticar a criação de APIs REST com Flask, trabalhando com requisições HTTP e armazenamento de dados em um arquivo JSON.

A API permite cadastrar, listar, editar e excluir contatos.

## Funcionalidades

- Listar contatos
- Adicionar novos contatos
- Editar contatos existentes
- Excluir contatos
- Armazenar dados em arquivo JSON

## Tecnologias utilizadas

- Python
- Flask
- JSON
- Git
- GitHub

## Rotas

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | / | Exibe uma mensagem inicial |
| GET | /sobre | Exibe informações sobre a API |
| GET | /contatos | Lista todos os contatos |
| POST | /contatos | Adiciona um novo contato |
| PUT | /contatos/<id> | Edita um contato |
| DELETE | /contatos/<id> | Exclui um contato |

## Como executar

Clone o repositório:

git clone https://github.com/Ericaleticia972/api-flask.git

Entre na pasta do projeto:

cd api-flask

Crie um ambiente virtual:

python -m venv venv

Ative o ambiente virtual no Windows:

venv\Scripts\activate

Instale o Flask:

pip install flask

Execute a aplicação:

python app.py

A API estará disponível em:

http://127.0.0.1:5000

## Aprendizados

Durante o desenvolvimento deste projeto foram praticados:

- Criação de APIs REST
- Rotas e métodos HTTP
- Requisições GET, POST, PUT e DELETE
- Manipulação de dados JSON
- Armazenamento de informações em arquivos
- Organização de código Python
- Uso do Git e GitHub

## Autora

Érica Silva
