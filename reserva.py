from operacao import Operacao


class Reserva(Operacao):

    def __init__(self, cpf: str, codigo: int):
        super().__init__(cpf, codigo)
        self.prioridade = int()

    def setPrioridade(self, prioridade: int):
        self.prioridade = prioridade

    def getPrioridade(self):
        return self.prioridade
