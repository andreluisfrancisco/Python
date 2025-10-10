"""
Módulo Transacao.

Este módulo define a classe base `BaseTransacao` e suas subclasses `TransacaoBancoA` e `TransacaoBancoB`, 
que representam diferentes tipos de transações no sistema de caixa eletrônico, de acordo com o banco selecionado.
Cada banco implementa sua própria lógica de processamento de transação, seguindo o padrão de herança.

Classes:
    BaseTransacao: Classe abstrata que define o método obrigatório `obrigatorio` que deve ser implementado pelas subclasses.
    TransacaoBancoA: Subclasse de `BaseTransacao` que implementa o processamento de transações específicas do Banco A.
    TransacaoBancoB: Subclasse de `BaseTransacao` que implementa o processamento de transações específicas do Banco B.

Métodos:
    BaseTransacao.obrigatorio(): Método abstrato que deve ser implementado por qualquer subclasse que herde de `BaseTransacao`.
    TransacaoBancoA.processar(): Processa a transação para o Banco A.
    TransacaoBancoB.processar(): Realiza a transação para o Banco B.
    
Exceções:
    NotImplementedError: Lançada se uma subclasse não implementar o método abstrato `obrigatorio` da `BaseTransacao`.
"""

class BaseTransacao:
    # Método obrigatório para implementação nas subclasses
    def obrigatorio(self):
        raise NotImplementedError("Este método deve ser implementado pela subclasse.")

class TransacaoBancoA(BaseTransacao):
    def processar(self) -> str:
        return "Transação processada no Banco A."

class TransacaoBancoB(BaseTransacao):
    def processar(self) -> str:
        return "Transação realizada no Banco B."
