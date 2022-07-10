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
    def atualizar(self, cliente: Cliente):
            if self.buscar(cliente.get_Cpf()) is None:
                print("Cliente não se encontra")
            else:
                cliente.set_Nome(cliente.get_Nome())
                cliente.set_Endereco(cliente.get_Endereco())
    def deletar(self, cpf: str):
            if self.buscar(cpf) is None:
                print("Cliente não se encontra")
            else:
                self._clientes.pop()
                print("Cliente apagado")
    def listar(self): 
          return self._clientes
 
