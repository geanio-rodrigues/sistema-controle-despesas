from models.lancamento import Lancamento
from models.alerta import Alerta


class Despesa(Lancamento):
    LIMITE_ALTO_GASTO = 500.0


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.categoria.tipo != "DESPESA":
            raise ValueError("Categoria inválida para Despesa.")

    
    def verificar_limite_categoria(self, total_categoria: float):
        if self.categoria.validar_limite(total_categoria):
            return Alerta(
                mensagem="Limite da categoria excedido.",
                tipo_alerta="LIMITE CATEGORIA",
                objeto_associado=self
            )
        return None
    

    def verificar_alto_gasto(self):
        if self.valor >= self.LIMITE_ALTO_GASTO:
            return Alerta(
                mensagem="Despesa de alto valor",
                tipo_alerta="ALTO VALOR",
                objeto_associado=self
            )
        return None
    

    def __add__(self, value):
        if not isinstance(value, Despesa):
            raise TypeError("Só é possível somar despesas.")
        return self.valor + value.valor
    