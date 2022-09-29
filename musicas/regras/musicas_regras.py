"""
Regras e ajustes para músicas.
"""

from typing import List, Optional
from uuid import uuid4

import musicas.persistencia.musicas_persistencia as musicas_persistencia
from musicas.modelos import ModeloBaseMusica, ModeloGeralMusica
from musicas.regras.regras_excecoes import (NaoEncontradoExcecao,
                                            OutroRegistroExcecao)


async def pesquisar_por_codigo(
    codigo: str, lanca_excecao_se_nao_encotrado: bool = False
) -> Optional[dict]:
    musica = await musicas_persistencia.pesquisar_pelo_codigo(codigo)
    if not musica and lanca_excecao_se_nao_encotrado:
        raise NaoEncontradoExcecao("Música não encontrada")
    return musica


async def pesquisar_por_todas() -> List[dict]:
    todas = await musicas_persistencia.pesquisar_todas()
    return todas


async def validar_nova_musica(musica: ModeloBaseMusica):
    # Seria bom validarmos aqui se há nome e artista.
    # Mas como a camada _rest já fez isto para nós, vamos 'confiar'
    # nela.

    # Validando se não há outra música com este nome
    outra_musica = await musicas_persistencia.pesquisar_pelo_nome(musica.nome)
    if outra_musica is not None:
        raise OutroRegistroExcecao("Há outra música com este nome")


async def inserir_nova_musica(musica: ModeloBaseMusica) -> ModeloGeralMusica:
    await validar_nova_musica(musica)

    # 'Convertendo' música para ser salva no banco
    nova_musica = musica.dict()
    # Gerando novo código com uuidv4
    nova_musica[musicas_persistencia.CampoMusica.CODIGO] = str(uuid4())

    # Salvando no banco de dados
    await musicas_persistencia.inserir_uma_nova_musica(nova_musica)

    # Retornando o registro da música completo
    musica_geral = ModeloGeralMusica(**nova_musica)

    return musica_geral
