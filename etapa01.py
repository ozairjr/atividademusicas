# Importando a biblioteca do FastAPI
from fastapi import FastAPI
# Recurso para CORS
from fastapi.middleware.cors import CORSMiddleware

# Minha aplicação REST
app = FastAPI()

# Configuração para CORS
app.add_middleware(
    CORSMiddleware,
    # Vou permitir todas a origens
    # Não faça isto em casa! ;-)
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota principal, diga um oi


@app.get("/")
def dizer_ola():
    return "Oi"

# Cadastrando uma nova música


@app.post("/api/musicas/")
def criar_nova_musica(musica: dict):
    print("Salvar nova musica", musica)
    return {
        "codigo": "texto"
    }


# Atualizando a música
@app.put("/api/musicas/{codigo}")
def atualizar_musica(codigo: str, musica: dict):
    print("Atualizar musica", codigo, "|", musica)
    return None


# Removendo a música
@app.delete("/api/musicas/{codigo}")
def remover_musica(codigo: str):
    print("Removendo musica de codigo", codigo)
    return None


# Pequisando a música pelo código
@app.get("/api/musicas/{codigo}")
def pesquisar_musica_pelo_codigo(codigo: str):
    print("Pesquisar pelo codigo", codigo)
    return {
        "codigo": codigo,
        "nome": "Nome da musica",
        "artista": "Uma artista"
    }


# Pesquisando todas as músicas.
@app.get("/api/musicas/")
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
