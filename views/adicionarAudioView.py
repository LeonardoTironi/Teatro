import flet as ft
from flet import Page, View, Column, Container, TextField, OutlinedButton, alignment, margin, Row, UserControl
import sounddevice as sd

class AudioView(UserControl):
    def __init__(self, page: Page, controller):
        super().__init__()
        self.page = page
        self.controller = controller
        self.titulo = TextField(label="Nome", width=page.window.width * 0.8)  
        self.tempo = TextField(label="Tempo", multiline=True, width=280, height=280, value=5,keyboard_type= ft.KeyboardType.NUMBER)

    def retornaNovoAudioView(self, peca):
        return View(
            "/adiciona_audio",
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
                            self.tempo,
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
                                        on_click=lambda e: self.comecar_gravacao(peca),
                                        text="Gravar",
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
                                        on_click=lambda e: e.page.go("/audios"),
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
    
    def comecar_gravacao(self, peca):
        titulo = self.titulo.value
        freq = 44100
        duracao = float(self.tempo.value)
        gravacao = sd.rec(int(duracao*freq), samplerate=freq, channels=2)
        sd.wait()
        self.controller.adicionar_audio(titulo, peca[0], gravacao)
        
        self.page.go("/audios")