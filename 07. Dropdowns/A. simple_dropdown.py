from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window

# Window.clearcolor=(1,1,1,1): white background.
Window.clearcolor = (1, 1, 1, 1)  # white background


class TopDropdown(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        center_x = Window.width / 2

        # TextInput(...): displays selected dropdown item.
        self.input = TextInput(text='Select',size_hint=(None,None), width=200, height=40,pos=(center_x - 150, Window.height - 60))
        # add_widget(widget): Adds an item to the dropdown.
        self.add_widget(self.input)

        # DropDown(): container for dropdown items.
        dropdown = DropDown()
            #   auto_width: True to match the width of the widest child.
            #   max_height: Maximum height before scrolling.
            #   dismiss(): Closes the dropdown.
        for val in ['Option 1','Option 2','Option 3']:
            # Button(...): required for interactive dropdown items.
            btn = Button(text=val, size_hint_y=None, height=40)
            # bind(on_select=callback): Executes callback when item is selected.
            # select(value): Programmatically select an item.
            btn.bind(on_release=lambda btn, v=val: dropdown.select(v))
            dropdown.add_widget(btn)

        # mainbtn opens dropdown; on_select updates TextInput.
        mainbtn = Button(text='Choose', size_hint=(None,None), width=100, height=40,pos=(center_x + 60, Window.height - 60))
        mainbtn.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(self.input,'text',x))
        self.add_widget(mainbtn)


class DropdownApp(App):
    def build(self):
        return TopDropdown()


if __name__ == '__main__':
    DropdownApp().run()




