from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.clearcolor = (0.9, 0.9, 1, 1)


class DropdownTextInputExample(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        center_x = Window.width / 2

        # TextInput displays the selected fruit.
        self.input = TextInput(text='', size_hint=(None,None), width=200, height=40,pos=(center_x - 150, Window.height - 60))
        self.add_widget(self.input)

        # DropDown() manages the fruit options.
        dropdown = DropDown()
        # Each fruit button is added manually.
        for val in ['Apple', 'Banana', 'Cherry']:
            btn = Button(text=val, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn, v=val: dropdown.select(v))
            dropdown.add_widget(btn)

        # Clicking “Select Fruit” opens the dropdown.
        mainbtn = Button(text='Select Fruit', size_hint=(None,None), width=120, height=40,pos=(center_x + 60, Window.height - 60))
        mainbtn.bind(on_release=dropdown.open)
        # On selection, chosen fruit name is shown in the TextInput.
        dropdown.bind(on_select=lambda instance, x: setattr(self.input, 'text', x))
        self.add_widget(mainbtn)


class DropdownApp(App):
    def build(self):
        return DropdownTextInputExample()


if __name__ == '__main__':
    DropdownApp().run()