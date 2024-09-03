import flet as ft
from flet import Page, View, Column, Container, TextField, OutlinedButton, alignment, margin, Row, UserControl

class EditarAnotacao(UserControl):
    def __init__(self, page: Page, controller, anotacao):
        super().__init__()
        self.page = page
        self.controller = controller
        self.anotacao = anotacao
        self.titulo = TextField(value=anotacao[2], label="Título", width=page.window.width * 0.8)
        self.texto = TextField(value=anotacao[1], label="Texto", multiline=True, width=280, height=280)

    def retornaEditarAnotacaoView(self, anotacao):
        return View(
            "/editar_anotacao",
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
                            self.texto,
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
                                        on_click=lambda e:self.editarAnotacao(anotacao),
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
    
    def editarAnotacao(self, anotacao):
        titulo = self.titulo.value
        texto = self.texto.value
        self.controller.alterar_anotacao(str(anotacao[0]), titulo, texto)
        self.page.go("/anotacoes")