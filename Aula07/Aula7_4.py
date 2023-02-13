from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Componentes(BoxLayout):
    def gera_intervalo(self):
        self.ids.pb.value =  self.ids.sl.value

class Aula7_4(App):
    def build(self):
        return Componentes()

if __name__ == "__main__":
    Aula7_4().run()
