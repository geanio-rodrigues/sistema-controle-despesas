from datetime import datetime


class Alerta:
    def __init__(self, mensagem: str, tipo_alerta: str, objeto_associado = None):
        self.mensagem = mensagem
        self.tipo_alerta = tipo_alerta
        self.data_geracao = datetime.now()
        self.objeto_associado = objeto_associado


    def __str__(self):
        return f"[{self.tipo_alerta}] {self.mensagem} - {self.data_geracao}"
    

    def exibir_detalhes(self):
        return {
            "mensagem": self.mensagem,
            "tipo": self.tipo_alerta,
            "data": self.data_geracao,
            "objeto": str(self.objeto_associado)
        }