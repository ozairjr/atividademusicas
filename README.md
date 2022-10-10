# Etapa 0

Criação do ambiente.

## Instruções da etapa

Dentro da pasta `atividadesmusicas`, criaremos um
ambiente virtual do Python ([venv](https://docs.python.org/pt-br/3/library/venv.html)) 
o qual serão instaladas as seguintes
bibliotecas:

- [fastapi](https://fastapi.tiangolo.com/),
- [uvicorn](https://www.uvicorn.org/),
- [motor](https://motor.readthedocs.io/en/stable/).

## Como fazer?

Criamos o arquivo [requerimentos.txt](./requerimentos.txt), que contém
os pacotes Python solicitados e suas versões. 

Realizamos as próximas instruções para configurar nosso ambiente. 

### Criação do ambiente virtual

Criando o ambiente virtual no Linux, usando o Python 3.9:

```shell
python3.9 -m venv venv
```

Criando o ambiente virtual no Windows, usando o Python 3.9, no Prompt de Comando:

```batch
python -m venv venv
```

### Ativando o ambiente virtual

Para _ativar_ o ambiente virtual no Linux:

```shell
source venv/bin/activate
```

E no Windows:

```batch
venv\Scripts\activate
```

### Instalando os pacotes no ambiente virtual

Instalando os pacotes necessários para projeto:

```sh
pip install -r requerimentos.txt
```

## Material

- [pip](https://pip.pypa.io/en/stable/getting-started/).
- [venv](https://docs.python.org/pt-br/3/library/venv.html).
