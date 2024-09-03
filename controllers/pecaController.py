from models.pecaModel import PecaModel
from flet import Page
import flet as ft
class PecaController:
    def __init__(self, page: Page):
        self.model = PecaModel()
        self.page = page

    def adicionar_peca(self, titulo, roteiro):
        if titulo and roteiro:
            self.model.criar_nova_peca(titulo, roteiro)
        else:
            return False
    def alterar_peca(self, id_peca, titulo, roteiro):
        self.model.alterar_peca(id_peca, titulo, roteiro)

    def retorna_titulo_peca(self, id_peca):
        return self.model.retorna_titulo_peca(id_peca)[0][0]

    def retorna_botoes_pecas(self, peca):

        return ft.Container(
            ft.OutlinedButton(
                width=200,
                height=40,
                on_click = lambda e: self.abrir_peca(peca),
                text=f"{peca[1]}",
                style=ft.ButtonStyle(
                    side={ft.ControlState.DEFAULT: ft.BorderSide(2, ft.colors.BLACK)},
                    shape={ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=5)},
                    bgcolor=ft.colors.WHITE,
                    color=ft.colors.BLACK,
                    ),
            ),
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=10)
        )
    
    def abrir_peca(self, peca):
        self.peca_atual = peca
        self.page.go("/peca")

    def retorna_peca(self, id_peca):
        return self.model.retorna_peca(id_peca)

    def retorna_pecas(self):
        return self.model.retorna_pecas()
    def deletar_peca(self, id_peca):
        self.model.deletar_peca(id_peca)