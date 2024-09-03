from models.audioModel import AudioModel
from flet import Page
import flet as ft
from playsound import playsound
class AudioController:
    def __init__(self, page:Page):
        self.model = AudioModel()
        self.page=page
    def adicionar_audio(self, texto, id_peca, audio):
        self.model.criar_novo_audio(texto, id_peca, audio)
    def retorna_audios(self, id_peca):
        return self.model.retorna_audios(id_peca)

    def retorna_botoes_audios(self,audio):
        return ft.Container(
            ft.OutlinedButton(
                width=200,
                height=40,
                on_click = lambda e: playsound(audio[1]),
                text=f"{audio[2]}",
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