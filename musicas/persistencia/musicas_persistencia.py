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
    # Campo nome da música.
    NOME = "nome"


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


async def pesquisar_pelo_nome(nome: str) -> Optional[dict]:
    # Filtro para a pesquisa
    filtro = {
        CampoMusica.NOME: nome
    }
    # Consultando no banco dados a primeira música
    # que contenha o código informado.
    musica = await COLECAO_MUSICA.find_one(filtro)

    return musica


async def inserir_uma_nova_musica(nova_musica: dict) -> dict:
    # Não validaremos aqui. Mais detalhes veja a
    # sessão do 'Cadastro da nova música no MongoDB'
    # no arquivo README.md
    await COLECAO_MUSICA.insert_one(nova_musica)
    # O registro `nova_musica` recebe o atributo `_id`
    # que é a chave no banco de dados MongoDB.
    return nova_musica


async def remover_uma_musica_pelo_codigo(codigo_musica: str) -> bool:
    # Remove uma música pelo código. SE a música foi removida
    # retornará True.

    # Filtro para a remoção
    filtro = {CampoMusica.CODIGO: codigo_musica}
    # Removendo no banco
    resultado = await COLECAO_MUSICA.delete_one(filtro)
    # E aí, removeu?
    removeu = resultado.deleted_count > 0
    return removeu
