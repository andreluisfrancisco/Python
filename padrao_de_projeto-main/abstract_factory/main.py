"""
Módulo Principal do Sistema de Caixa Eletrônico.

Este módulo contém a função `main`, que é responsável por inicializar o sistema de caixa eletrônico 
e coordenar a criação dos componentes de interface, recibo e transação de acordo com o banco escolhido.
O sistema utiliza o padrão Abstract Factory para gerar os componentes específicos para cada banco (A ou B).

Funções:
    main(): Função principal que inicializa a factory de componentes, cria os objetos de interface, recibo e transação 
    com base no banco selecionado, e inicia o controlador do caixa eletrônico para realizar as operações.

Dependências:
    controllers.caixa_controller: Controlador que gerencia o fluxo do caixa eletrônico.
    factory.caixa_eletronico_factory: Factory responsável por criar componentes específicos para cada banco.
    
Como usar:
    O banco pode ser escolhido alterando a variável `banco_escolhido`. Atualmente está configurado para "A", 
    mas pode ser alterado para "B". O script cria os componentes corretos com base nessa escolha e executa 
    as operações do caixa eletrônico.

Exemplo:
    Para executar o sistema de caixa eletrônico:
    
    1. Selecione o banco alterando a variável `banco_escolhido` ("A" ou "B").
    2. Execute o script com `python main.py`.

Se tudo estiver configurado corretamente, o sistema exibirá a interface do banco selecionado, processará uma transação, 
e imprimirá o recibo correspondente.
"""

from controllers.caixa_controller import CaixaController
from factory.caixa_eletronico_factory import CaixaEletronicoFactory

def main():
    fabrica = CaixaEletronicoFactory()

    # Escolhendo o banco (pode ser uma entrada de usuário, por exemplo)
    banco_escolhido = "A"  # ou "B"
    
    # Criando os componentes do caixa para o banco escolhido
    interface_usuario = fabrica.criar_interface_usuario(banco_escolhido)
    recibo = fabrica.criar_recibo(banco_escolhido)
    transacao = fabrica.criar_transacao(banco_escolhido)

    # Criando o controller e iniciando a operação
    controller = CaixaController(interface_usuario, recibo, transacao)
    controller.iniciar()

if __name__ == "__main__":
    main()
