from kivy.app import App
from kivy.uix.switch import Switch
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)


class BgToggleSwitch(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        cx = Window.width / 2
        # Display a label showing current background color.
        self.lbl = Label(text='Background: White', color=(0,0,0,1),pos=(cx - 160, Window.height - 140))
        self.add_widget(self.lbl)
        # Create a switch below and bind it to toggle_bg().
        self.sw = Switch(active=False, pos=(cx + 60, Window.height - 155))
        self.sw.bind(active=self.toggle_bg)
        self.add_widget(self.sw)

    # When toggled ON, background changes to green; when OFF, returns to white.
    def toggle_bg(self, instance, value):
        # Label text updates accordingly.
        if value:
            Window.clearcolor = (0.88, 1, 0.88, 1)
            self.lbl.text = 'Background: Light Green'
        else:
            Window.clearcolor = (1, 1, 1, 1)
            self.lbl.text = 'Background: White'


class SwitchApp(App):
    def build(self):
        return BgToggleSwitch()


if __name__ == '__main__':
    SwitchApp().run()