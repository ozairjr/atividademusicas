# Etapa 2

Organizando a aplicação.

## Instruções da etapa

Vamos organizar nossa aplicação por estruturá-la em vários módulos e pacotes do Python.
Para fins didáticos, iremos ter as seguintes pastas:

- [musicas](./musicas/): Pasta principal da aplicação. 
  - [persistencia](./musicas/persistencia/): Módulo para persistência (repositório) 
  com o banco de dados.
  - [regras](./musicas/regras): Módulos para as regras (casos de uso) da 
  aplicação.
  - [rest](./musicas/regras): Módulos para de _controle_ e/ou _comunicação_ com o 
  FastAPI.

Dentro desses diretórios iremos ter estes arquivos:

- [aplicacao.py](./musicas/aplicacao.py): Arquivo principal do projeto.
Vamos dizer que a aplicação FastAPI _inicia_ aqui.
- [rest_conf.py](./musicas/rest/rest_conf.py): Configurações com o FastAPI.
- [principal_rest.py](./musicas/rest/principal_rest.py): Rotas para o caminho de URL "`/`".
- [musicas_rest.py](./musicas/rest/musicas_rest.py): Rotas para as APIs de música 
(caminho URL "`/api/musicas`").
- [musicas_regras.py](./musicas/regras/musicas_regras.py): Regras para o cadastro e pesquisa
de músicas.
- [musicas_persistencia.py](./musicas/persistencia/musicas_persistencia.py): Responsável pela
persistência das músicas; ou seja, é módulo responsável pela comunicação com o banco de dados.

## Como fazer?

Criamos as pastas e os arquivos requisitados. 
Pegamos o conteúdo do _script_ `etapa01.py` da etapa anterior, e _espalhamos_ o seu conteúdo entre os arquivos
[rest_conf.py](./musicas/rest/rest_conf.py), [principal_rest.py](./musicas/rest/principal_rest.py)
e [musicas_rest.py](./musicas/rest/musicas_rest.py); e, fizemos os ajustes necessários. Dentre os
ajustes, as rotas da API Rest agora são _definidas_ com o 
[APIRouter](https://fastapi.tiangolo.com/tutorial/bigger-applications).

Reestruturamos os arquivos e os interligamos, removemos o arquivo `etapa01.py`. Logo, navegue
pelos novos arquivos.

### Executando o servidor no ambiente virtual

Executando o servidor:

```sh
uvicorn --reload musicas.aplicacao:app
```

### Acessando a aplicação

Teste a aplicação por acessar: 

> http://localhost:8000

Ela irá lhe dizer um "`Oi`".

### Testando as APIs criadas

Tal como a etapa anteriror, o arquivo [musicas.http](./extras/musicas.http) é utilizado com 
a extensão [Rest Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)
do [Visual Code](https://code.visualstudio.com/).

### Frontend para teste

Fizemos um rascunho quase funcional de um _frontend_ 
para a nossa aplicação, utilizando [Bootstrap](https://getbootstrap.com/) e JavaScript.

Para executá-lo com um servidor HTTP, podemos utilizar o Python. Seguem as instruções rápidas:

```sh
cd extras
python -m http.server 9000
```

E acesse pelo seu navegador Web:

> http://localhost:9000/musicas.html

## Material

- [APIRouter](https://fastapi.tiangolo.com/tutorial/bigger-applications).
