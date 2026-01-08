from models.despesa import Despesa
from models.receita import Receita
from models.alerta import Alerta


class OrcamentoMensal:
    def __init__(self, mes: int, ano: int):
        self.mes = mes
        self.ano = ano
        self.lista_lancamentos = []
        self.saldo_consolidado = 0
        self.alertas = []


    def adicionar_lancamento(self, lancamento):
        self.lista_lancamentos.append(lancamento)
        self.calcular_totais()

    
    def calcular_totais(self):
        total_receitas = sum(i.valor for i in self.lista_lancamentos if isinstance(i, Receita))
        total_despesas = sum(i.valor for i in self.lista_lancamentos if isinstance(i, Despesa))
        self.saldo_consolidado = total_receitas - total_despesas

        if self.saldo_consolidado < 0:
            self.alertas.append(
                Alerta(
                    mensagem="Saldo mensal negativo.",
                    tipo_alerta="DEFICIT_ORCAMENTARIO",
                    objeto_associado=self
                )
            )

    
    def verificar_deficit(self):
        return self.saldo_consolidado < 0
    

    def obter_extrato(self):
        return sorted(self.lista_lancamentos)
        