from typing import Callable, Tuple
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from musicas.regras.regras_excecoes import NaoEncontradoExcecao
from musicas.rest.musicas_rest import rota_musicas
from musicas.rest.principal_rest import rota_principal


def responder_naoencontradoexcecao(requisicao: Request, excecao: NaoEncontradoExcecao):
    # Respondeo o erro 404
    return JSONResponse(
        # Código HTTP da resposta
        status_code=status.HTTP_404_NOT_FOUND,
        # Mensagem
        content={
            "mensagem": excecao.mensagem
        }
    )


def configurar_interceptador_excecoes(app: FastAPI) -> Tuple[Callable]:
    @app.exception_handler(NaoEncontradoExcecao)
    async def interceptador_naoencontradoexcecao(request: Request, exc: NaoEncontradoExcecao):
        return responder_naoencontradoexcecao(request, exc)

    # Vamos retornar as funções interceptadoras em uma tupla
    return (interceptador_naoencontradoexcecao, )


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
    # Configurando os interceptadores
    configurar_interceptador_excecoes(app)


def criar_aplicacao_fastapi():
    # Crio a aplicação FastAPI
    app = FastAPI()

    # Configuro a aplicação FastAPI
    configurar_api_rest(app)
    # ... e configuro suas rotas
    configurar_rotas(app)

    return app
