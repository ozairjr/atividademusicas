"""
Módulo responsável pela persistência das músicas.
Este conversa com Mongo para inserir, atualizar, remover
e pesquisar as músicas no MongoDB.
"""

from typing import List, Optional

from .persistencia_bd import obter_colecao

class CampoMusica:
    # Campo código da música.
    CODIGO = "codigo"


# Deixando o meu 'recurso de conversa' com coleção global.
COLECAO_MUSICA = obter_colecao("musica")


async def pesquisar_pelo_codigo(codigo_musica: str) -> Optional[dict]:
    # Filtro para a pesquisa
    filtro = {
        CampoMusica.CODIGO: codigo_musica
    }
    # Consultando no banco dados a primeira música
    # que contenha o código informado.
    musica = await COLECAO_MUSICA.find_one(filtro)

    return musica

async def pesquisar_todas() -> List[dict]:
    # Filtro vazio, desejo todas as músicas
    filtro = {}
    # Obtendo um 'cursor' para varrer todas as músicas
    cursor_pesquisa = COLECAO_MUSICA.find(filtro)
    # Varrendo todas as músicas e 'colocando-as' 
    # dentro de uma lista.
    lista_todas = [
        musica
        async for musica in cursor_pesquisa
    ]

    return lista_todas
