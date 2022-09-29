# Etapa 4

Cadastro de uma nova música no banco de dados.

## Instruções da etapa

Com o nosso banco de dados MongoDB, vamos agora cadastrar uma nova música nele.
Isto implica em ajustarmos a API:

> POST /api/musicas

para "enviar" a requisição de salvar a nova música para o banco de dados.

Antes de salvar a nova música, precisamos validar as seguintes **regras**:

- Uma música deve ter um nome com pelo menos 2 caracteres e no máximo 128
caracteres.
- Neste projeto, o nome da música deve ser único. Logo, não temos duas músicas
com o nome "Alegria", por exemplo. Para _facilitar_, não iremos considerar as
diferenças de letras maiúsculas e minúsculas, bem como acentuação. Logo, por 
exemplo, os seguintes nomes de músicas são três nomes diferentes em nosso projeto:
três são nomes diferentes para o meu projeto: 
"`Música`", "`música`" e "`musica`".
- Uma música deve ter um pessoa ou um grupo que é o artista da música,
seu valor deter ter menos 2 caracteres e no máximo 128 caracteres.
- Duas ou mais músicas podem ter o mesmo artista.
- Uma música pode ter opcionalmente um tempo em segundos. Se o tempo for
informado deverá ser maior que 0.
- Antes de salvar a música no banco, iremos gerar um código único para
música. Cada música terá o seu código único gerado pelo _sistema_.


Na API, se conseguirmos cadastrar a música no banco de dados, iremos retornar o
código HTTP [201](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/201)
(Criado/_Created_), e no corpo de resposta iremos informar apenas o novo 
código da música:

```json
{
  "codigo": "<codigo da nova música>"
}
```

Se ao tentar cadastrar uma nova música, há outra música com o mesmo nome 
(seguindo a regra definida), a API irá retornar o código HTTP 
[409](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/409)
(Conflito/_Conflict_) informando a seguinte mensagem:

```json
{
  "mensagem": "Há outra música com este nome"
}
```

Quaisquer outros erros poderão ser gerados ou _interceptados_ pelo 
próprio FastAPI.

## Como fazer?

Continuando da etapa anterior, que já temos um banco MongoDB 
e já o configuramos em nossa aplicação, agora vamos fazer 
as _atividades_ para cadastrar a nova música.

### Cadastro da nova música no MongoDB

Neste projeto, vamos considerar que todas as validações para cadastrar
uma nova música estarão _escritas_ no arquivo
[musicas_regras.py](./musicas/regras/musicas_regras.py). Assim sendo,
vamos somente *salvar* a música no banco de dados na função
`inserir_uma_nova_musica()` no arquivo 
[musicas_persistencia.py](./musicas/persistencia/musicas_persistencia.py).

Além disso, adicionamos a função `pesquisar_pelo_nome()` que será utilizada
pela `_regra` de validação em que precisamos verificar se o nome único da
música.

É digno de nota que poderíamos criar um índice único no MongoDB para garantir
que ao inserir uma nova música seu nome seja único. Mas, aqui neste projeto,
fizemos isto programaticamente (no código Python mesmo).

### Classes modelos para música

O FastAPI trabalha com o [pydantic](https://pydantic-docs.helpmanual.io/)
para validar as entradas e saídas da API através de tipos básicos do Python
e [modelos](https://fastapi.tiangolo.com/tutorial/extra-models/) de classes. 

Modelamos nossas _classes_ para
os registros de música no arquivo [modelos.py](./musicas/modelos.py) conforme
a entrada ou saída da API:

- `ModeloBaseMusica`: Modelo básico para o cadastro de uma nova música. É 
usado na entrada da API `POST`.
- `ModeloCodigoMusica`: Modelo em que apresenta apenas o código da música.
É usado na saída da API `POST`.
- `ModeloGeralMusica`: Modelo _completo_ da música com nome, artista, tempo 
e código. Ajustamos as APIs de pesquisa para utilizá-lo.

Há quem associe as validações do `pydantic` como validações para a camada
 `_rest`; mas, aqui somente para o nosso estudo, e pensando que o ele não é 
 amarrado ao FastAPI, vamos _aproveitá-lo_ para ser nosso pré-validador para
o cadastro da nova música e o modelo irá ser _utilizado_ também na camada
`_regras`.


### Regras para nova música

As regras definidas nesta etapa estão escritas na função `validar_nova_musica()`
no arquivo [musicas_regras.py](./musicas/regras/musicas_regras.py). Aproveitamos
neste projeto, que a música já é validada pelo "FastAPI", e **não** refizemos
as validações de nome, artista e código de música (Seria bom fazer em projeto
real). 

_Escrevemos_ a regra do nome da música que deve ser único; se no processo de criar
uma nova música encontrarmos uma com o mesmo nome lançamos uma exceção do 
tipo `OutroRegistroExcecao`, que foi definida no arquivo 
[regras_excecoes.py](./musicas/regras/regras_excecoes.py).

### Interceptando 'OutroRegistroExcecao'

A exceção `OutroRegistroExcecao` foi interceptada no arquivo 
[rest_conf.py](./musicas/rest/rest_conf.py) para retornar sua mensagem e código
HTTP [409](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/409).

### Código da nova música

No arquivo [musicas_regras.py](./musicas/regras/musicas_regras.py), nós aproveitamos
a biblioteca nativa do Python [uuid](./https://docs.python.org/3/library/uuid.html)
para gerar o código único da música.

### Modelando e ajeitando a camada REST

Com os [modelos](./musicas/modelos.py) para entrada e saída do 
[pydantic](https://fastapi.tiangolo.com/tutorial/extra-models/) utilizados pelo FastAPI;
editamos o arquivo [musicas_rest.py](./musicas/rest/musicas_rest.py) para trabalhar
com estes modelos nas funções de criar novo produto e de pesquisa.

Vejam também que na decoração ([decorator](https://peps.python.org/pep-0318/))
da função `criar_nova_musica()`, nós adicionamos o parâmetro (atributo) 
`status_code` para retornar o código HTTP 
[201](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/201) (Criado/_Created_).


## Testando

Para testar a aplicação, siga as seguintes instruções:

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
