"""
Módulo InterfaceUsuario.

Este módulo define a classe base `BaseInterfaceUsuario` e suas subclasses `InterfaceUsuarioBancoA` e `InterfaceUsuarioBancoB`,
que representam diferentes interfaces de usuário no sistema de caixa eletrônico para os bancos A e B, respectivamente. 
Cada banco oferece suas próprias opções de interface para interação com o usuário.

Classes:
    BaseInterfaceUsuario: Classe abstrata que define o método obrigatório `obrigatorio` que deve ser implementado pelas subclasses.
    InterfaceUsuarioBancoA: Subclasse de `BaseInterfaceUsuario` que implementa a interface do usuário para o Banco A.
    InterfaceUsuarioBancoB: Subclasse de `BaseInterfaceUsuario` que implementa a interface do usuário para o Banco B.

Métodos:
    BaseInterfaceUsuario.obrigatorio(): Método abstrato que deve ser implementado por qualquer subclasse que herde de `BaseInterfaceUsuario`.
    InterfaceUsuarioBancoA.mostrar_opcoes(): Retorna as opções disponíveis na interface de usuário do Banco A.
    InterfaceUsuarioBancoB.mostrar_opcoes(): Retorna as opções disponíveis na interface de usuário do Banco B.
    
Exceções:
    NotImplementedError: Lançada se uma subclasse não implementar o método abstrato `obrigatorio` da `BaseInterfaceUsuario`.
"""

class BaseInterfaceUsuario:
    def obrigatorio(self):
        raise NotImplementedError("Este método deve ser implementado pela subclasse.")

class InterfaceUsuarioBancoA(BaseInterfaceUsuario):
    def mostrar_opcoes(self) -> str:
        return "Interface do Banco A: Ver saldo, Retirar dinheiro, Depositar."

class InterfaceUsuarioBancoB(BaseInterfaceUsuario):
    def mostrar_opcoes(self) -> str:
        return "Interface do Banco B: Consultar saldo, Sacar, Depositar."
