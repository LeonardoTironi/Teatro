import flet as ft
from flet import Page, View, Column, Container, Text, OutlinedButton, alignment, margin, Row, UserControl

class RoteiroView(UserControl):
    def __init__(self, page: Page, controller, peca):
        super().__init__()
        self.page = page
        self.controller = controller
        self.peca = peca
        
          
    def retornaRoteiroView(self):
        return View(
            f"/roteiro",
            controls=[
                Column(
                    controls=[
                        Column(
                            controls=[
                                Container(
                                    Text(self.peca[1], size=24, weight="bold"),
                                    alignment=alignment.center,
                                    padding=10,
                                    margin=margin.only(top=30)
                                ),
                            ],
                            scroll=ft.ScrollMode.HIDDEN,
                            height=100,
                        ),
                        Column(
                            controls=[
                                Text(self.peca[2], size=16, text_align=ft.TextAlign.JUSTIFY),
                            ],
                            scroll=ft.ScrollMode.HIDDEN,
                            height=300,
                        ),
                        Container(
                            Row(
                                controls=[
                                    OutlinedButton(
                                        width=150,
                                        height=40,
                                        on_click=lambda e: self.page.go(f"/editar_roteiro"),
                                        text="Editar Roteiro",
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
                                        on_click=lambda e: self.page.go(f"/peca"),
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
                    alignment=alignment.center
                )
            ],
        )
    
