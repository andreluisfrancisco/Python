## Módulo CaixaEletronicoFactory

Este módulo define a classe CaixaEletronicoFactory, que utiliza o padrão Abstract Factory para criar instâncias de
diferentes componentes do caixa eletrônico, com base no banco selecionado (Banco A, Banco B, etc.). O objetivo desta
factory é fornecer uma interface para criar objetos relacionados, como a interface do usuário, o recibo e a transação,
de forma centralizada e consistente.

## Classes

    CaixaEletronicoFactory: Classe responsável pela criação de componentes específicos para o sistema de caixa eletrônico
    com base no banco selecionado.

## Métodos

    criar_interface_usuario(banco: str): Retorna uma instância da interface de usuário específica para o banco fornecido.
    criar_recibo(banco: str): Retorna uma instância do recibo específico para o banco fornecido.
    criar_transacao(banco: str): Retorna uma instância de transação específica para o banco fornecido.
    
## Exceções

    ValueError: Lançada se o banco fornecido não for reconhecido ("A" ou "B").