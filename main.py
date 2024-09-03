import flet as ft
from flet import UserControl, Page, Container, OutlinedButton, alignment

#Páginas
from views.home import Home
from views.pecaView import PecaView
from views.adicionarPecaView import NovaPeca
from views.roteiroView import RoteiroView
from views.editarPecaView import EditarPeca
from views.anotacoesView import AnotacoesView
from views.adicionaAnotacaoView import NovaAnotacao
from views.anotacaoView import AnotacaoView
from views.editarAnotacaoView import EditarAnotacao
from views.audiosViews import AudiosView
from views.adicionarAudioView import AudioView
#Controllers
from controllers.pecaController import PecaController
from controllers.anotacaoController import AnotacaoController
from controllers.audioController import AudioController
def main(page:Page):
    page.title="De Cor"

    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 360
    page.window.height = 640

    #Controllers
    peca_Controller = PecaController(page)
    anotacao_Controller = AnotacaoController(page)
    audio_Controller = AudioController(page)


    home = Home(page, peca_Controller)


    def route_change(route):
        page.views.clear()

        #Peças
        if page.route=="/home" or page.route=="/": #Finalizado
            page.views.append(home.retornaHomePage())
        if page.route=="/peca": 
            pecaTela = PecaView(page, peca_Controller, peca_Controller.peca_atual)
            page.views.append(pecaTela.retornaPecaView())
        if page.route=="/adicionar_peca": #Finalizado
            adicionarPeca_Tela=NovaPeca(page, peca_Controller)
            page.views.append(adicionarPeca_Tela.retornaNovaPecaPage())
        
        #Roteiros
        if page.route=="/roteiro":
            roteiro_View_Tela=RoteiroView(page, peca_Controller, peca_Controller.peca_atual)
            page.views.append(roteiro_View_Tela.retornaRoteiroView())
        if page.route=="/editar_roteiro":
            editarRoteiro_View=EditarPeca(page, peca_Controller, peca_Controller.peca_atual)
            page.views.append(editarRoteiro_View.retornaEditarPecaPage())
        
        #Anotações
        if page.route=="/anotacoes":
            anotacoesTela = AnotacoesView(page, anotacao_Controller)
            page.views.append(anotacoesTela.retornaAnotacoesView(peca_Controller.peca_atual))
        if page.route=="/adicionar_anotacao":
            novaAnotacaoTela = NovaAnotacao(page, anotacao_Controller)
            page.views.append(novaAnotacaoTela.retornaNovaAnotacaoView(peca_Controller.peca_atual))
        if page.route=="/anotacao":
            verAnotacaoTela = AnotacaoView(page, anotacao_Controller, anotacao_Controller.anotacao_atual)
            page.views.append(verAnotacaoTela.retornaAnotacaoView())
        if page.route=="/editar_anotacao":
            editarAnotacaoTela = EditarAnotacao(page, anotacao_Controller, anotacao_Controller.anotacao_atual)
            page.views.append(editarAnotacaoTela.retornaEditarAnotacaoView(anotacao_Controller.anotacao_atual))

        if page.route=="/audios":
            audiosTela = AudiosView(page, audio_Controller)
            page.views.append(audiosTela.retornaAudiosView(peca_Controller.peca_atual))
        if page.route=="/adicionar_audio":
            audioTela = AudioView(page, audio_Controller)
            page.views.append(audioTela.retornaNovoAudioView(peca_Controller.peca_atual))
        
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.update()


if __name__=="__main__":
    ft.app(target=main)