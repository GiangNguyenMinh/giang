from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.app import App


class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.stop = Button(text='stop ')
        # self.stop.pos_hint = {'x': self.width//2, 'y':0}
        # self.stop.size_hint = (0.2, 0.1)
        self.add_widget(self.stop)
        self.inside = BoxLayout()
        self.inside.orientation = 'horizontal'
        self.add_widget(self.inside)
        self.inside.pos_hint = {'x':0, 'y':self.width}
        self.inside.size_hint =(1, 0.1)
        self.summit = Button(text='start')
        # self.summit.pos_hint = {'x':0, 'y':10}
        # self.summit.size_hint = (0.5, 2)
        self.inside.add_widget(self.summit)







class MyApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    MyApp().run()
