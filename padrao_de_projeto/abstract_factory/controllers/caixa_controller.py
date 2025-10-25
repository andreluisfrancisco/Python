from views.interface_usuario import BaseInterfaceUsuario
from views.recibo import BaseRecibo
from models.transacao import BaseTransacao

class CaixaController:
    def __init__(self, interface_usuario: BaseInterfaceUsuario, recibo: BaseRecibo, transacao: BaseTransacao):
        self.interface_usuario = interface_usuario
        self.recibo = recibo
        self.transacao = transacao

    def iniciar(self):
        print(self.interface_usuario.mostrar_opcoes())
        print(self.transacao.processar())
        print(self.recibo.imprimir())
