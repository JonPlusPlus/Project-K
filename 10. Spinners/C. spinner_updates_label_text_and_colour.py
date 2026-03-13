from kivy.app import App
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.clearcolor = (1, 1, 0.98, 1)


class SpinnerColor(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        cx = Window.width / 2

        self.lbl = Label(text='Color: None', color=(0,0,0,1),pos=(cx - 80, Window.height - 120))
        self.add_widget(self.lbl)

        self.sp = Spinner(text='Color', values=('Red','Green','Blue'),size_hint=(None, None), width=150, height=40,pos=(cx + 60, Window.height - 120))
        # bind(text=self.on_pick): connects spinner changes to the callback.
        self.sp.bind(text=self.on_pick)
        self.add_widget(self.sp)

    # on_pick(self, inst, val): a callback function triggered on spinner selection.
    def on_pick(self, inst, val):
        # cmap: maps color names to RGBA values.
        cmap = {'Red': (1,0,0,1), 'Green': (0,0.6,0,1), 'Blue': (0,0,1,1)}
        # lbl.text and lbl.color update the label’s text and color dynamically.
        self.lbl.text = f'Color: {val}'
        self.lbl.color = cmap.get(val, (0,0,0,1))


class SpinnerApp(App):
    def build(self):
        return SpinnerColor()


if __name__ == '__main__':
    SpinnerApp().run()