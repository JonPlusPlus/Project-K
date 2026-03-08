from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class BasicCheckBox(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Label(text='Accept Terms', pos=(20,400)): creates the descriptive label.
        self.lbl = Label(text='Accept Terms', pos=(20, 400))
        self.add_widget(self.lbl)
        # CheckBox(pos=(150,400), active=False): creates an unchecked checkbox.
        self.chk = CheckBox(pos=(150, 400), active=False)
            #   active: sets the initial state of the checkbox.
            #   You can attach a callback using bind(active=callback) to detect state changes.
        # self.add_widget(...): adds widgets to the root widget.
        self.add_widget(self.chk)


class CheckBoxApp(App):
    def build(self):
        return BasicCheckBox()


if __name__ == '__main__':
    CheckBoxApp().run()