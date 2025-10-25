"""
Módulo Recibo.

Este módulo define a classe base `BaseRecibo` e suas subclasses `ReciboBancoA` e `ReciboBancoB`,
que representam diferentes formatos de recibo no sistema de caixa eletrônico para os bancos A e B.
Cada banco possui sua própria implementação do recibo, informando a conclusão da transação.

Classes:
    BaseRecibo: Classe abstrata que define o método obrigatório `obrigatorio` que deve ser implementado pelas subclasses.
    ReciboBancoA: Subclasse de `BaseRecibo` que implementa o recibo específico do Banco A.
    ReciboBancoB: Subclasse de `BaseRecibo` que implementa o recibo específico do Banco B.

Métodos:
    BaseRecibo.obrigatorio(): Método abstrato que deve ser implementado por qualquer subclasse que herde de `BaseRecibo`.
    ReciboBancoA.imprimir(): Retorna o recibo formatado para o Banco A.
    ReciboBancoB.imprimir(): Retorna o recibo formatado para o Banco B.
    
Exceções:
    NotImplementedError: Lançada se uma subclasse não implementar o método abstrato `obrigatorio` da `BaseRecibo`.
"""

class BaseRecibo:
    def obrigatorio(self):
        raise NotImplementedError("Este método deve ser implementado pela subclasse.")

class ReciboBancoA(BaseRecibo):
    def imprimir(self) -> str:
        return "Recibo do Banco A: Transação realizada com sucesso."

class ReciboBancoB(BaseRecibo):
    def imprimir(self) -> str:
        return "Recibo do Banco B: Operação concluída com sucesso."
