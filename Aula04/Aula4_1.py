from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Componentes(Screen):
    def on_checkbox_Active(self, checkboxInstance, isActive):
        if isActive:
            self.ids.lbl.text ="Checkbox is ON"
            print("Checkbox Checked")
        else:
            self.ids.lbl.text ="Checkbox is OFF"
            print("Checkbox unchecked")


class Atividades(Screen):
    def __init__(self, atividades=[], **kwargs): #keyword arguments (poderia ser qualquer nome)
        super().__init__(**kwargs)

class Funcoes(BoxLayout):
    def __init__(self,text='',**kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

class Aula4_1(App):
    def build(self):
        return Gerenciador()

if __name__ == '__main__':
    Aula4_1().run()
