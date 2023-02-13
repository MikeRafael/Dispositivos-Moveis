from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Componentes(BoxLayout):
    def carrega_Progress(self):
            self.ids.pb.value += 10

class Aula7_1(App):
    def build(self):
        return Componentes()

if __name__ == "__main__":
    Aula7_1().run()
