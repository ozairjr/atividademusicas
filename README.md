# Atividade API de Músicas

Atividade para um cadastro de músicas com [FastAPI](https://fastapi.tiangolo.com/)
e [MongoDB](https://www.mongodb.com/).

## Objetivo


Nesta atividade extra iremos construir uma API em FastAPI para cadastrar músicas. O
registro de uma música deverá conter:

- `nome`: Nome da música. Este é um campo texto obrigatório que deverá conter no
mínimo 2 caracteres sem espaços e no máximo 128.
- `artista`: Artista da música. Este é um campo texto obrigatório que deverá conter
no mínimo 2 caracteres sem espaços e no máximo 128.
- `tempo`: Tempo em segundos da música. Este é um campo inteiro opcional.
- `codigo`: Código da música. É um campo no formato texto e será gerado pelo
sistema.

Mais detalhes serão apresentados adiante.
Os registros das músicas serão salvos no banco não relacional MongoDB.

## Apresentação das atividades

As atividades estão divididas em etapas, e cada etapa está em uma _branch_ diferente
deste repositório.

- Etapa 0: Criação do ambiente.
- Etapa 1: Esboço das APIs.
- Etapa 2: Organizando a aplicação.
- Etapa 3: Conectando o banco de dados.
- Etapa 4: Cadastro de uma nova música.
- Etapa 5: Removendo uma música.
- Etapa 6: Atualização da música.
- Etapa 7: Pesquisa com filtros.
- Etapa 8: Teste unitários.