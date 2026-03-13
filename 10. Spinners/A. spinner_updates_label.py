from kivy.app import App
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window

# Window.clearcolor = (1,1,1,1): set a white background.
Window.clearcolor = (1, 1, 1, 1)


class BasicSpinner(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        cx = Window.width / 2
        # Label(...) pos=(...): top label to display the current selection.
        self.lbl = Label(text='Selected: None', color=(0,0,0,1),pos=(cx - 60, Window.height - 120))
        self.add_widget(self.lbl)

        # Spinner(text=..., values=...) pos=(...): top spinner placed below the label.
        self.sp = Spinner(text='Choose', values=('One', 'Two', 'Three'),size_hint=(None, None), width=150, height=40,pos=(cx - 75, Window.height - 160))
            #   text: text shown when no selection change (or current value).
            #   values: tuple/list of selectable values.
            #   size_hint/width/height: set to None for manual placement.
            #   background_color: spinner background rgba.
        # sp.bind(text=...): update label when the spinner selection changes.
        self.sp.bind(text=lambda inst, val: setattr(self.lbl, 'text', f'Selected: {val}'))
        self.add_widget(self.sp)


class SpinnerApp(App):
    def build(self):
        return BasicSpinner()


if __name__ == '__main__':
    SpinnerApp().run()