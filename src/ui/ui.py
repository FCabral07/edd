import flet as ft
from src.data_structures.lista_seq import Lista_Seq
from src.models.book import Book
from src.sorting_algorithms.bubble_sort import BubbleSort

class BibliotecaDigitalUI:
    def __init__(self):
        self.lista_livros = Lista_Seq()
        self.bubble_sort = BubbleSort()

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
            # Garantindo que os campos não estejam vazios
            if not titulo.value or not autor.value or not ano.value or not genero.value:
                page.snack_bar = ft.SnackBar(content=ft.Text("Por favor, preencha todos os campos."))
                page.snack_bar.open = True
                page.update()
                return

            # Criando o novo livro
            novo_livro = Book(titulo.value, autor.value, int(ano.value), genero.value)
            self.lista_livros.add(novo_livro)

            # Fechando o popup e exibindo uma mensagem de sucesso
            page.dialog.open = False
            page.snack_bar = ft.SnackBar(content=ft.Text("Livro adicionado com sucesso!"))
            page.snack_bar.open = True

            # Atualizando a página
            page.update()

        # Popup para remover último livro
        def remover_livro_popup(e):
            # Verificando se há livros na lista
            if self.lista_livros.size() > 0:
                # Removendo o último livro
                self.lista_livros.remove()

                # Exibindo uma mensagem de sucesso
                page.snack_bar = ft.SnackBar(content=ft.Text("Último livro removido com sucesso!"))
                page.snack_bar.open = True

                # Atualizando a página
                page.update()
            else:
                # Exibindo uma mensagem de erro
                page.snack_bar = ft.SnackBar(content=ft.Text("Não há livros para remover."))
                page.snack_bar.open = True

                # Atualizando a página
                page.update()

        # Popup para listar livros
        def listar_livros_popup(e):
            # Criando uma lista de livros
            lista = ft.Column()
            for i in range(self.lista_livros.size()):
                # Obtendo o livro atual
                livro = self.lista_livros._array_interno[i]

                # Adicionando o livro à lista
                lista.controls.append(ft.Container(
                    content=ft.Text(f"{livro.titulo} - {livro.autor}"),
                    padding=10,
                    margin=5,
                    border=ft.border.all(1, ft.colors.BLUE_200),
                    border_radius=ft.border_radius.all(5)
                ))
            conteudo = ft.Column([
                ft.Text("Lista de Livros", size=20, weight=ft.FontWeight.BOLD),
                lista
            ])
            abrir_popup(conteudo)

        # Popup para buscar livro
        def buscar_livro_popup(e):
            # Retornando o conteúdo da busca de livros
            conteudo = ft.Column([
                ft.Text("Buscar Livro", size=20, weight=ft.FontWeight.BOLD),
                busca := ft.TextField(label="Livro ou Autor a ser buscado", border=ft.InputBorder.UNDERLINE),
                ft.ElevatedButton("Buscar", on_click=lambda _: buscar_livro(busca), style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.BLUE_600))
            ])

            # Abrindo o popup com o conteúdo
            abrir_popup(conteudo)

        # Função para buscar livro
        def buscar_livro(busca):
            # Obtendo o valor de busca e colocando em minúsculo
            termo = busca.value.lower()
            resultados = ft.Column()

            # Iterando sobre a lista de livros e verificando se o termo de busca está no título ou autor
            for i in range(self.lista_livros.size()):
                livro = self.lista_livros._array_interno[i]
                if termo in livro.titulo.lower() or termo in livro.autor.lower():
                    resultados.controls.append(ft.Container(
                        content=ft.Text(f"{livro.titulo} - {livro.autor}"),
                        padding=10,
                        margin=5,
                        border=ft.border.all(1, ft.colors.BLUE_200),
                        border_radius=ft.border_radius.all(5)
                    ))
            conteudo = ft.Column([
                ft.Text("Resultados da Busca", size=20, weight=ft.FontWeight.BOLD),
                resultados
            ])
            abrir_popup(conteudo)

        # Popup para ordenar livros
        def ordenar_livros_popup(e):
            # Ordenando a lista de livros
            self.lista_livros = self.bubble_sort.ordenar(self.lista_livros)

            # Exibindo uma mensagem de sucesso
            page.snack_bar = ft.SnackBar(content=ft.Text("Livros ordenados com sucesso!"))
            page.snack_bar.open = True
            page.update()

        # Interface da Biblioteca Digital
        page.add(
            ft.Container(
                content=ft.Column([
                    ft.Text("Biblioteca Digital", size=40, weight=ft.FontWeight.BOLD, color=ft.colors.with_opacity(0.5, "#e2725b")),
                    ft.ElevatedButton("Adicionar Livro", on_click=adicionar_livro_popup, style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.with_opacity(0.7, "#e2725b"))),
                    ft.ElevatedButton("Remover Último Livro", on_click=remover_livro_popup, style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.with_opacity(0.7, "#e2725b"))),
                    ft.ElevatedButton("Listar Livros", on_click=listar_livros_popup, style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.with_opacity(0.7, "#e2725b"))),
                    ft.ElevatedButton("Buscar Livro", on_click=buscar_livro_popup, style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.with_opacity(0.7, "#e2725b"))),
                    ft.ElevatedButton("Ordenar Livros", on_click=ordenar_livros_popup, style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.with_opacity(0.7, "#e2725b")))
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                padding=50,
                bgcolor=ft.colors.BLUE_GREY_800,
                border_radius=ft.border_radius.all(20),
                alignment=ft.alignment.center
            )
        )
