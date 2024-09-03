import flet as ft
from flet import Page, View, Column, Container, TextField, OutlinedButton, alignment, margin, Row, UserControl

class NovaAnotacao(UserControl):
    def __init__(self, page: Page, controller):
        super().__init__()
        self.page = page
        self.controller = controller
        self.titulo = TextField(label="Título", width=page.window.width * 0.8) 
        
        self.anotacao = TextField(label="Texto", multiline=True, width=280, height=280)
    def retornaNovaAnotacaoView(self, peca):
        
        return View(
            "/adiciona_anotacao",
            controls=[
                Column(
                    controls=[
                        Container(
                            self.titulo,
                            alignment=alignment.center,
                            padding=10,
                            margin=margin.only(top=30)
                        ),
                        Container(
                            self.anotacao,
                            alignment=alignment.center,
                            padding=10,
                            margin=margin.only(top=30)
                        ),
                        Container(
                            Row(
                                controls=[
                                    OutlinedButton(
                                        width=None,
                                        height=40,
                                        on_click=lambda e: self.adicionarNovaAnotacao(peca),
                                        text="Adicionar Anotação",
                                        style=ft.ButtonStyle(
                                            side={ft.ControlState.DEFAULT: ft.BorderSide(2, ft.colors.BLACK)},
                                            shape={ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=5)},
                                            bgcolor=ft.colors.WHITE,
                                            color=ft.colors.BLACK,
                                        ),
                                        expand=True
                                    ),
                                    OutlinedButton(
                                        width=None,
                                        height=40,
                                        on_click=lambda e: e.page.go("/anotacoes"),
                                        text="Voltar",
                                        style=ft.ButtonStyle(
                                            side={ft.ControlState.DEFAULT: ft.BorderSide(2, ft.colors.BLACK)},
                                            shape={ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=5)},
                                            bgcolor=ft.colors.WHITE,
                                            color=ft.colors.BLACK,
                                        ),
                                        expand=True
                                    )
                                ],
                                alignment=alignment.center,
                                spacing=10,
                                expand=True
                            ),
                            alignment=alignment.center,
                            padding=10,
                            margin=margin.only(top=30)
                        )
                    ],
                    alignment=alignment.center
                )
            ],
        )
    
    def adicionarNovaAnotacao(self, peca):
        titulo = self.titulo.value
        anotacao = self.anotacao.value
        self.controller.adicionar_anotacao(str(peca[0]),titulo, anotacao)
        self.page.go("/anotacoes")