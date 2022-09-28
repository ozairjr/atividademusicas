# Etapa 1

Esboço das APIs.

## Instruções da etapa

Criaremos a casca de nosso servidor API REST com o FastAPI.

Utilizando o arquivo [musicas.http](./extras/musicas.http), 
iremos criar os esboços das APIs até a marca
"`Etapa 1 até aqui`". Ou seja, nosso servidor REST estará somente respondendo 
às requisições na porta **8000**, sem validar entradas e saídas.

## Como fazer?

Criamos o _script_ [etapa01.py](./etapa01.py) seguindo o 
[tutorial](https://fastapi.tiangolo.com/tutorial/) 
do FastAPI. Neste único _script_, colocamos todas as APIs solicitadas,
sem fazer validações, somente respodendo quaisquer requisições.

### Executando o servidor no ambiente virtual

Para executar o servidor FastAPI:

```sh
guvicorn --reload etapa01:app
```

### Acessando a aplicação

Teste a aplicação por acessar: 

> http://localhost:8000

Ela irá lhe dizer um "`Oi`".

### Testando as APIs criadas

O arquivo [musicas.http](./extras/musicas.http) é utilizado com 
a extensão [Rest Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)
do [Visual Code](https://code.visualstudio.com/). 
Nós o utilizamos para realizar os testes com nossa API.

## Material

- API REST, documento da :
  - [Red Hat](https://www.redhat.com/pt-br/topics/api/what-is-a-rest-api).
  - [AWS](https://aws.amazon.com/pt/what-is/restful-api/).
- [FastAPI](https://fastapi.tiangolo.com/).
- [CORS](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/CORS).
- [CORS no FastAPI](https://fastapi.tiangolo.com/tutorial/cors/).
