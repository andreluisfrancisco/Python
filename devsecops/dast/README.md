# Varredura de Segurança com ZAPv2

Este módulo é responsável por realizar varreduras de segurança em aplicações web utilizando a ferramenta **ZAPv2** (Zed Attack Proxy). O código executa uma varredura completa em um URL especificado, incluindo uma spider e uma varredura ativa, e exibe os resultados de segurança encontrados.

## Funcionalidades

- Inicia uma spider no URL especificado para explorar o aplicativo.
- Realiza uma varredura ativa para identificar vulnerabilidades.
- Coleta e exibe alertas de segurança encontrados, incluindo descrição, gravidade e recomendações.

## Pré-requisitos

Antes de executar o código, você precisa garantir que:

1. O [ZAPv2](https://www.zaproxy.org/download/) está instalado e em execução.
2. A API do ZAP está habilitada e a chave da API (`api_key`) está configurada.
3. As bibliotecas necessárias estão instaladas, especialmente `python-owasp-zap`:

pip install python-owasp-zap
