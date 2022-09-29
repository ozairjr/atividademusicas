# Etapa 6

Atualização da música.

## Instruções da etapa

Agora iremos atualizar a música no banco de dados. Para a API:


> POST /api/musicas/{codigo}

atualizaremos a música pelo seu código.

Antes de atualizar, precisamos validar as seguintes **regras**:

- Uma música deve ter um nome com pelo menos 2 caracteres e no máximo 128
caracteres.
- A música atualizada não pode coincidir com o nome de outra música. Não temos duas músicas
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
- Opcionalmente, pode-se informar o código no corpo da requisição.
- Se o código for informado no corpo da requisição; este deve ser igual
ao código da URL de requisição ("`/{codigo}`").

Notem que são quase todas as mesmas validações para 
se cadastrar uma nova música.

E, ao atualizarmos uma música pelo código:

- se música existe e for atualizada; então, a API retornará o código HTTP 
[202](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/202)
(Aceito/_Accepted_), e sem corpo na resposta.

- se música não existe; então, a aplicação irá responder com o código HTTP
[404](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/404)
(Não encontrado/_Not Found_) com a mensagem:

```json
{
  "mensagem": "Música não encontrada"
}
```

- se o código da música na URL de atualização for diferente
do código informado no corpo da mensagem; então, a API responderá
com o código 
[409](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/409)
(Conflito/_Conflict_) com a mensagem:

```json
{
  "mensagem": "Códigos diferentes"
}
```

- se a música atualizada coincidir em nome com outra música do 
banco de dados; então, a API responderá com o código 
[409](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/409)
(Conflito/_Conflict_) com a mensagem:

```json
{
  "mensagem": "Há outra música com este nome"
}
```

Quaisquer outros erros poderão ser gerados ou _interceptados_ pelo 
próprio FastAPI.

## Como fazer?

Seguem os ajustes feitos no código.

### Atualizando a música do banco de dados

Em [musicas_persistencia.py](./musicas/persistencia/musicas_persistencia.py),
criamos a função `atualizar_uma_musica_pelo_codigo()` que somente
irá atualizar a música no banco de dados; retornando `True` informando
se há registros que foram atualizados.

### Regras atualizar


Ajustamos [musicas_regras.py](./musicas/regras/musicas_regras.py)
para aproveitar a regras e os modelos para criar um registro e 
escrevemos o código para validar e atualizar o registro da música.

Notem que a função `validar_nova_musica()` foi reescrita como 
sendo a função `validar_musica()` para atender os processos de criar
e atualizar as músicas.

Também criamos a exceção `CodigosDiferentesExcecao` em 
[regras_excecoes.py](./musicas/regras/regras_excecoes.py) para os
casos em que a pessoa passa um código no corpo da atualização
que é diferente do que está na URL. Percebam que esta exceção
é uma especialização (subclasse) de `OutroRegistroExcecao`. 
Fizemos isto para que a aplicação retorna-se o mesmo código 
HTTP de _Conflito_ para este tipo de exceção.

### Ajuste API remover

Em [musicas_rest.py](./musicas/rest/musicas_rest.py) ajustamos o código
para devolver o código HTTP [202](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/202)
(Aceito/_Accepted_) e chamar a função de remoção de 
[musicas_regras.py](./musicas/regras/musicas_regras.py).


## Testando

Na próxima [etapa](https://github.com/ozairjr/atividademusicas/blob/etapa07/README.md) ....
