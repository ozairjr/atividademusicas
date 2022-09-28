from fastapi import APIRouter

# Minha rota API de músicas
rota_musicas = APIRouter(
    # Prefixo para o caminho da rota
    prefix="/api/musicas"
)


# Cria nova música
@rota_musicas.post("/")
def criar_nova_musica(musica: dict):
    print("Salvar nova musica", musica)
    return {
        "codigo": "texto"
    }

# Atualiza a música pelo código.
@rota_musicas.put("/{codigo}")
def atualizar_musica(codigo: str, musica: dict):
    print("Atualizar musica", codigo, "|", musica)
    return None


# Remove uma música pelo código
@rota_musicas.delete("/{codigo}")
def remover_musica(codigo: str):
    print("Removendo musica de codigo", codigo)
    return None


# Pesquisa a música pelo código.
@rota_musicas.get("/{codigo}")
def pesquisar_musica_pelo_codigo(codigo: str):
    print("Pesquisar pelo codigo", codigo)
    return {
        "codigo": codigo,
        "nome": "Nome da musica",
        "artista": "Uma artista"
    }


# Pesquisa por todas as músicas (sem um filtro)
@rota_musicas.get("/")
def pesquisar_todas_as_musicas():
    print("Pesquisar todas")
    return [
        {
            "codigo": "123",
            "nome": "Nome da musica",
            "artista": "Uma artista"
        },
        {
            "codigo": "124",
            "nome": "Outra música",
            "artista": "De outro artista"
        },
    ]
