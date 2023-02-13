from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class DrawingSpace(RelativeLayout):
    pass

class Aula6_1(App):
    def build(self):
        return DrawingSpace()



if __name__=="__main__":
    Aula6_1().run()
