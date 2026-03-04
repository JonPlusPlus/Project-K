import kivy
from kivy.app import App
from kivy.uix.label import Label


kivy.require('1.11.1')

class A(App):
    def build(selfself):
        return Label(text='Hello Kivy')

A().run()

