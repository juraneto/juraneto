import datetime


class Operacao:

    def __init__(self, cpf: str, codigo: int):
        self.data = datetime.date()
        self.cpf = cpf
        self.codigo = codigo
        self.ativo = bool()


    def setData(self, data: datetime):
        self.data = data


    def setCpf(self, cpf: str):
        self.cpf = cpf


    def setCodigo(self, codigo: int):
        self.codigo = codigo


    def setAtivo(self, ativo: bool):
        self.ativo = ativo


    def getData(self):
        return self.data


    def getCpf(self):
        return self.cpf


    def getCodigo(self):
        return self.codigo


    def isAtivo(self):
        return bool(self.ativo)
