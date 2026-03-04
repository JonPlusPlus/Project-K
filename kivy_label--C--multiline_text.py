import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.11.1')


class C(App):
    def build(self):
        return Label(
            # text contains \n to create multiple lines.
            text='Label one\nLine two\nLine three',
            # font_size controls appearance.
            font_size='18sp',
            #halign='center' centers text horizontally; valign='middle' centers vertically within the text_size area.
            halign='center',
            valign='middle',
            # text_size=(300, None) gives the label a fixed wrapping width so halign can center lines.
            text_size=(300, None)
        )


C().run()
