from kivy.app import App

from kivy.uix.screenmanager import ScreenManager, Screen

class GerenciarTelas(ScreenManager):
    pass

class TelaMenu(Screen):
    pass

class Tela1(Screen):
    def on_checkbox_Active(self, checkboxInstance, isActive):
        if isActive:
            self.ids.lbl.text ="Atlético MG É CAMPEÃO"
            print("Checkbox Checked")
        else:
            self.ids.lbl.text ="Atlético MG"
            print("Checkbox unchecked")
class Tela2(Screen):
    def __init__(self, atividades=[], **kwargs): #keyword arguments (poderia ser qualquer nome)
        super().__init__(**kwargs)
        for atividades in atividades:
            self.ids.box.add_widget(Funcoes(text=atividades))

    def addComponente(self):
        texto = self.ids.tarefa.text
        self.ids.box.add_widget(Funcoes(text=texto))
        self.ids.tarefa.text = ''   

class Funcoes(Screen):
    def __init__(self,text='',**kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

class Tela(App):
    def build(self):
        return GerenciarTelas()

if __name__ == '__main__':
    Tela().run()