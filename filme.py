import datetime


class Filme:

    def __init__(self, codigo: int, titulo: str):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = []
        self.datalancamento = str()
        self.diretor = str()
        self.atores = []
        self.sinopse = str()
        self.produtores = []
        self.precolocacao = float()
        self.numerocopias = int()

    def setCodigo(self, codigo: int):
        self.codigo = codigo

    def setTitulo(self, titulo: str):
        self.titulo = titulo

    def setGenero(self, genero):
        self.genero = genero

    def setdatalancamento(self, datalancamento: str):
        self.datalancamento = datalancamento

    def setDiretor(self, diretor: str):
        self.diretor = diretor

    def setAtores(self, atores):
        self.atores = atores

    def setSinopse(self, sinopse: str):
        self.sinopse = sinopse

    def setProdutores(self, produtores):
        self.produtores = produtores

    def setprecolocacao(self, precolocacao: float):
        self.precolocacao = precolocacao


    def setnumerocopias(self, numerocopias: int):
        self.numerocopias = numerocopias


    def getCodigo(self):
        return self.codigo


    def getTitulo(self):
        return self.titulo


    def getGenero(self):
        return self.genero


    def getdatalancamento(self):
        return self.datalancamento


    def getDiretor(self):
        return self.diretor


    def getAtores(self):
        return self.atores


    def getSinopse(self):
        return self.sinopse


    def getProdutores(self):
        return self.produtores


    def getPrecoLocacao(self):
        return self.precolocacao


    def getnumerocopias(self):
        return self.numerocopias


    def addGenero(self, genero: str):
        self.genero += genero


    def addAtor(self, ator):
        self.atores += ator


    def addProdutor(self, produtor: str):
        self.produtores += produtor


    def imprimir(self):
        return print('código', self.codigo, 'filme', self.titulo, 'gênero', self.genero, 'data de lançamento',
                     self.datalancamento,
                     'atores', self.atores, 'diretor', self.diretor, 'sinopse', self.sinopse)
