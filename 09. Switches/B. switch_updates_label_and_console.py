from kivy.app import App
from kivy.uix.switch import Switch
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.clearcolor = (0.98, 0.98, 1, 1)


class CallbackSwitch(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        cx = Window.width / 2
        # Create a label to show the current state.
        self.lbl = Label(text='Switch is OFF', color=(0,0,0,1),pos=(cx - 120, Window.height - 140))
        self.add_widget(self.lbl)
        # Create a Switch(active=False) and position it slightly lower than the label.
        self.sw = Switch(active=False, pos=(cx + 60, Window.height - 155))
        # Bind the switch to a callback using sw.bind(active=self.on_active).
        self.sw.bind(active=self.on_active)
            #   Common usage: sw.bind(active=callback) -> responds when user toggles the switch. Read the state using sw.active.
        self.add_widget(self.sw)

    # Update the label and print the switch state in the callback.
    def on_active(self, instance, value):
        self.lbl.text = 'Switch is ON' if value else 'Switch is OFF'
        print('Switch state:', 'ON' if value else 'OFF')


class SwitchApp(App):
    def build(self):
        return CallbackSwitch()


if __name__ == '__main__':
    SwitchApp().run()