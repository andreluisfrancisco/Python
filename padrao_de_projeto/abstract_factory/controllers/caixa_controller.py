"""
Módulo CaixaController.

Este módulo define a classe CaixaController, que atua como o controlador principal do sistema de caixa eletrônico,
orquestrando a interação entre a interface do usuário, o processamento de transações e a geração de recibos. O 
CaixaController utiliza o padrão Abstract Factory para criar componentes específicos de diferentes bancos (Banco A, Banco B, etc.).

Classes:
    CaixaController: Classe responsável por coordenar as operações do caixa eletrônico.

Atributos:
    interface_usuario (BaseInterfaceUsuario): Instância da interface de usuário específica de um banco.
    recibo (BaseRecibo): Instância do recibo específico de um banco.
    transacao (BaseTransacao): Instância de transação específica de um banco.

Métodos:
    iniciar(): Inicia o fluxo de operação do caixa eletrônico, exibindo as opções da interface do usuário, 
               processando a transação e imprimindo o recibo.
"""

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
