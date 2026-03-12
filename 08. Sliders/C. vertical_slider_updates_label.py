from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.clearcolor = (1, 1, 0.98, 1)


class VerticalSliderFont(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        cx = Window.width / 2

        # Label(...): shows sample text whose font size will change.
        self.sample = Label(text='Sample Text', color=(0,0,0,1),pos=(cx - 60, Window.height - 160))
        self.sample.font_size = 20
        self.add_widget(self.sample)

        # Slider(orientation='vertical', min=10, max=80): vertical slider placed to the right and slightly lower.
        self.vs = Slider(min=10, max=80, value=20, orientation='vertical',size_hint=(None,None), width=40, height=140,pos=(cx + 120, Window.height - 220))
        # bind(value=self.on_font): call on_font when slider moves.
        self.vs.bind(value=self.on_font)
        self.add_widget(self.vs)

    # on_font(): assigns the slider value to label.font_size, changing the text size live.
    def on_font(self, inst, v):
        self.sample.font_size = v


class SliderApp(App):
    def build(self):
        return VerticalSliderFont()


if __name__ == '__main__':
    SliderApp().run()