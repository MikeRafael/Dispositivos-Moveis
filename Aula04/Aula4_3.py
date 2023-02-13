import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class GerenciarTelas(ScreenManager):
    pass

class TelaMenu(Screen):
    pass

class Tela1(Screen):
    pass
class Tela2(Screen):
    pass

class Aplicativo(App):
    def build(self):
        return GerenciarTelas()

if __name__ == '__main__':
    Aplicativo().run()