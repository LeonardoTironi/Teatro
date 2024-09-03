import flet as ft
from flet import UserControl, Page, Column, Container, OutlinedButton, alignment, margin, Row

class AudiosView(UserControl):
    def __init__(self, page:Page, controller):
        super().__init__()
        self.page=page
        self.lista_audio = ft.ListView(expand=True, spacing=10)
        self.controller = controller
    def retornaAudiosView(self, peca):
        self.atualizarAnotacoes(peca)
        return ft.View(
            "/audios",
            controls=[
                Column(
                    controls=[
                        Container(
                                OutlinedButton(
                                            width=200,
                                            height=40,
                                            on_click= lambda e: e.page.go("/adicionar_audio"),
                                            text="Novo Áudio",
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
                self.lista_audio,
                Container(
                    Column(
                        controls=[
                            OutlinedButton(
                                width=150,
                                height=40,
                                on_click=lambda e: e.page.go("/peca"),
                                text="Voltar",
                                style=ft.ButtonStyle(
                                    side={ft.ControlState.DEFAULT: ft.BorderSide(2, ft.colors.BLACK)},
                                    shape={ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=5)},
                                    bgcolor=ft.colors.WHITE,
                                    color=ft.colors.BLACK,
                                ),
                            )
                        ],
                        alignment=alignment.center,
                        spacing=10
                    ),
                    alignment=alignment.center,
                    padding=10,
                    margin=margin.only(top=30)
                )
            ],
        )
    #Exemplo
    def atualizarAnotacoes(self, peca):
        self.lista_audio.controls.clear()
        audios = self.controller.retorna_audios(peca[0])
        if audios:
            for audio in audios:
                self.lista_audio.controls.append(self.controller.retorna_botoes_audios(audio))
