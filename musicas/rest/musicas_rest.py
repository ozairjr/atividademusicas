from typing import List

from pydantic import BaseModel, Field

import musicas.regras.musicas_regras as musicas_regras
from fastapi import APIRouter, status
from musicas.modelos import (ModeloAtualizaMusica, ModeloBaseMusica,
                             ModeloCodigoMusica, ModeloGeralMusica)

# Minha rota API de músicas
rota_musicas = APIRouter(
    # Prefixo para o caminho da rota
    prefix="/api/musicas",
    # Rótulos/tags
    tags=["Músicas"],
)

# Não seria melhor colocar em um arquivo??
DESCRICAO_CRIACAO_MUSICA = """
Criação de uma nova música. Para registrar uma nova música:

- `nome`: Deve ter nome único.
- `artista`: Deve ter uma pessoa artista.
- `tempo`: Opcionalmente pode ter um tempo. Se informado deve ser
maior que 0 (zero).

Se a música for criada corretamente a API retornará sucesso
(código HTTP 201) e no corpo da resposta um registro com o campo
`codigo`, que é o código da nova música em nosso sistema.
"""

# Colocamos este modelo aqui, SOMENTE para ficar perto da documentação.
# Seria apropriado criar um 'modelo' para cada erro??

class ModeloHaOutraMusica(BaseModel):
    """
    Outra música possui o mesmo nome que a música corrente.
    """
    mensagem: str = Field(
        ...,
        description="Mensagem com a causa do problema")

    class Config:
        schema_extra = {
            "example": {
                "mensagem": "Há outra música com este nome",
            }
        }


@rota_musicas.post(
    "/",
    # 'Título'
    summary="Criação de nova música",
    description=DESCRICAO_CRIACAO_MUSICA,
    # Ajustado o código HTTP de retorno
    status_code=status.HTTP_201_CREATED,
    # Modelo da resposta
    response_model=ModeloCodigoMusica,
    # Extra
    responses={
        status.HTTP_409_CONFLICT: {
            "description": "Já temos outra música com este nome.",
            "model": ModeloHaOutraMusica
        }
    },
)
async def criar_nova_musica(musica: ModeloBaseMusica):
    # Cria nova música
    nova_musica = await musicas_regras.inserir_nova_musica(musica)
    return nova_musica


@rota_musicas.put(
    "/{codigo}",
    # Código HTTP infomando que foi atualizad
    status_code=status.HTTP_202_ACCEPTED,
    summary="Atualização da música",
    description="Atualiza uma música pelo código",
)
async def atualizar_musica(codigo: str, musica: ModeloAtualizaMusica):
    # Atualiza a música pelo código.
    await musicas_regras.atualizar_por_codigo(codigo, musica)


@rota_musicas.delete(
    "/{codigo}",
    # Código HTTP infomando que foi removido
    status_code=status.HTTP_202_ACCEPTED,
    summary="Remoção da música",
    description="Remove a música pelo código",
)
async def remover_musica(codigo: str):
    # Remove uma música pelo código
    await musicas_regras.remover_por_codigo(codigo)


@rota_musicas.get(
    "/{codigo}",
    # Informamos para a pesquisa o modelo da resposta
    response_model=ModeloGeralMusica,
    summary="Pesquisa pela música",
    description="Pesquisa uma música pelo código",
)
async def pesquisar_musica_pelo_codigo(codigo: str):
    # Pesquisa a música pelo código.
    musica = await musicas_regras.pesquisar_por_codigo(codigo, True)
    return musica


@rota_musicas.get(
    "/",
    # E também informamos aqui o modelo da resposta.
    response_model=List[ModeloGeralMusica],
    summary="Pesquisa todas as músicas",
    description="Pesquisa por todas as músicas.",
)
async def pesquisar_todas_as_musicas() -> List[ModeloGeralMusica]:
    # Pesquisa por todas as músicas (sem um filtro)
    todas = await musicas_regras.pesquisar_por_todas()
    return todas
