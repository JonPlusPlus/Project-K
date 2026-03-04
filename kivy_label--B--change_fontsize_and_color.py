import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.11.1')


class B(App):
    def build(self):
        # font_size='24sp': increases the label text size (use sp for scalable units).
        # color=(r,g,b,a): RGBA tuple with values from 0 to 1; here it makes the text bluish.
        # The Label is centered by default in a bare app window.
        return Label(text='Style Label', font_size='24sp', color=(0.2, 0.6, 0.9, 1))


B().run()
