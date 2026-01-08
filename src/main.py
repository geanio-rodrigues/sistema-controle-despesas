from datetime import date
from models.categoria import Categoria
from models.receita import Receita
from models.despesa import Despesa
from models.orcamento_mensal import OrcamentoMensal


salario = Categoria("Salário", "RECEITA")
alimentacao = Categoria("Alimentação", "DESPESA", limite_mensal=800)

orcamento = OrcamentoMensal(1, 2026)

r1 = Receita(1, 3000, date.today(), "Salário Janeiro", salario, "PIX")
d1 = Despesa(2, 600, date.today(), "Supermercado", alimentacao, "CRÉDITO")

orcamento.adicionar_lancamento(r1)
orcamento.adicionar_lancamento(d1)

print(orcamento.saldo_consolidado)

