import flet as ft
from flet import Page, View, Column, Container, Text, alignment, OutlinedButton, UserControl, ListView, margin

class Home(UserControl):
    def __init__(self, page:Page, controller):
        super().__init__()
        self.lista_pecas = ListView(expand=True, spacing=10)
        self.controller = controller
    def retornaHomePage(self):
        self.atualizarListaPecas()
        return View(
            "/home",
            controls=[
                Column(
                    controls=[
                        Container(
                                OutlinedButton(
                                            width=200,
                                            height=40,
                                            on_click= lambda e: e.page.go("/adicionar_peca"),
                                            text="Nova Peça",
                                            style=ft.ButtonStyle(
                                                side={ft.ControlState.DEFAULT: ft.BorderSide(2, ft.colors.BLACK)},
                                                shape={ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=5)},
                                                bgcolor=ft.colors.WHITE,
                                                color=ft.colors.BLACK,
                                            ),
                                ),
                                alignment=alignment.center,
                                padding=10,
                                margin=margin.only(top=30)
                        )
                    ]
                ),
                self.lista_pecas,
                
            ],
        )
    #Exemplo
    def atualizarListaPecas(self):
        self.lista_pecas.controls.clear() #Usar algo como botão ou gesture detector
        pecas = self.controller.retorna_pecas()
        
        for peca in pecas:
            self.lista_pecas.controls.append(self.controller.retorna_botoes_pecas(peca))
