from abc import ABC, abstractmethod
from datetime import date


class Lancamento(ABC):
    def __init__(self, id: int, valor: float, data: date, descricao: str, categoria, forma_pagamento: str):
        self.id = id
        self.valor = valor
        self.data = data
        self.descricao = descricao
        self.categoria = categoria
        self.forma_pagamento = forma_pagamento

    
    @property
    def valor(self):
        return self._valor
    

    @valor.setter
    def valor(self, valor: float):
        if valor <= 0:
            raise ValueError("O valor do lançamento deve ser positivo.")
        self._valor = valor

    
    def __str__(self):
        return f"{self.data} | {self.descricao} | R$ {self.valor:.2f}"


    def __eq__(self, value):
        if not isinstance(value, Lancamento):
            return False
        return self.id == value.id
    

    def __lt__(self, value):
        return self.data < value.data
    