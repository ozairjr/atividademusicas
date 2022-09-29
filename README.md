# Etapa 4

Removendo uma música.

## Instruções da etapa

Após criar uma nova música no banco de dados, e pesquisar por ela; nesta etapa
iremos remover a música do banco de dados, pelo seu código.

Com a API

> DELETE /api/musicas/{codigo}

removeremos a música pelo seu código. Se a música for encontrada e removida
a API retornará o código HTTP 
[202](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/202)
(Aceito/_Accepted_), e sem corpo na resposta.

Se não há música para ser removida, a aplicação irá responder com o código HTTP
[404](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/404)
(Não encontrado/_Not Found_) com a mensagem:

```json
{
  "musica": "Música não encontrada"
}
```


Quaisquer outros erros poderão ser gerados ou _interceptados_ pelo 
próprio FastAPI.

## Como fazer?

Continuando da etapa anterior, no qual já consultamos e inserimos 
no banco de dados.

### Removendo a música do banco de dados

Em [musicas_persistencia.py](./musicas/persistencia/musicas_persistencia.py),
criamos a função `remover_uma_musica_pelo_codigo()` que irá diretamente
remover a música do banco de dados. A função retorna o valor `True`, 
se o registro foi encontrado e removido no banco de dados.

### Regra para remover a música

Como a função de remover de 
[musicas_persistencia.py](./musicas/persistencia/musicas_persistencia.py)
retorna `True` para indicar que a música foi removida; nós _deixamos_
para testar se a música existe após a remoção da camada
de `_persistencia`.

Logo, em [musicas_regras.py](./musicas/regras/musicas_regras.py), a
_regra_ de "verificar se a música existe para remover" na verdade ficou
"remover do banco e confirmar se algum registro foi removido".

### Ajuste API remover

Em [musicas_rest.py](./musicas/rest/musicas_rest.py) ajustamos o código
para devolver o código HTTP [202](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/202)
(Aceito/_Accepted_) e chamar a função de remoção de 
[musicas_regras.py](./musicas/regras/musicas_regras.py).


## Testando

Tal como na etapa anterior ...

### Criação do arquivo `.env`

Copie o arquivo [env.txt](./extras/confenv/env.txt) para a raiz do projeto com o nome `.env`.

No Linux e na raiz do projeto:

```sh
cp ./extras/confenv/env.txt .env
```

No Windows, com o Prompt de Comando na raiz do projeto:

```batch
copy .\extras\confenv\ext.txt .env
```

Altere se necessário o valor da variável no arquivo `.env`
com a string de conexão de *seu* banco de dados.

### Banco de dados MongoDB

Se necessário, inicie o seu banco de dados MongoDB.
No caso deste projeto, temos um MongoDB _com_ um Docker,
que vamos executá-lo com o docker-compose, na raiz do projeto.

No Linux, deixando o _terminal_ travado: 
```sh
docker-compose -f ./extras/dockermusica/docker-compose.yml up
```

### Executando o servidor

Executando o servidor na raiz do projeto e _dentro_ do ambiente virtual:

```sh
uvicorn --reload musicas.aplicacao:app
```

### Acessando a aplicação

Teste a aplicação por acessar: 

> http://localhost:8000

Ela irá lhe dizer um "`Oi`".

### Testando as APIs criadas

Podemos continuar nossos testes com o arquivo 
[musicas.http](./extras/musicas.http), que é utilizado com 
a extensão [Rest Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)
do [Visual Code](https://code.visualstudio.com/).

### Frontend para teste

Também podemos utilizar o rascunho de _front_ _end_.
Para executá-lo com o Python:

```sh
cd extras
python -m http.server 9000
```

E acesse pelo seu navegador Web:

> http://localhost:9000/musicas.html

## Material

- [MongoDB](https://www.mongodb.com/).
- [Motor](https://motor.readthedocs.io/en/stable/).
- [Docker](https://docs.docker.com).
- [docker-compose](https://docs.docker.com/compose/).
- [Async IO no Python](https://realpython.com/async-io-python/).
- [FastAPI](https://fastapi.tiangolo.com/tutorial/).
