from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Atividades(Screen):
    def __init__(self, atividades=[], **kwargs): #keyword arguments (poderia ser qualquer nome)
        super(Atividades,self).__init__(**kwargs)
        for atividades in atividades:
            self.ids.box.add_widget(Funcoes(text=atividades))

    #def on_enter()
    def on_pre_enter(self):
        Window.bind(on_keyboard= self.retorno)

    def retorno(self,window,key,*args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
        #print(key)
        return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard = self.retorno)

    def addComponente(self):
        texto = self.ids.tarefa.text
        self.ids.box.add_widget(Funcoes(text=texto))
        self.ids.tarefa.text = ''

class Funcoes(BoxLayout):
    def __init__(self,text='',**kwargs):
        super(Atividades, self).__init__(**kwargs)
        self.ids.label.text = text

class Aula5_3(App):
    def build(self):
        return Gerenciador()

if __name__ == '__main__':
    Aula5_3().run()
