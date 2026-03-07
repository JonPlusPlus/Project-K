import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.11.1')

class D(App):
    def build(self):
        return Label(
            # [b]...[/b] makes text bold; [color=RRGGBB]...[/color] sets text color (hex).
            text='[b]Bold[/b] and [color=ff3333]Red[/color] text',
            # markup=True tells Kivy to parse BBCode-like tags.
            markup=True,
            # font_size adjusts overall size.
            font_size='20sp'
        )


D().run()
