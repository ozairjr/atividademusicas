from fastapi import APIRouter

# Minha API da rota principal
rota_principal = APIRouter(
    # Prefixo para o caminho da rota
    prefix="",
    # Rótulo (tag) para mostrar no documento Swagger.
    tags=["Principal",],

)


@rota_principal.get(
    "/",
    response_model=str,
    summary="Diga oi.",
    description="Rota principal em que se diz um '`Oi`'.",
    )
async def dizer_ola():
    return "Oi"
