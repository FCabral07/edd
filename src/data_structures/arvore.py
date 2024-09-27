from __future__ import annotations

from src.models import book
import unittest

class Node:
    _direita: Node = None
    _esquerda: Node = None
    _valor: book.Book = None

    # Inicialização da classe com os esquerda e direita como valores opcionais a serem passados
    def __init__(self, valor: book.Book, esquerda: Node = None, direita: Node = None):
        self._valor = valor
        self._esquerda = esquerda
        self._direita = direita

    def setNull(self) -> None:
        self._esquerda = None
        self._direita = None
        self._valor = None

    # Inserção de um novo nó na árvore
    def inserir(self, valor: book.Book, node: Node) -> Node:
        # Verifica se o nó é nulo
        if node is None:
            # Se o nó é nulo, cria um novo nó com o valor
            return Node(valor)
        
        # Se o título do livro for menor que o título do nó, ele vai para a esquerda
        if valor.titulo < node.valor.titulo:
            node.esquerda = self.inserir(valor, node.esquerda)
        # Se o título do livro for maior que o título do nó, ele vai para a direita
        elif valor.titulo > node.valor.titulo:
            node.direita = self.inserir(valor, node.direita)
        # Se o título for igual, não fazemos nada (evitamos duplicatas)
        
        return node
    
    def buscar(self, titulo: str, node: Node) -> book.Book:
        if node is None or node.valor.titulo == titulo:
            return node.valor if node else None
        
        if titulo < node.valor.titulo:
            return self.buscar(titulo, node.esquerda)
        else:
            return self.buscar(titulo, node.direita)
    
    # Método para remover um nó da árvore
    def remover(self, titulo: str, node: Node) -> Node:
        if node is None:
            print('A árvore está vazia')
            return node
        
        if titulo < node.valor.titulo:
            node.esquerda = self.remover(titulo, node.esquerda)
        elif titulo > node.valor.titulo:
            node.direita = self.remover(titulo, node.direita)
        else:
            if node.esquerda is None and node.direita is None:
                return None
            elif node.esquerda is None:
                return node.direita
            elif node.direita is None:
                return node.esquerda
            else:
                sucessor = self.encontraMenor(node.direita)
                node.valor = sucessor.valor
                node.direita = self.remover(sucessor.valor.titulo, node.direita)
        
        return node

    # Método para encontrar o menor valor da árvore
    def encontraMenor(self, node: Node) -> Node:
        atual = node
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual
    
    # Método para remover o menor valor da árvore
    def removeMenor(self, node: Node) -> Node:
        if node.esquerda is None:
            return node.direita
        else:
            node.esquerda = self.removeMenor(node.esquerda)
            return node
    
    # Métodos de impressão da árvore
    def emOrdem(self, node: Node) -> None:
        if node is not None:
            self.emOrdem(node.esquerda)
            print(f"Título: {node.valor.titulo}", end=" ")
            self.emOrdem(node.direita)

    def preOrdem(self, node: Node) -> None:
        if node is not None:
            print(f"Título: {node.valor.titulo}", end=" ")
            self.preOrdem(node.esquerda)
            self.preOrdem(node.direita)

    def posOrdem(self, node: Node) -> None:
        if node is not None:
            self.posOrdem(node.esquerda)
            self.posOrdem(node.direita)
            print(f"Título: {node.valor.titulo}", end=" ")

    # Getters e Setters para os atributos da classe
    @property
    def valor(self) -> book.Book:
        return self._valor
    
    @valor.setter
    def valor(self, valor: book.Book) -> None:
        self._valor = valor
    
    @property
    def esquerda(self) -> Node:
        return self._esquerda
    
    @esquerda.setter
    def esquerda(self, esquerda: Node) -> None:
        self._esquerda = esquerda
    
    @property
    def direita(self) -> Node:
        return self._direita
    
    @direita.setter
    def direita(self, direita: Node) -> None:
        self._direita = direita
