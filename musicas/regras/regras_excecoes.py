"""
Exceções das regras.
"""


class RegraExcecao(Exception):
    # Exceção geral das regras
    def __init__(self, mensagem: str) -> None:
        super(RegraExcecao, self).__init__(mensagem)
        self.mensagem = mensagem


class NaoEncontradoExcecao(RegraExcecao):
    # Exceção geral para um registro não encontrado.
    def __init__(self, mensagem: str) -> None:
        super(NaoEncontradoExcecao, self).__init__(mensagem)


class OutroRegistroExcecao(RegraExcecao):
    # Exceção de que há outro registro coincidindo...
    def __init__(self, mensagem: str) -> None:
        super(OutroRegistroExcecao, self).__init__(mensagem)

# 
class CodigosDiferentesExcecao(OutroRegistroExcecao):
    def __init__(self) -> None:
        super().__init__("Código diferentes") 