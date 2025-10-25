class BaseInterfaceUsuario:
    def obrigatorio(self):
        raise NotImplementedError("Este método deve ser implementado pela subclasse.")

class InterfaceUsuarioBancoA(BaseInterfaceUsuario):
    def mostrar_opcoes(self) -> str:
        return "Interface do Banco A: Ver saldo, Retirar dinheiro, Depositar."

class InterfaceUsuarioBancoB(BaseInterfaceUsuario):
    def mostrar_opcoes(self) -> str:
        return "Interface do Banco B: Consultar saldo, Sacar, Depositar."
