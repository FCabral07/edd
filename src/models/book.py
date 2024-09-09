from typing import Dict

class Book:
    '''Classe que representa os livros, com: Título, Autor, Ano de Publicação, Gênero'''
    def __init__(self, titulo: str, autor: str, ano_publicacao: int, genero: str):
        self.titulo: str = titulo
        self.autor: str = autor
        self.ano_publicacao: int = ano_publicacao
        self.genero: str = genero

    def return_info(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "ano_publicacao": self.ano_publicacao,
            "genero": self.genero
        }