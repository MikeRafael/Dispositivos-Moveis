from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

class Componentes(BoxLayout):
    def gera_intervalo(self):
        Clock.schedule_interval(self.next, 1 / 25)

    def next(self, dt):
        if self.ids.pb.value >= 100:
            return False
        self.ids.pb.value += 1

class Aula7_2(App):
    def build(self):
        return Componentes()

if __name__ == "__main__":
    Aula7_2().run()
