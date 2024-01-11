import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
#kivy.require('1.9.0')

class MyRoot(FloatLayout):

    def __init__(self):
        super(MyRoot,self).__init__()

    def generate_text(self):
        
        self.random_label.text = str("JHGJHKUKJILUZ")
        


class MyGrow(App):

    def build(self):
        print(Window.size)
        return MyRoot()
    

Th = MyGrow()
Th.run()


