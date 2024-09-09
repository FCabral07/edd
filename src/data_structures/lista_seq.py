from ..models import book

class Lista_Seq:
    '''Classe que simula uma lista sequencial'''
    def __init__(self):
        self._alocacao_inicial: int = 3
        self._array_interno: list = [None] * self._alocacao_inicial
        self._inseridos: int = 0

    # Método que retorna o size da lista
    def size(self) -> int:
        return self._inseridos
    
    # Método para adicionar na lista
    def add(self, livro: book.Book) -> None:
        if self._isFull():
            self._redimensionar()

        self._array_interno[self._inseridos] = livro
        self._inseridos += 1

    # Método para limpar a lista
    def clear(self) -> None:
        self._inseridos: int = 0
        self._array_interno: list[book.Book] = [None] * self._alocacao_inicial

    # Printa os elementos da lista
    def listar(self) -> None:
        for i in range(self._inseridos):
            livro = self._array_interno[i]
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano de Publicação: {livro.ano_publicacao}, Gênero: {livro.genero}")

    # Método para remover da lista
    def remove(self) -> None:
        self._inseridos -= 1
        self._array_interno[self._inseridos] = None

    # Método para verificar se a lista está cheia
    def _isFull(self) -> bool:
        return self._inseridos == len(self._array_interno)
    
    # Método para redimensionar o tamanho da lista
    def _redimensionar(self):
        nova_alocacao = len(self._array_interno) * 2    # Novo tamanho da lista
        novoArray = [None] * nova_alocacao              # Nova lista

        for i in range(self._inseridos):                # Alocação dos itens do array antigo para o novo
            novoArray[i] = self._array_interno[i]

        self._array_interno = novoArray                 # Alocando o novo array para o lugar do antigo
