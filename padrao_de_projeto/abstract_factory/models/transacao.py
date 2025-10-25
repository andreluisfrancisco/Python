class BaseTransacao:
    def obrigatorio(self):
        raise NotImplementedError("Este método deve ser implementado pela subclasse.")

class TransacaoBancoA(BaseTransacao):
    def processar(self) -> str:
        return "Transação processada no Banco A."

class TransacaoBancoB(BaseTransacao):
    def processar(self) -> str:
        return "Transação realizada no Banco B."
