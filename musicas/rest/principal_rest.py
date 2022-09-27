from fastapi import APIRouter

# Minha API da rota principal
rota_principal = APIRouter(
    # Prefixo para o caminho da rota
    prefix=""
)


@rota_principal.get("/")
def dizer_ola():
    return "Oi"
