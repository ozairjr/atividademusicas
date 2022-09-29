from typing import List

import musicas.regras.musicas_regras as musicas_regras
from fastapi import APIRouter, status
from musicas.modelos import (ModeloBaseMusica, ModeloCodigoMusica,
                             ModeloGeralMusica)

# Minha rota API de músicas
rota_musicas = APIRouter(
    # Prefixo para o caminho da rota
    prefix="/api/musicas"
)


# Cria nova música
@rota_musicas.post(
    "/",
    # Ajustado o código HTTP de retorno
    status_code=status.HTTP_201_CREATED,
    # Modelo da resposta
    response_model=ModeloCodigoMusica,
)
async def criar_nova_musica(musica: ModeloBaseMusica):
    nova_musica = await musicas_regras.inserir_nova_musica(musica)
    return nova_musica

# Atualiza a música pelo código.
@rota_musicas.put("/{codigo}")
async def atualizar_musica(codigo: str, musica: dict):
    return None


# Remove uma música pelo código
@rota_musicas.delete(
    "/{codigo}",
    # Código HTTP infomando que foi removido
    status_code=status.HTTP_202_ACCEPTED
    )
async def remover_musica(codigo: str):
    await musicas_regras.remover_por_codigo(codigo)


# Pesquisa a música pelo código.
@rota_musicas.get(
    "/{codigo}",
    # Informamos para a pesquisa o modelo da resposta
    response_model=ModeloGeralMusica
)
async def pesquisar_musica_pelo_codigo(codigo: str):
    musica = await musicas_regras.pesquisar_por_codigo(codigo, True)
    return musica


# Pesquisa por todas as músicas (sem um filtro)
@rota_musicas.get(
    "/",
    # E também informamos aqui o modelo da resposta.
    response_model=List[ModeloGeralMusica]
)
async def pesquisar_todas_as_musicas() -> List[ModeloGeralMusica]:
    todas = await musicas_regras.pesquisar_por_todas()
    return todas
