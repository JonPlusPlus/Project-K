import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.11.1')


class B(App):
    def build(self):
        return Label(text='Style Label', font_size='24sp', color=(0.2, 0.6, 0.9, 1))


B().run()
