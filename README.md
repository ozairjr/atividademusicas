# Etapa 1

Esboço das APIs

## Instruções da etapa

Criaremos a casca de nosso servidor API REST com o FastAPI.

Utilizando o arquivo [musicas.http](./extras/musicas.http), 
iremos criar os esboços das APIs até a marca
"`Etapa 1 até aqui`". Ou seja, nosso servidor REST estará somente respondendo 
às requisições na porta **8000**, sem validar entradas e saídas.

## Como fazer?

_Editar_/Estudar o arquivo [etapa01.py](./etapa01.py)

### Executando o servidor no ambiente virtual

Instalando os pacotes necessários para projeto:

```sh
guvicorn --reload etapa01:app
```

### Acessando a aplicação

Teste a aplicação por acessar: 

> http://localhost:8000

Ela irá lhe dizer um "`Oi`.

### Testando as APIs criadas

O arquivo [musicas.http](./extras/musicas.http) é utilizado com 
a extensão [Rest Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)
do [Visual Code](https://code.visualstudio.com/).

## Material

- API REST, documento da :
  - [Red Hat](https://www.redhat.com/pt-br/topics/api/what-is-a-rest-api).
  - [AWS](https://aws.amazon.com/pt/what-is/restful-api/)
- [FastAPI](https://fastapi.tiangolo.com/).
- [CORS](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/CORS).
- [CORS no FastAPI](https://fastapi.tiangolo.com/tutorial/cors/).