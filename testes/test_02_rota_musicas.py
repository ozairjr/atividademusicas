"""
Testes com API de músicas (incompleto!)
"""

from typing import Any

import pytest
import pytest_asyncio
from fastapi import status
from fastapi.testclient import TestClient
from musicas.aplicacao import app
from musicas.persistencia.musicas_persistencia import (COLECAO_MUSICA,
                                                       CampoMusica)
from musicas.rest.musicas_rest import rota_musicas

# Cliente da API do FastAPI.
cliente_app = TestClient(app)

# Prefixo de música
PREFIXO_URL = rota_musicas.prefix


# -----------------------------------------------
# Podemos colocar os prefixos em outros arquivos.
# Deixamos aqui somente para 'centralizar' o estudo.
#
# O teste será 'integrado', ou seja, iremos gravar
# e consultar no banco de dados.
#
# Por isso, em geral, antes de cada teste precisamos
# deixar o banco 'limpo' para que um teste não 'suje'
# outro. Vamos usar as 'fixtures' do pytest.
#
# https://docs.pytest.org/en/7.1.x/explanation/fixtures.html


# Fixture assíncrono já que o Motor é assíncrono
@pytest_asyncio.fixture
async def limpa_musicas():
    # Limparando a base de dados
    await COLECAO_MUSICA.delete_many({})

    return None


@pytest_asyncio.fixture
async def musica_nome01(
    # Limpando o banco
    limpa_musicas
):
    assert limpa_musicas is None

    # Música para ser inserida no banco
    musica = {
        CampoMusica.NOME: "nome01",
        CampoMusica.CODIGO: "codigo01",
        "artista": "ninguem",
    }
    # Inserindo no banco de dados
    await COLECAO_MUSICA.insert_one(musica)

    # Devolvendo para saber o nome depois
    return musica

# ---------------------------------------------------
# Nossos testes
# ---------------------------------------------------


@pytest.mark.asyncio
# Teste 'marcado' como assíncrono por que `conta_musicas` é
# assíncrono
async def test_deveria_cadastrar_uma_nova_musica_corretamente(
    # 'Chamando' o context/fixture (um fixture usando outro)
    limpa_musicas
):
    # Somente 'validando' para que o 'parâmetro' não fique solto
    assert limpa_musicas is None

    # Novo registro de música
    musica = {
        CampoMusica.NOME: "nome01",
        "artista": "artista",
        "tempo": 10,
    }
    # Chamando a API para cadastrar
    resposta = cliente_app.post(PREFIXO_URL + "/", json=musica)
    # Deu certo?
    assert resposta.status_code == status.HTTP_201_CREATED
    # Vamos validar a resposta
    registro_codigo = resposta.json()
    # Há código na resposta?
    assert CampoMusica.CODIGO in registro_codigo
    # O código...
    codigo = registro_codigo[CampoMusica.CODIGO]
    # existe?
    assert codigo is not None

    # Foi gravado mesmo no banco? (Na verdade, deveríamos
    # consultar no banco)
    resposta = cliente_app.get(f"{PREFIXO_URL}/{codigo}")
    # Deu certo?
    assert resposta.status_code == status.HTTP_200_OK
    # Vamos validar a resposta
    musica_consultada = resposta.json()
    # Há código na resposta?
    assert CampoMusica.CODIGO in musica_consultada

    # Notaram alguma repetição de código acima?

    # Gravou sem mudar?
    musica_base = dict(**musica_consultada)
    musica_base.pop(CampoMusica.CODIGO, None)
    assert musica == musica_base


def test_nao_deveria_cadastrar_uma_musica_sem_nome():
    # Novo registro de música
    musica = {
        "artista": "artista",
        "tempo": 10,
    }
    # Chamando a API para cadastrar
    resposta = cliente_app.post(f"{PREFIXO_URL}/", json=musica)
    # E aí, há problema na requisição?
    assert resposta.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    # Sabe de mais algum teste que poderíamos fazer?


@pytest.mark.asyncio
async def test_nao_deveria_inserir_musica_com_mesmo_nome(musica_nome01: dict):
    assert musica_nome01 is not None

    nova_musica = {
        CampoMusica.NOME: musica_nome01[CampoMusica.NOME],
        "artista": "Mais um artista"
    }

    # Chamando a API para cadastrar
    resposta = cliente_app.post(f"{PREFIXO_URL}/", json=nova_musica)
    # E aí, há outra música com o mesmo nome?
    assert resposta.status_code == status.HTTP_409_CONFLICT

    # Precisamos validar mais alguma coisa?
