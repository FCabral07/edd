from ..data_structures.lista_seq import Lista_Seq
from ..models.book import Book

class SelectionSort:
    '''Classe que implementa o algoritmo de ordenação Selection Sort'''
    def ordem_alfabetica(self, lista: Lista_Seq) -> int:
        menor_indice = 0
        # Vai de 1 até o tamanho da lista, ignorando o primeiro elemento pois já está acima
        for i in range(1, lista.size()):
            # Compara o titulo do livro atual com o menor indice
            if lista._array_interno[i].titulo.lower() < lista._array_interno[menor_indice].titulo.lower():
                menor_indice = i
        return menor_indice
    
    def ordenar(self, lista: Lista_Seq) -> Lista_Seq:
        novo_array = Lista_Seq()
        for i in range(lista.size()):
            menor_indice = self.ordem_alfabetica(lista)
            novo_array.add(lista.remove(menor_indice))
        return novo_array
