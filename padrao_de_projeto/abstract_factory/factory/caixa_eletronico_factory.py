from __future__ import annotations
from views.interface_usuario import InterfaceUsuarioBancoA, InterfaceUsuarioBancoB
from views.recibo import ReciboBancoA, ReciboBancoB
from models.transacao import TransacaoBancoA, TransacaoBancoB

class CaixaEletronicoFactory:
    """Classe responsável pela criação de componentes específicos para o caixa eletrônico."""

    def criar_interface_usuario(self, banco: str) -> InterfaceUsuarioBancoA | InterfaceUsuarioBancoB:
        """Retorna a interface de usuário específica para o banco fornecido."""
        if banco == "A":
            return InterfaceUsuarioBancoA()
        if banco == "B":
            return InterfaceUsuarioBancoB()
        raise ValueError("Banco desconhecido")

    def criar_recibo(self, banco: str) -> ReciboBancoA | ReciboBancoB:
        """Retorna o recibo específico para o banco fornecido."""
        if banco == "A":
            return ReciboBancoA()
        if banco == "B":
            return ReciboBancoB()
        raise ValueError("Banco desconhecido")

    def criar_transacao(self, banco: str) -> TransacaoBancoA | TransacaoBancoB:
        """Retorna a transação específica para o banco fornecido."""
        if banco == "A":
            return TransacaoBancoA()
        if banco == "B":
            return TransacaoBancoB()
        raise ValueError("Banco desconhecido")
    