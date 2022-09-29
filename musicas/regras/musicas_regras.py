"""
Regras e ajustes para músicas.
"""

from typing import List, Optional
from uuid import uuid4

import musicas.persistencia.musicas_persistencia as musicas_persistencia
from musicas.modelos import ModeloBaseMusica, ModeloGeralMusica
from musicas.regras.regras_excecoes import (CodigosDiferentesExcecao, NaoEncontradoExcecao,
                                            OutroRegistroExcecao)

# Campo código
CAMPO_CODIGO = musicas_persistencia.CampoMusica.CODIGO


async def pesquisar_por_codigo(
    codigo: str, lanca_excecao_se_nao_encontrado: bool = False
) -> Optional[dict]:
    # Pesquisando pelo código no banco
    musica = await musicas_persistencia.pesquisar_pelo_codigo(codigo)
    # Não encontrei, devo lançar exceção?
    if not musica and lanca_excecao_se_nao_encontrado:
        raise NaoEncontradoExcecao("Música não encontrada")
    # Retornando o registro do banco.
    return musica


async def pesquisar_por_todas() -> List[dict]:
    # Pesquisando todas as músicas.
    todas = await musicas_persistencia.pesquisar_todas()
    return todas


async def validar_musica(musica: ModeloBaseMusica, codigo_base: Optional[str] = None):
    # Validador de música.
    # Se codigo_base for informado, entendemos que é uma atualização.
    # Se codigo_base não for informado, é um processo de criação.
    # Esse parâmetro será utilizado para na validação se há outra
    # música com o mesm nome.
    eh_musica_nova = codigo_base is None

    # Mais uma vez: Seria bom validarmos aqui se há nome e artista.
    # Mas como a camada _rest já fez isto para nós, vamos 'confiar'
    # nela.

    # Validando se não há outra música com este nome
    outra_musica = await musicas_persistencia.pesquisar_pelo_nome(musica.nome)
    if (outra_musica is not None) and (
        # Se (é nova música) ou ...
        eh_musica_nova or
        #  (código encontrado é diferente do informado),
        (codigo_base != outra_musica[CAMPO_CODIGO])
    ):
        # Então temos uma repetição de nome.
        raise OutroRegistroExcecao("Há outra música com este nome")


async def inserir_nova_musica(musica: ModeloBaseMusica) -> ModeloGeralMusica:
    # Validando sem codigo, já que é música nova.
    await validar_musica(musica)

    # 'Convertendo' música para ser salva no banco
    nova_musica = musica.dict()
    # Gerando novo código com uuidv4
    nova_musica[musicas_persistencia.CampoMusica.CODIGO] = str(uuid4())

    # Salvando no banco de dados
    await musicas_persistencia.inserir_uma_nova_musica(nova_musica)

    # Retornando o registro da música completo
    musica_geral = ModeloGeralMusica(**nova_musica)

    return musica_geral


async def remover_por_codigo(codigo: str):
    # Removendo no banco e a regra de verificar
    # se existe, vamos ver aqui no retorno
    removeu = await musicas_persistencia.remover_uma_musica_pelo_codigo(codigo)

    # "Validando" se removeu (encontrou e removeu?)
    if not removeu:
        raise NaoEncontradoExcecao("Música não encontrada")


async def atualizar_por_codigo(codigo: str, musica: ModeloGeralMusica):
    # Pesquisando a música para atualizar
    # Se não existe, iremos lançar exceção.
    await pesquisar_por_codigo(codigo, True)

    # Se foi informado o código, vamos ver se não são diferentes
    if musica.codigo is not None and musica.codigo != codigo:
        # Sim na linha de abaixo não esquecemos dos parêntesis.
        # Por quê?
        raise CodigosDiferentesExcecao

    # Validando, com código; para identificar que é uma atualização
    validar_musica(musica, codigo)

    musica_para_banco = musica.dict()
    # Pequeno ajuste, se o código não existe, devemos retirá-lo
    if musica.codigo is None:
        musica_para_banco.pop(CAMPO_CODIGO, None)

    # Atualizando no banco de dado
    await musicas_persistencia.atualizar_uma_musica_pelo_codigo(
        codigo, musica_para_banco
    )
