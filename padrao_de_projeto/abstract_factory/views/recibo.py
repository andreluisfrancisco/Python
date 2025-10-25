class BaseRecibo:
    def obrigatorio(self):
        raise NotImplementedError("Este método deve ser implementado pela subclasse.")

class ReciboBancoA(BaseRecibo):
    def imprimir(self) -> str:
        return "Recibo do Banco A: Transação realizada com sucesso."

class ReciboBancoB(BaseRecibo):
    def imprimir(self) -> str:
        return "Recibo do Banco B: Operação concluída com sucesso."
