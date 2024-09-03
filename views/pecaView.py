import flet as ft
from flet import UserControl, Page, Column, Container, OutlinedButton, alignment, margin, Row

class PecaView(UserControl):
    def __init__(self, page: Page, controller, peca):
        super().__init__()
        self.page = page
        self.controller = controller
        self.peca = peca
    
    def retornaPecaView(self):
        return ft.View(
            "/peca",
            controls=[
                Column(
                    controls=[
                        Column(
                            controls=[
                                ft.Container(
                                    ft.Text(self.peca[1], size=24, weight="bold"),
                                    alignment=alignment.center,
                                    padding=10,
                                    margin=margin.only(top=30)
                                ),
                            ],
                            scroll=ft.ScrollMode.HIDDEN,
                            height=100,
                            
                        ),
                        Container(
                            Column(
                                controls=[
                                    OutlinedButton(
                                        width=150,
                                        height=40,
                                        on_click=lambda e: self.page.go(f"/roteiro"),
                                        text="Roteiro",
                                        style=ft.ButtonStyle(
                                            side={ft.ControlState.DEFAULT: ft.BorderSide(2, ft.colors.BLACK)},
                                            shape={ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=5)},
                                            bgcolor=ft.colors.WHITE,
                                            color=ft.colors.BLACK,
                                        ),
                                    ),
                                    OutlinedButton(
                                        width=150,
                                        height=40,
                                        on_click=lambda e: self.page.go(f"/anotacoes"),
                                        text="Ver Anotações",
                                        style=ft.ButtonStyle(
                                            side={ft.ControlState.DEFAULT: ft.BorderSide(2, ft.colors.BLACK)},
                                            shape={ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=5)},
                                            bgcolor=ft.colors.WHITE,
                                            color=ft.colors.BLACK,
                                        ),
                                    ),
                                    OutlinedButton(
                                        width=150,
                                        height=40,
                                        on_click=lambda e: self.page.go(f"/audios"),
                                        text="Ver Áudios",
                                        style=ft.ButtonStyle(
                                            side={ft.ControlState.DEFAULT: ft.BorderSide(2, ft.colors.BLACK)},
                                            shape={ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=5)},
                                            bgcolor=ft.colors.WHITE,
                                            color=ft.colors.BLACK,
                                        ),
                                    ),
                                    OutlinedButton(
                                        width=150,
                                        height=40,
                                        on_click=self.deletePeca,
                                        text="Deletar Peça",
                                        style=ft.ButtonStyle(
                                            side={ft.ControlState.DEFAULT: ft.BorderSide(2, ft.colors.RED)},
                                            shape={ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=5)},
                                            bgcolor=ft.colors.WHITE,
                                            color=ft.colors.RED,
                                        ),
                                    ),
                                    
                                ],
                                alignment=alignment.center,
                                spacing=10
                            ),
                            alignment=alignment.center,
                            padding=10,
                            margin=margin.only(top=30)
                        )
                    ]

                ),
                Container(
                    Column(
                        controls=[
                            OutlinedButton(
                                width=150,
                                height=40,
                                on_click=lambda e: e.page.go("/home"),
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
    def deletePeca(self, e):
        self.controller.deletar_peca(str(self.peca[0]))
        self.page.go("/home")