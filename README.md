# Etapa 3

Conectando no banco de dados.

## Instruções da etapa

No nosso banco de dados MongoDB, iremos criar a base de dados (_database_) "`musicasbd`".
E as músicas serão salvas na coleção (_tabela_) "`musica`".

Criaremos o arquivo [persistencia_bd.py](./musicas/persistencia/persistencia_bd.py)
para termos os acessos ao banco de dados MongoDB.

Vamos ajustar as seguintes APIs para realizarem suas pesquisas com o banco de dados:

> GET /api/musicas/{codigo}

Na consulta da música pelo código, retornará a pesquisa realizada no banco de dados.
Se encontrar o registro, a API retornará o código HTTP 200 e o registro. 
Se não encontrar, a API retornará o código HTTP 404 , com a seguinte
mensagem:

```json
{
  "mensagem": "Música não encontrada"
}
```

E para a API:

> GET /api/musicas

Pesquisamos todas as músicas que estão registradas no banco de dados.

É digno de nota, que para esta etapa e as seguintes, qualquer acesso que
[musicas_rest.py](./musicas/rest/musicas_rest.py) precisar fazer ao banco
de dados, ela obrigatoriamente precisará _passar_ (ou solicitar) através
do arquivo [musicas_regras.py](./musicas/regras/musicas_regras.py). Em suma,
a camada `_rest` não enxerga o banco, ela precisa da intermediária 
`_regras` para realizar seus trabalhos. 
A camada `_rest` é quem trbalha diretamente com a camada
`_persistencia`. 

## Como fazer?

Nesta etapa há diversas atividades envolvidas.

### Instalação do MongoDB

Para realizarmos esta atividade, precisaremos de um banco de dados MongoDB.
Você pode _ter_ um Mongo de três formas diferentes:

1. Instalá-lo localmente. Seguem as [instruções](https://www.mongodb.com/docs/manual/installation/).
2. Instalá-lo via [Docker](https://hub.docker.com/_/mongo). 
Sugestão de [instruções](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-enterprise-with-docker/).
3. Instalar e usar o Mongo _gratuito_ da [Atlas](https://www.mongodb.com/atlas/database).

Neste projeto, escolhemos a 2ª opção. Criamos o arquivo
[docker-compose.yml](./extras/dockermongo/docker-compose.yml), que será usado mais adiante.

### Configuração para o banco de dados

O acesso ao banco de dados é _configurado_ em uma 
[string de conexão](https://www.mongodb.com/docs/manual/reference/connection-string/). 
Para o nosso banco de dados local, com o Docker, a string
de conexão é:

> mongodb://localhost/musicasbd

Para não deixarmos esta string de conexão fixa em nosso código Python, vamos colocá-la
em um arquivo _externo_; por enquanto, está no arquivo 
[env.txt](./extras/confenv/env.txt), associada à chave
`BD_URL`.

Depois, esse arquivo será copiado para a raiz do projeto com o nome de `.env`, para ser carregado pela
bilbioteca [python-dotenv](./https://pypi.org/project/python-dotenv/) (Biblioteca
nova para o projeto).

Depois criamos o arquivo [configuracoes.py](./musicas/configuracoes.py) para centralizar
estas configurações de nossa aplicação. Aproveitamos o 
[Pydantic](https://pydantic-docs.helpmanual.io/usage/settings) para criar uma classe a
qual carrega as nossas configurações externas; neste caso, a string de conexão com o banco
de dados.

### Conectando no MongoDB

Utilizamos o [Motor](https://motor.readthedocs.io/en/stable/) para a nossa aplicação
_conversar_ com o MongoDB.

Escrevemos o arquivo [persistencia_bd.py](./musicas/persistencia/persistencia_bd.py) 
para ser o ponto central da aplicação para conectar e acessar as coleções do MongoDB.
Por conta do FastAPI, vamos trabalhar com o 
[Motor assíncrono](https://motor.readthedocs.io/en/stable/tutorial-asyncio.html); logo
vamos ajustando a aplicação para ter funções 
[assíncronas](https://docs.python.org/3/library/asyncio.html).

### Pesquisando pelas músicas

Para as pesquisas com banco de dados pelas músicas, editamos o arquivo 
[musicas_persistencia.py](./musicas/persistencia/musicas_persistencia.py) para usar
a biblioteca [Motor](https://motor.readthedocs.io/en/stable/).

### 'Regras' para pesquisar por código

Para a API de pesquisar a música pelo código, há a seguinte instrução:

>Se não encontrar, a API retornará o código HTTP 404 , com a seguinte mensagem ...

Logo, se uma música não é encontrada, nós teremos que retornar um código HTTP 
[404](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/404) com uma mensagem
informando que o produto não foi encontrado. 

Vamos optar por lançar uma exceção para que a camada `_rest` a trate devidamente.
Logo, criamos o arquivo [regras_excecao.py](./musicas/regras/regras_excecoes.py) para
conter todas as exceções das regras. E no caso da música não encontrada, iremos
lançar a exceção do tipo `NaoEncontradoExcecao`.

### Tratando as exceções de regras com o FastAPI

Na atividade anterior, ao não encontrar uma determinada música, é lançada uma exceção
do tipo `NaoEncontradoExcecao` da camada `_regras`. Podemos _orientar_ o FastAPI para 
retornar um erro HTTP 404 ao receber esta exceção por criar um **inteceptador** de
exceções 
([exception handler](https://fastapi.tiangolo.com/tutorial/handling-errors/#install-custom-exception-handlers)).

Assim, no arquivo [ss](./musicas/rest/rest_conf.py) criamos a função
`configurar_interceptador_excecoes()` para inteceptar as exceções do tipo `NaoEncontradoExcecao`
para retornar o erro HTTP 404 e sua mensagem.

### Ajustes na camada `_rest_

Ajustamos os arquivos de rotas ([musicas_rest.py](./musicas/rest/musicas_rest.py) e
[principal_rest.py](./musicas/rest/principal_rest.py)) para possuírem somente funções assíncronas.

No arquivo [musicas_rest.py](./musicas/rest/musicas_rest.py) nas _APIS_/funções de pesquisa de
músicas, nós _utilizamos_ a camada `_regras_ para realizar as operações.

### Reestruturação da pasta `extras`

Como atividade extra, fizemos um orgranização na pasta [extras](./extras/):
  - [api](./extras/api/): Conterá os arquivos de clientes Rest (extensão `.http`).
  - [dockermusica](./extras/dockermusica/): Meus arquivos de Docker.
  - [frontend](./extras/frontend/): Arquivos do _esboço_ do _front_ _end_ para a minha API.


## Testando

Para testar a aplicação, siga as seguintes instruções.

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
guvicorn --reload musicas.aplicacao:app
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
