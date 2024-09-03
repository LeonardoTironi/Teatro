import flet as ft
from flet import Page, View, Column, Container, TextField, OutlinedButton, alignment, margin, Row, UserControl

class EditarPeca(UserControl):
    def __init__(self, page: Page, controller, peca):
        super().__init__()
        self.page = page
        self.controller = controller
        self.peca=peca
        self.titulo = TextField(value=peca[1], label="Título", width=page.window.width * 0.8) 
        
        self.roteiro = TextField(value=peca[2], label="Roteiro", multiline=True, width=280, height=280)
    def retornaEditarPecaPage(self):
        return View(
            "/adicionar_peca",
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
                            self.roteiro,
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
                                        on_click=self.alterarPeca,
                                        text="Salvar",
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
                                        on_click=lambda e: e.page.go("/peca"),
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
    
    def alterarPeca(self, e):
        titulo = self.titulo.value
        roteiro = self.roteiro.value
        self.controller.alterar_peca(str(self.peca[0]),titulo, roteiro)
        self.page.go("/home")