# pip install ffpyplayer
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Componentes(BoxLayout):
    pass

class Aula7_5(App):
    def build(self):
        return Componentes()

if __name__ == "__main__":
    Aula7_5().run()
