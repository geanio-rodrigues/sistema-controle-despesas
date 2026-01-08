from models.lancamento import Lancamento


class Receita(Lancamento):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.categoria.tipo != "RECEITA":
            raise ValueError("Categoria inválida para Receita.")

    
    def __add__(self, value):
        if not isinstance(value, Receita):
            raise TypeError("Só é possível somar receitas.")
        return self.valor + value.valor
    