from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text='fist name'))
        self.fist_name = TextInput(multiline= False)
        self.inside.add_widget(self.fist_name)

        self.inside.add_widget(Label(text='middle name'))
        self.middle_name = TextInput(multiline=False)
        self.inside.add_widget(self.middle_name)
        self.add_widget(self.inside)

        self.submit = Button(text = "submit", font_size= 40)
        self.submit.bind(on_press= self.pressed)
        self.add_widget(self.submit)
    def pressed(self, instance):
        fist_name = self.fist_name.text
        middle_name = self.middle_name.text
        # print('fist_name', fist_name, 'middle_name', middle_name)
        self.fist_name.text = ''
        self.middle_name.text = ''



class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()