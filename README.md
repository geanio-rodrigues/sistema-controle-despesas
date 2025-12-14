# 📊 Sistema de Controle Financeiro

Este projeto implementa um sistema de gerenciamento financeiro orientado a objetos, focado em controle orçamentário, categorização de lançamentos e geração de relatórios analíticos.

---

## 🏗️ Arquitetura e Classes

Abaixo estão detalhadas as responsabilidades, atributos e métodos das classes que compõem o núcleo do sistema.

### Classes Principais:

#### `Lancamento` (Classe Base)
Classe abstrata que representa qualquer movimentação financeira, garantindo atributos comuns e validações de tipos e valores positivos.
- **Atributos:** `id`, `valor` (encapsulado), `data`, `descricao`, `categoria`, `forma_pagamento`.
- **Métodos:** `@valor.setter` (validação), `__str__` (resumo), `__lt__` (ordenação por data), `__eq__` (comparação).

#### `Receita`
Especialização de Lançamento para entradas de valores, permitindo somas diretas entre objetos deste tipo.
- **Atributos:** Herda de `Lancamento`.
- **Métodos:** `__init__` (valida tipo de categoria), `__add__` (soma de receitas).

#### `Despesa`
Especialização de Lançamento para saídas, com lógica de verificação de limites configurados e alertas de alto valor.
- **Atributos:** Herda de `Lancamento`.
- **Métodos:** `__init__`, `verificar_limite_categoria`, `verificar_alto_gasto`, `__add__` (soma de despesas).

#### `Categoria`
Define o agrupamento dos lançamentos, controlando o tipo (receita/despesa) e o teto de gastos mensais.
- **Atributos:** `nome`, `tipo`, `limite_mensal` (encapsulado), `descricao`.
- **Métodos:** `@limite_mensal.setter`, `validar_limite`, `__str__`, `__eq__`.

#### `OrcamentoMensal`
Classe agregadora que gerencia todos os lançamentos de um mês específico, calculando saldos e identificando déficits.
- **Atributos:** `mes`, `ano`, `lista_lancamentos`, `saldo_consolidado`.
- **Métodos:** `adicionar_lancamento`, `calcular_totais`, `verificar_deficit`, `obter_extrato`.

#### `Alerta`
Representa notificações do sistema geradas por violações de regras de negócio (limites estourados ou saldo negativo).
- **Atributos:** `mensagem`, `tipo_alerta`, `data_geracao`, `objeto_associado`.
- **Métodos:** `__str__` (formatação para log/tela), `exibir_detalhes`.

#### `Persistencia`
Responsável pela camada de dados, convertendo os objetos em registros (JSON ou SQLite) e vice-versa.
- **Atributos:** `caminho_arquivo`, `formato`.
- **Métodos:** `salvar_tudo`, `carregar_categorias`, `carregar_orcamentos`.

#### `Relatorio`
Classe utilitária para processamento estatístico e geração de visões analíticas sobre os dados financeiros.
- **Atributos:** Nenhum (classe de serviço).
- **Métodos:** `total_por_categoria`, `percentual_gastos`, `comparativo_trimestral`, `mes_mais_economico`.

---

# 👤 Autor

- **Geanio Marcio Basilio Rodrigues | *Matrícula: 2023011976*** 