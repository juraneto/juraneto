from cliente import Cliente


class RepositorioCliente:

    def __init__(self):
        self.clientes = []

    def cadastrar(self, cliente: Cliente):
        if self.buscar(cliente.getCpf()) is None:
            self.clientes.append(cliente)
            print('cliente cadastrado')
        else:
            print('cliente ja existe')

    def buscar(self, cpf):
        for cliente in self.clientes:
            if cliente.getCpf() == cpf:
                return cliente
        return None
