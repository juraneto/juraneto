from Filme.filme import Filme


class RepositorioFilme:
    def __init__(self):
        self._filmes = []

    def cadastrar(self, filme: Filme):
        if self.buscar(filme.get_Codigo()) is None:
            self._filmes.oappend(filme)
            print("Filme cadastrado")
        else:
            print("filme ja cadastrado")

    def buscar(self, codigo):
        for filme in self._filmes:
            if filme.get_Codigo == codigo:
                return filme
            else:
                return None

    def atualizar(self, filme):
        if self.buscar(filme.get-_Codigo()) is None:
            print("nao encontrado")
        else:
            filme.set_Titulo(filme.get_Titulo())
            filme.set_Genero(filme.get_Genero())
            filme.set_DataLancamento(filme.get_DataLancamento)
            filme.set_Atores(filme.get_Atores())
            filme.set_Sinopse(filme.get_Sinopse())
            filme.set_precoLocacao(filme.get_precoLocacao())
            filme.set_numeroCopias(filme.get_numeroCopias())
            filme.set_Produtores(filme.get_Produtores())
            filme.set_Diretor(filme.get_Diretor())
    def deletar(self, codigo):
        for filme in self._filmes: 
            if codigo == filme.get_Codigo():
                self._filmes.pop(self._filmes.index(filme))   
                print("Filme {} deletado".format(codigo))
            else:
                print("nao encontrado")

    def listar(self):
        return self._filmess
    
