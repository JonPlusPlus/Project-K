from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.clearcolor = (0.98, 0.98, 1, 1)


class SliderToInput(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        cx = Window.width / 2

        # TextInput(...) pos=(..., Window.height-60): top-centered input displays numeric value.
        self.inp = TextInput(text='0', size_hint=(None,None),width=120, height=40,pos=(cx - 60, Window.height - 60))
        self.add_widget(self.inp)

        # Slider(min=0, max=200, pos=(..., Window.height-120)): slider below the input.
        self.s = Slider(min=0, max=200, value=0,size_hint=(None,None), width=300, height=40,pos=(cx - 150, Window.height - 120))
        # bind(value=self.on_val): calls on_val on changes.
        self.s.bind(value=self.on_val)
        self.add_widget(self.s)

    # on_val(): sets TextInput.text to the integer slider value.
    def on_val(self, inst, v):
        self.inp.text = str(int(v))


class SliderApp(App):
    def build(self):
        return SliderToInput()


if __name__ == '__main__':
    SliderApp().run()




