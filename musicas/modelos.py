from typing import Optional

from pydantic import BaseModel, Field


# Modelo base de uma música (para cadastro)
class ModeloBaseMusica(BaseModel):
    # Nome da música
    nome: str = Field(
        # Valor padrão
        None,
        # Tamanho mínimo
        min_length=3,
        # Tamanho máximo
        max_length=128,
    )
    # Artista da música
    artista: str = Field(
        # Valor padrão
        None,
        # Tamanho mínimo
        min_length=3,
        # Tamanho máximo
        max_length=128,
    )
    # Tempo em segundos (opcional)
    tempo: Optional[int] = Field(
        # Valor padrão
        None,
        # Se informado o valor mínimo é 1
        ge=1
    )

# Modelo do código da Música
class ModeloCodigoMusica(BaseModel):
    # Código da música
    codigo: str


# Modelo 'geral' da música
class ModeloGeralMusica(ModeloCodigoMusica, ModeloBaseMusica):
    # Possui todos os campos das duas classes informadas.
    ...
