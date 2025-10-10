# Listagem segura de diretórios em python

Este projeto demonstra uma vulnerabilidade comum de segurança em python (injeção de comandos), e como mitigá-la utilizando práticas seguras ao trabalhar com entrada de dados do usuário e comandos do sistema.

## Ferramenta utilizada para teste

Para identificar vulnerabilidades no código, utilizei a ferramenta [Bandit](https://bandit.readthedocs.io/en/latest/), que analisa códigos em python em busca de falhas de segurança.

### Instalação

pip install bandit

### Uso

bandit codigo_vulneravel.py

bandit codigo_nao_vulneravel.py