"""
Regras e ajustes para músicas.
"""

from typing import List, Optional
import musicas.persistencia.musicas_persistencia as musicas_persistencia
from musicas.regras.regras_excecoes import NaoEncontradoExcecao


async def pesquisar_por_codigo(codigo: str, lanca_excecao_se_nao_encotrado: bool = False) -> Optional[dict]:
    musica = await musicas_persistencia.pesquisar_pelo_codigo(codigo)
    if not musica and lanca_excecao_se_nao_encotrado:
        raise NaoEncontradoExcecao("Música não encontrada")
    return musica


async def pesquisar_por_todas() -> List[dict]:
    todas = await musicas_persistencia.pesquisar_todas()
    return todas