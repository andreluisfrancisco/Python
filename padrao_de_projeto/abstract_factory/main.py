from controllers.caixa_controller import CaixaController
from factory.caixa_eletronico_factory import CaixaEletronicoFactory

def main():
    factory = CaixaEletronicoFactory()

    # Escolhendo o banco (pode ser uma entrada de usuário, por exemplo)
    banco_escolhido = "A"  # ou "B"
    
    # Criando os componentes do caixa para o banco escolhido
    interface_usuario = factory.criar_interface_usuario(banco_escolhido)
    recibo = factory.criar_recibo(banco_escolhido)
    transacao = factory.criar_transacao(banco_escolhido)

    # Criando o controller e iniciando a operação
    controller = CaixaController(interface_usuario, recibo, transacao)
    controller.iniciar()

if __name__ == "__main__":
    main()
