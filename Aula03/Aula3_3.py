from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Atividades(Screen):
    def __init__(self, atividades=[], **kwargs): #keyword arguments (poderia ser qualquer nome)
        super().__init__(**kwargs)
        for atividades in atividades:
            self.ids.box.add_widget(Funcoes(text=atividades))

    def addComponente(self):
        texto = self.ids.tarefa.text
        self.ids.box.add_widget(Funcoes(text=texto))
        self.ids.tarefa.text = ''

class Funcoes(BoxLayout):
    def __init__(self,text='',**kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

class Aula3_3(App):
    def build(self):
        return Gerenciador()

if __name__ == '__main__':
    Aula3_3().run()
