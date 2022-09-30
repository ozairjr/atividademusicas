# Etapa 8

Testes para cobertura.

## Instruções da etapa

Com as ferramentas apropriadas, criem testes unitários e/ou de integração para _validarmos_ as APIs criadas.

Para um teste de código, ou para o teste de uma função, perguntem-se:

- O código foi _escrito_ corretamente?
- O valor que foi passado como entrada gera o resultado esperado?
- Um valor incorreto gera um comportamento inesperado?
- Do código que esrevi, estou _cobrindo_ grande parte dele?


## Como fazer?

Nós **não** fizemos completamente esta etapa; somente começamos a _escrever_ alguns
testes para algumas de nossas APIs, deixando para vocês continuarem o _estudo_
e _criarem_ mais testes para que a cobertura chegue a pelo menos uns 90% de
código. 📈

### Requerimentos para testes

Para os testes unitários de nosso projeto utilizaremos a bilioteca 
[pytest](https://docs.pytest.org/en/7.1.x/) juntamente com a biblioteca
[pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) para apresentar
a cobertura do projeto. E como temos chamadas assíncronas com o FastAPI,
poderemos utilizar a biblioteca auxiliar
[pytest-asyncio](https://github.com/pytest-dev/pytest-asyncio).

Neste projeto, escolhemos separar os requerimentos necessários para o _ambiente_ 
de testes e os colocamos no arquivo [requerimentos-testes.txt](./requerimentos-testes.txt),
que está "ligado internamente" com arquivo [requerimentos.txt](./requerimentos.txt).

### Base dados separada

Separamos uma base de dados (_database_) para os testes, e a string de conexão para essa base
está _configurada_ no arquivo [env-testes.txt](./extras/confenv/env-testes.txt).

### 'Bug' do Motor

De acordo com este [artigo](https://github.com/tiangolo/fastapi/issues/4473), é necessário
fazermos um ajuste ao criarmos o cliente do Mongo com o [Motor](https://motor.readthedocs.io/en/stable/).
Veja a linha 16 do arquivo [persistencia_bd.py](./musicas/persistencia/persistencia_bd.py).

### Pasta dos testes

Os códigos de testes foram centralizados na pasta [testes](./testes). Há quem estruture esta
pasta em subpastas para negócios, casos de usos ou outra forma. 

Aqui, vamos deixar apenas arquivos com um prefixo `test` seguido de um número,
para termos uma "ordem", e em seguida  um _apresentação_ do que será testado. 

### Escrevendo os testes

Com base na documentação do FastAPI para [testes](https://fastapi.tiangolo.com/tutorial/testing)
normais e [assíncronos](https://fastapi.tiangolo.com/advanced/async-tests) criamos nossos testes
para algumas _entradas_ de nossas APIs:

- [test_01_rota_prinicpal.py](./testes/test_01_rota_prinicpal.py): Testando a API principal.
Somente um teste para ver se há um "`Oi`". 😉

- [test_02_rota_musicas.py](./testes/test_02_rota_musicas.py): Testando _apenas_ o 
cadastrar uma nova música, e o pesquisar com o código.  
Nestes testes iremos trabalhar com 
[fixtures](https://docs.pytest.org/en/7.1.x/fixture.html), que vamos dizer, seria um contexto 
_preparado_ ou fornecido para um dos testes.
Mais detalhes vejam nos comentários 
do arquivo.

### Modelos ajustados

Com os testes descobrimos que modelamos incorretamente a _entrada_ para cadastro de uma nova
música.

```sh
__test_nao_deveria_cadastrar_uma_musica_sem_nome ______

    def test_nao_deveria_cadastrar_uma_musica_sem_nome():
        # Novo registro de música
        musica = {
            "artista": "artista",
            "tempo": 10,
        }
        # Chamando a API para cadastrar
        resposta = cliente_app.post(PREFIXO_URL + "/", json=musica)
        # Deu certo?
>       assert resposta.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
E       assert 201 == 422
E        +  where 201 = <Response [201]>.status_code
E        +  and   422 = status.HTTP_422_UNPROCESSABLE_ENTITY

testes/test_02_rota_musicas.py:101: AssertionError
```

Revisem e vejam a mudança que fizemos no arquivo 
[modelos.py](./musicas/modelos.py).

## Testando

Para testar os testes criados 😊, fizemos o seguinte no Linux:

- Instalamos os pacotes necessários para os testes

```sh
pip install -r requerimentos-testes.txt
```

- Copiamos o arquivo com a _configuração_ do banco de testes para raiz do
projeto com o nome `.env`:

```sh
cp extras/confenv/env-testes.txt .env
```

⚠️ *Atenção*: Lembrem-se de que agora temos um `.env` para o desenvolvimento
do projeto e outro para os testes lá na pasta [confenv](./extras/confenv/).

Em um terminal separado subimos o Docker:

```sh
docker-compose -f ./extras/dockermusica/docker-compose.yml up
```

E rodamos os testes:

```sh
pytest
```

Que gerou esta saída:

```log
== test session starts ==
platform linux -- Python 3.9.14, pytest-7.1.3, pluggy-1.0.0
rootdir: /luizacode/atividademusicas
plugins: cov-4.0.0, anyio-3.6.1, asyncio-0.19.0
asyncio: mode=strict
collected 4 items

testes/test_01_rota_prinicpal.py .   [ 25%]
testes/test_02_rota_musicas.py ...   [100%]
== 4 passed in 0.50s ===
```

Para vermos a cobertura de código, de todos os códigos, incluindo o de testes:

```sh
pytest --cov
```

A saída foi:

```
== test session starts ==
platform linux -- Python 3.9.14, pytest-7.1.3, pluggy-1.0.0
rootdir: /luizacode/atividademusicas
plugins: cov-4.0.0, anyio-3.6.1, asyncio-0.19.0
asyncio: mode=strict
collected 4 items

testes/test_01_rota_prinicpal.py .   [ 25%]
testes/test_02_rota_musicas.py ...   [100%]
== 4 passed in 0.50s ===

---------- coverage: platform linux, python 3.9.14-final-0 -----------
Name                                           Stmts   Miss  Cover
------------------------------------------------------------------
musicas/__init__.py                                0      0   100%
musicas/aplicacao.py                               2      0   100%
musicas/configuracoes.py                           9      0   100%
musicas/modelos.py                                12      0   100%
musicas/persistencia/__init__.py                   0      0   100%
musicas/persistencia/musicas_persistencia.py      32     12    62%
musicas/persistencia/persistencia_bd.py           14      0   100%
musicas/regras/musicas_regras.py                  39     14    64%
musicas/regras/regras_excecoes.py                 13      2    85%
musicas/rest/__init__.py                           0      0   100%
musicas/rest/musicas_rest.py                      23      4    83%
musicas/rest/principal_rest.py                     5      0   100%
musicas/rest/rest_conf.py                         30      2    93%
testes/__init__.py                                 0      0   100%
testes/test_01_rota_prinicpal.py                   9      0   100%
testes/test_02_rota_musicas.py                    47      0   100%
------------------------------------------------------------------
TOTAL                                            235     34    86%
```

Vejam que temos uma cobertura de pelo menos **86%** do código.
