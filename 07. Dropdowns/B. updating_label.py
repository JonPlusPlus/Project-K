from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.clearcolor = (0.95, 0.95, 0.95, 1)


class DropdownLabelExample(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        center_x = Window.width / 2

        # Label shows which color was chosen.
        self.lbl = Label(text='Selected: None', color=(0, 0, 0, 1),pos=(center_x - 50, Window.height - 140))
        self.add_widget(self.lbl)

        # DropDown() holds the selectable color buttons.
        dropdown = DropDown()
        for val in ['Red', 'Green', 'Blue']:
            btn = Button(text=val, size_hint_y=None, height=40)
            # When an option is chosen, dropdown.select() triggers on_select.
            btn.bind(on_release=lambda btn, v=val: dropdown.select(v))
            # Each button is added to dropdown with add_widget().
            dropdown.add_widget(btn)

        mainbtn = Button(text='Select Color', size_hint=(None, None), width=120, height=40,pos=(center_x - 60, Window.height - 190))
        mainbtn.bind(on_release=dropdown.open)

        # The label text is updated dynamically.
        dropdown.bind(on_select=lambda instance, x: setattr(self.lbl, 'text', f'Selected: {x}'))
        self.add_widget(mainbtn)


class DropdownApp(App):
    def build(self):
        return DropdownLabelExample()


if __name__ == '__main__':
    DropdownApp().run()