from ..data_structures.lista_seq import Lista_Seq
from ..models.book import Book

class BubbleSort:
    '''Classe que implementa o algoritmo de ordenação Bubble Sort'''
    def ordenar(self, lista: Lista_Seq) -> Lista_Seq:
        tamanho = lista.size()
        for i in range(tamanho):
            for j in range(0, tamanho - i - 1):
                livro_atual: Book = lista._array_interno[j]
                proximo_livro: Book = lista._array_interno[j + 1]
                if livro_atual.titulo.lower() > proximo_livro.titulo.lower():
                    lista._array_interno[j], lista._array_interno[j + 1] = proximo_livro, livro_atual
        return lista
