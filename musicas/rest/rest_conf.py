from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from musicas.rest.musicas_rest import rota_musicas
from musicas.rest.principal_rest import rota_principal


def configurar_rotas(app: FastAPI):
    # Publicando as rotas para o FastAPI.
    app.include_router(rota_principal)
    app.include_router(rota_musicas)


def configurar_api_rest(app: FastAPI):
    # Configurando o CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def criar_aplicacao_fastapi():
    # Crio a aplicação FastAPI
    app = FastAPI()

    # Configuro a aplicação FastAPI
    configurar_api_rest(app)
    # ... e configuro suas rotas
    configurar_rotas(app)

    return app
