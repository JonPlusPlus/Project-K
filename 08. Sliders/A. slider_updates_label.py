from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window

# Window.clearcolor = (1,1,1,1): set a white background for visibility.
Window.clearcolor = (1, 1, 1, 1)


class BasicSlider(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        cx = Window.width / 2

        # Label(...) pos=(...): place a label near the top to show the slider value.
        self.lbl = Label(text='Value: 0', color=(0,0,0,1),pos=(cx - 40, Window.height - 120))
        self.add_widget(self.lbl)

        # Slider(min=0, max=100, value=0, pos=(...)): horizontal slider placed just below the label.
        self.s = Slider(min=0, max=100, value=0,size_hint=(None, None), width=300, height=40,pos=(cx - 150, Window.height - 160))
            #   min/max: numeric range for the slider.
            #   value: initial value (within [min, max]).
            #   step: set step size (e.g., step=1) for discrete values.
            #   orientation: 'horizontal' (default) or 'vertical'.
            #   size_hint/width/height: use size_hint=(None,None) + width/height for manual placement.
        # bind(value=self.on_value): call on_value whenever slider moves.
        # on_value(): updates the label text with the integer slider value.
        self.s.bind(value=self.on_value)
            #   Common methods / events: bind(value=callback), read .value, set .value programmatically.
        self.add_widget(self.s)

    def on_value(self, inst, val):
        self.lbl.text = f'Value: {int(val)}'


class SliderApp(App):
    def build(self):
        return BasicSlider()


if __name__ == '__main__':
    SliderApp().run()


