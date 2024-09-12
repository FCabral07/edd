import flet as ft
from src.ui.ui import BibliotecaDigitalUI

if __name__ == "__main__":
    app = BibliotecaDigitalUI()
    ft.app(target=app.main)
