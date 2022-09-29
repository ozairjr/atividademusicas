from fastapi import APIRouter

import musicas.regras.musicas_regras as musicas_regras

# Minha rota API de músicas
rota_musicas = APIRouter(
    # Prefixo para o caminho da rota
    prefix="/api/musicas"
)


# Cria nova música
@rota_musicas.post("/")
async def criar_nova_musica(musica: dict):
    return {
        "codigo": "texto"
    }

# Atualiza a música pelo código.
@rota_musicas.put("/{codigo}")
async def atualizar_musica(codigo: str, musica: dict):
    return None


# Remove uma música pelo código
@rota_musicas.delete("/{codigo}")
async def remover_musica(codigo: str):
    return None


# Pesquisa a música pelo código.
@rota_musicas.get("/{codigo}")
async def pesquisar_musica_pelo_codigo(codigo: str):
    musica = await musicas_regras.pesquisar_por_codigo(codigo, True)
    return musica


# Pesquisa por todas as músicas (sem um filtro)
@rota_musicas.get("/")
async def pesquisar_todas_as_musicas():
    todas = await musicas_regras.pesquisar_por_todas()
    return todas    
