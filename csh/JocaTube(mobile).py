#pip install "kivy[base]" kivy_examples --pre --extra-index-url https://kivy.org/downloads/simple\
#https://youtube.com/playlist?list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&si=84kpTAY3Bjqp-w1I

# Importa bibliotecas kivy que faz o GUI
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.config import Config

# Importa bibliotecas necessárias para download dos videos
from pytubefix import YouTube
from pytubefix.cli import on_progress

import threading
from kivy.uix.filechooser import FileChooserIconView

# Define o tema do Kivy

kivy.Config.set('kivy', 'exit_on_escape', '1')
kivy.Config.set('graphics', 'width', '600')
kivy.Config.set('graphics', 'height', '800')

# Configurações do Kivy para permitir download de videos

Config.set('kivy', 'video', {'driver': 'ffpyplayer'})
Config.set('kivy', 'audio', {'driver':'sdl2'})







    
# Load the GUI from the KV file
GUI = Builder.load_file("tela.kv")

#Classe da grid, onde fica os botoes e labels e pa
class MeuGrid(Widget):
    #funções da grid, aqui vou colocar as funcoes pro download do pytube
    link = ObjectProperty(None)
    label1 = ObjectProperty(None)


     
        
     
    def fufuque(self):
        link = self.link.text
        yt = YouTube(link)
        video = yt.streams.get_highest_resolution()
        video.download()

    # thread
    thread = threading.Thread(target=fufuque)
    thread.start()
    

       



class MeuApp(App):
    def build(self):
        return MeuGrid()

if __name__ == "__main__":
    MeuApp().run()




#código de fazer download: