from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class CallbackCheckBox(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lbl = Label(text='Checkbox is OFF', pos=(100, 250))
        self.add_widget(self.lbl)
        self.chk = CheckBox(pos=(100, 200), active=False)
        # bind(active=self.on_checkbox_active): triggers the callback when the checkbox state changes.
        # on_checkbox_active(): updates the label and prints the state.
        self.chk.bind(active=self.on_checkbox_active)
        self.add_widget(self.chk)

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.lbl.text = 'Checkbox is ON'
            print('Checkbox Checked')
        else:
            self.lbl.text = 'Checkbox is OFF'
            print('Checkbox Unchecked')


class CheckBoxApp(App):
    def build(self):   return CallbackCheckBox()


if __name__ == '__main__':
    CheckBoxApp().run()