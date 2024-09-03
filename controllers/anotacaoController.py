from models.anotacaoModel import AnotacaoModel
from flet import Page
import flet as ft
class AnotacaoController:
    def __init__(self, page:Page):
        self.model = AnotacaoModel()
        self.page = page

    def adicionar_anotacao(self, id_peca, titulo, conteudo):
        self.model.adicionar_nova_anotacao(id_peca, titulo, conteudo)

    def alterar_anotacao(self, id_anotacao, titulo, conteudo):
        self.model.altera_anotacao(id_anotacao, titulo, conteudo)

    def retornar_anotacoes(self, id_peca):
        return self.model.retorna_anotacoes(str(id_peca))
    
    def retorna_anotacao(self, id_anotacao):
        return self.model.retorna_anotacao(id_anotacao)
    
    def retorna_botoes_anotacoes(self, anotacao):
        return ft.Container(
            ft.OutlinedButton(
                width=200,
                height=40,
                on_click = lambda e: self.abrir_anotacao(anotacao),
                text=f"{anotacao[2]}",
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
    def abrir_anotacao(self, anotacao):
        self.anotacao_atual = anotacao
        self.page.go("/anotacao")