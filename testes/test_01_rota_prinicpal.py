"""
Testes com API principal.
"""

from fastapi import status
from fastapi.testclient import TestClient
from musicas.aplicacao import app

# Cliente da API do FastAPI.
cliente_app = TestClient(app)


def test_deveria_receber_um_oi():
    # Para o `pytest`, escolhemos o prefixo `test`.
    # Com o nome da função já explicamos rapidamente
    # o que o teste deveria realizar por nós.

    # 'Chamando' a rota principal.
    resposta = cliente_app.get("/")
    # Temos resposta ?
    assert resposta
    # É o código HTTP esperado?
    assert resposta.status_code == status.HTTP_200_OK
    # E o corpo da mensagem é um json com um Oi ?
    assert resposta.json() == "Oi"
