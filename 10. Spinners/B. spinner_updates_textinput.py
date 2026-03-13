from kivy.app import App
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.clearcolor = (0.98, 0.98, 1, 1)


class SpinnerToInput(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        cx = Window.width / 2

        self.inp = TextInput(text='', size_hint=(None, None), width=200, height=40,pos=(cx - 150, Window.height - 60))
        self.add_widget(self.inp)

        self.sp = Spinner(text='Pick', values=('Apple','Banana','Cherry'),size_hint=(None, None), width=150, height=40,pos=(cx + 60, Window.height - 60))
        self.sp.bind(text=lambda inst, v: setattr(self.inp, 'text', v))
        self.add_widget(self.sp)


class SpinnerApp(App):
    def build(self):
        return SpinnerToInput()


if __name__ == '__main__':
    SpinnerApp().run()