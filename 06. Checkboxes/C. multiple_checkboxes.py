from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class MultiCheckBox(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        options = ['Option 1', 'Option 2', 'Option 3']
        y = 300
        # Loop over options to create labels and checkboxes.
        for opt in options:
            # pos=(x,y): sets positions manually on the window.
            lbl = Label(text=opt, pos=(100, y))
            # active=False: all checkboxes start unchecked.
            chk = CheckBox(pos=(250, y), active=False)
            # self.add_widget(...): adds labels and checkboxes to the widget.
            self.add_widget(lbl)
            self.add_widget(chk)
            y -= 50


class CheckBoxApp(App):
    def build(self):
        return MultiCheckBox()


if __name__ == '__main__':
    CheckBoxApp().run()