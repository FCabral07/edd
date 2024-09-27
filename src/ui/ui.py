import flet as ft
from src.data_structures.arvore import Node
from src.models.book import Book
# from src.sorting_algorithms.bubble_sort import BubbleSort

class BibliotecaDigitalUI:
    def __init__(self):
        self.arvore_livros = None
        # self.bubble_sort = BubbleSort()

    def main(self, page: ft.Page):
        page.title = "Biblioteca Digital"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.padding = 50
        page.bgcolor = ft.colors.with_opacity(0.8, "#FFFDD0")

        # Funções POPUP
        def fechar_popup(e):
            page.dialog.open = False
            page.update()

        def abrir_popup(conteudo):
            popup = ft.AlertDialog(
                content=conteudo,
                bgcolor= ft.colors.BLUE_GREY_900,
                actions=[
                    ft.TextButton("Fechar", on_click=fechar_popup, style= ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.with_opacity(0.7, "#e2725b")))
                ]
            )
            page.dialog = popup
            popup.open = True
            page.update()

        # Popup para adicionar livro
        def adicionar_livro_popup(e):
            conteudo = ft.Column([
                ft.Text("Adicionar Livro", size=20, weight=ft.FontWeight.BOLD),
                titulo := ft.TextField(label="Título", border=ft.InputBorder.UNDERLINE),
                autor := ft.TextField(label="Autor", border=ft.InputBorder.UNDERLINE),
                ano := ft.TextField(label="Ano de Publicação", border=ft.InputBorder.UNDERLINE),
                genero := ft.TextField(label="Gênero", border=ft.InputBorder.UNDERLINE),
                ft.ElevatedButton("Adicionar", on_click=lambda _: adicionar_livro(titulo, autor, ano, genero), style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.with_opacity(0.3, ft.colors.BLUE_300)))
            ])
            abrir_popup(conteudo)

        # Função para adicionar livro
        def adicionar_livro(titulo, autor, ano, genero):
            try:
                novo_livro = Book(titulo.value, autor.value, int(ano.value), genero.value)
                
                # Testando se a arvore esta vazia antes de adicionar o livro
                if self.arvore_livros is None:
                    self.arvore_livros = Node(novo_livro)
                else:
                    self.arvore_livros = self.arvore_livros.inserir(novo_livro, self.arvore_livros)

                # Limpando os campos de entrada após adicionar o livro
                titulo.value = ""
                autor.value = ""
                ano.value = ""
                genero.value = ""
                
                # Funçõpes da GUI
                page.dialog.open = False
                
                page.snack_bar = ft.SnackBar(content=ft.Text("Livro adicionado com sucesso!"))
                page.snack_bar.open = True
                page.update()
            # Tratamento do erro (estou cansado de erros, por favor não entre aqui)    
            except ValueError:
                page.snack_bar = ft.SnackBar(content=ft.Text("Erro ao adicionar o livro. Verifique os dados inseridos."))
                page.snack_bar.open = True
                page.update()

        # Popup para remover último livro
        def remover_livro_popup(e):
            conteudo = ft.Column([
                ft.Text("Remover Livro", size=20, weight=ft.FontWeight.BOLD),
                titulo := ft.TextField(label="Título do livro a ser removido", border=ft.InputBorder.UNDERLINE),
                ft.ElevatedButton("Remover", on_click=lambda _: remover_livro(titulo), style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.BLUE_600))
            ])
            abrir_popup(conteudo)

        # Função para remover livro
        def remover_livro(titulo):
            if not titulo.value:
                page.snack_bar = ft.SnackBar(content=ft.Text("Por favor, insira o título do livro."))
                page.snack_bar.open = True
                page.update()
                return

            self.arvore_livros = self.arvore_livros.remover(titulo.value, self.arvore_livros)

            page.dialog.open = False
            page.snack_bar = ft.SnackBar(content=ft.Text("Livro removido com sucesso!"))
            page.snack_bar.open = True
            page.update()

        # Popup para listar livros
        def listar_livros_popup(e):
            lista = ft.Column()
            def adicionar_livro_lista(node):
                if node is not None:
                    adicionar_livro_lista(node.esquerda)
                    lista.controls.append(ft.Container(
                        content=ft.Text(f"{node.valor.titulo} - {node.valor.autor}"),
                        padding=10,
                        margin=5,
                        border=ft.border.all(1, ft.colors.BLUE_200),
                        border_radius=ft.border_radius.all(5)
                    ))
                    adicionar_livro_lista(node.direita)

            adicionar_livro_lista(self.arvore_livros)
            conteudo = ft.Column([
                ft.Text("Lista de Livros", size=20, weight=ft.FontWeight.BOLD),
                lista
            ])
            abrir_popup(conteudo)

        # Popup para buscar livro
        def buscar_livro_popup(e):
            conteudo = ft.Column([
                ft.Text("Buscar Livro", size=20, weight=ft.FontWeight.BOLD),
                busca := ft.TextField(label="Título do livro a ser buscado", border=ft.InputBorder.UNDERLINE),
                ft.ElevatedButton("Buscar", on_click=lambda _: buscar_livro(busca), style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.BLUE_600))
            ])
            abrir_popup(conteudo)

        # Função para buscar livro
        def buscar_livro(busca):
            livro = self.arvore_livros.buscar(busca.value, self.arvore_livros)
            if livro:
                conteudo = ft.Column([
                    ft.Text("Livro Encontrado", size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Título: {livro.titulo}"),
                    ft.Text(f"Autor: {livro.autor}"),
                    ft.Text(f"Ano: {livro.ano_publicacao}"),
                    ft.Text(f"Gênero: {livro.genero}")
                ])
            else:
                conteudo = ft.Text("Livro não encontrado", size=20, weight=ft.FontWeight.BOLD)
            abrir_popup(conteudo)

        # Popup para ordenar livros
        # def ordenar_livros_popup(e):
        #     # Ordenando a lista de livros
        #     self.lista_livros = self.bubble_sort.ordenar(self.lista_livros)

        #     # Exibindo uma mensagem de sucesso
        #     page.snack_bar = ft.SnackBar(content=ft.Text("Livros ordenados com sucesso!"))
        #     page.snack_bar.open = True
        #     page.update()

        # Interface da Biblioteca Digital
        page.add(
            ft.Container(
                content=ft.Column([
                    ft.Text("Biblioteca Digital", size=40, weight=ft.FontWeight.BOLD, color=ft.colors.with_opacity(0.5, "#e2725b")),
                    ft.ElevatedButton("Adicionar Livro", on_click=adicionar_livro_popup, style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.with_opacity(0.7, "#e2725b"))),
                    ft.ElevatedButton("Remover Livro", on_click=remover_livro_popup, style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.with_opacity(0.7, "#e2725b"))),
                    ft.ElevatedButton("Listar Livros", on_click=listar_livros_popup, style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.with_opacity(0.7, "#e2725b"))),
                    ft.ElevatedButton("Buscar Livro", on_click=buscar_livro_popup, style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.with_opacity(0.7, "#e2725b"))),
                    # ft.ElevatedButton("Ordenar Livros", on_click=ordenar_livros_popup, style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.with_opacity(0.7, "#e2725b")))
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                padding=50,
                bgcolor=ft.colors.BLUE_GREY_800,
                border_radius=ft.border_radius.all(20),
                alignment=ft.alignment.center
            )
        )
