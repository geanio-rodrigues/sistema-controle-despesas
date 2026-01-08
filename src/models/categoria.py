class Categoria:
    def __init__(self, nome: str, tipo: str, limite_mensal: float = None, descricao: str = ""):
        self.nome = nome
        self.tipo = tipo.upper()
        self.descricao = descricao
        self.limite_mensal = limite_mensal

    
    @property
    def limite_mensal(self):
        return self._limite_mensal
    

    @limite_mensal.setter
    def limite_mensal(self, valor):
        if self.tipo == "RECEITA" and valor is not None:
            raise ValueError("Categorias de receita não possuem limite mensal.")
        if valor is not None and valor <= 0:
            raise ValueError("Limite mensal deve ser positivo.")
        self._limite_mensal = valor


    def validar_limite(self, total_gasto: float):
        if self.limite_mensal is None:
            return False    
        return total_gasto > self.limite_mensal
    

    def __str__(self):
        return f"{self.nome} ({self.tipo})"

    
    def __eq__(self, value):
        return self.nome == value.nome and self.tipo == value.tipo
    