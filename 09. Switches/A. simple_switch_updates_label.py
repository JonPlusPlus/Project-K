from kivy.app import App
from kivy.uix.switch import Switch
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window

# Window.clearcolor = (1,1,1,1): sets a white background.
Window.clearcolor = (1, 1, 1, 1)


class BasicSwitch(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        cx = Window.width / 2
        # Label(...): displays a short message near the top.
        self.lbl = Label(text='Switch', color=(0,0,0,1),pos=(cx - 120, Window.height - 120))
        self.add_widget(self.lbl)
        # Switch(active=False): places the switch beside the label.
        self.sw = Switch(active=False, pos=(cx + 40, Window.height - 135))
            #   active: True if the switch starts ON, False if OFF.
            #   disabled: True to disable interaction.
            #   size_hint, pos: use size_hint=(None,None) and pos for manual placement.
        # add_widget(): adds both widgets to the window.
        self.add_widget(self.sw)


class SwitchApp(App):
    def build(self):
        return BasicSwitch()


if __name__ == '__main__':
    SwitchApp().run()




