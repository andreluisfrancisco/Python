# Sistema de Caixa Eletrônico – Padrão Abstract Factory

Este projeto demonstra o uso do **padrão de projeto Abstract Factory** aplicado a um sistema de **Caixa Eletrônico (ATM)**.  
A proposta é apresentar uma arquitetura modular, clara e extensível para aprendizado de **Padrões de Projeto em Python** e boas práticas de **orientação a objetos, abstração e polimorfismo**.

---

## Visão Geral

O sistema simula o funcionamento básico de um caixa eletrônico que pode operar para **diferentes bancos (A e B)**.  
Cada banco possui sua própria **interface de usuário**, **recibo** e **transação**, criados dinamicamente pela **Abstract Factory**, garantindo baixo acoplamento e alta coesão entre os componentes.

---

## Estrutura dos Módulos

### 1. Módulo Principal (`main.py`)

Responsável por inicializar o sistema, escolher o banco e coordenar a execução dos componentes.

**Função principal:**  
`main()` – Cria a factory de componentes conforme o banco selecionado, instancia interface, transação e recibo, e inicia o controlador.

**Como usar:**
1. Defina o banco desejado alterando a variável `banco_escolhido` (`"A"` ou `"B"`).
2. Execute o programa com:
   ```bash
   python main.py
   ```
3. O sistema exibirá a interface do banco selecionado, processará a transação e imprimirá o recibo correspondente.

---

### 2. Módulo `recibo.py`

Define a estrutura e comportamento dos **recibos** emitidos após cada transação.

**Classes:**
- `BaseRecibo`: Classe abstrata que define o contrato obrigatório para as subclasses.
- `ReciboBancoA` / `ReciboBancoB`: Implementações específicas de recibos para cada banco.

**Exceções:**
- `NotImplementedError`: Lançada caso uma subclasse não implemente o método obrigatório.

---

### 3. Módulo `interface_usuario.py`

Define as **interfaces de interação com o usuário**, variando conforme o banco.

**Classes:**
- `BaseInterfaceUsuario`: Classe abstrata com o método obrigatório `obrigatorio()`.
- `InterfaceUsuarioBancoA` / `InterfaceUsuarioBancoB`: Implementações das interfaces específicas.

**Métodos principais:**
- `mostrar_opcoes()`: Exibe as opções de operação do caixa eletrônico.

---

### 4. Módulo `transacao.py`

Implementa a lógica das **transações bancárias**.

**Classes:**
- `BaseTransacao`: Classe abstrata que define o método obrigatório `obrigatorio()`.
- `TransacaoBancoA` / `TransacaoBancoB`: Classes concretas que processam as operações para cada banco.

**Métodos principais:**
- `processar()`: Realiza o processamento da transação bancária.

---

### 5. Módulo `controllers/caixa_controller.py`

Atua como o **controlador principal** do sistema, integrando interface, transação e recibo.

**Classe:**
- `CaixaController`: Orquestra o fluxo completo da operação de um caixa eletrônico.

**Métodos principais:**
- `iniciar()`: Exibe opções, executa a transação e imprime o recibo.

---

## Conceitos Demonstrados

- **Padrão Abstract Factory:** Criação de famílias de objetos relacionados sem acoplamento direto às classes concretas.
- **Abstração e Polimorfismo:** Uso de classes base e métodos obrigatórios para garantir consistência entre implementações.
- **Separação de Responsabilidades (SoC):** Cada módulo trata de uma função específica dentro do sistema.
- **Extensibilidade:** Adicionar um novo banco exige apenas a criação de novas subclasses.
