class Cliente:

    def __init__(self, cpf: str):
        self.cpf = cpf
        self.nome = str()
        self.endereco = str()

    def setCpf(self, cpf: str):
        self.cpf = cpf

    def setNome(self, nome: str):
        self.nome = nome

    def setEndereco(self, endereco: str):
        self.endereco = endereco

    def getCpf(self):
        return self.cpf

    def getNome(self):
        return self.nome

    def getEndereco(self):
        return self.endereco

    def imprimir(self):
        return print('Nome', self.nome, 'Endereço', self.endereco)
