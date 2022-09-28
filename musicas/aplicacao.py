from musicas.rest.rest_conf import criar_aplicacao_fastapi

# Criando minha aplicação FastAPI e deixando-a 'global'.
# Este `app` será 'chamado' pelo guvicorn. 
app = criar_aplicacao_fastapi()