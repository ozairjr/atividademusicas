from typing import Optional

from pydantic import BaseModel, Field


# Modelo base de uma música (para cadastro)
class ModeloBaseMusica(BaseModel):
    """
    Modelo básico para o registro de uma música.
    """
    # Nome da música
    nome: str = Field(
        # Padrão seria
        ...,
        # Tamanho mínimo
        min_length=3,
        # Tamanho máximo
        max_length=128,
        # Descrição
        description="Nome da música",
    )
    # Artista da música
    artista: str = Field(
        # Padrão seria
        ...,
        # Tamanho mínimo
        min_length=3,
        # Tamanho máximo
        max_length=128,
        # Descrição
        description="Artista da música"
    )
    # Tempo em segundos (opcional)
    tempo: Optional[int] = Field(
        # Valor padrão
        None,
        # Se informado o valor mínimo é 1
        ge=1,
        description="Tempo (opcional) da música."
    )

    # Configurações extra para o Swagger
    class Config:
        schema_extra = {
            "example": {
                "nome": "nomemusica",
                "artista": "nomeartista",
                "tempo": 10
            }
        }

# Modelo do código da Música
class ModeloCodigoMusica(BaseModel):
    """
    Registro com o código da música.
    """
    # Código da música
    codigo: str = Field(
        ...,
        description="Código da música, no formato uuid v4",
    )

    #Configurações extras
    class Config:
        schema_extra = {
            "example": {
                "codigo": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6",
            }
        }


# Modelo 'geral' da música
class ModeloGeralMusica(ModeloCodigoMusica, ModeloBaseMusica):
    # Possui todos os campos das duas classes informadas.
    ...

class ModeloAtualizaMusica(ModeloBaseMusica):
    # Modelo para atualizar a música, em que o código 
    # é opcional.
    codigo: Optional[str] = None