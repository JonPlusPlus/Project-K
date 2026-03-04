import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.11.1')

# class A(App) define the app class (inherits App).
class A(App):
    # build() returns the widget to display (a Label with text).
    def build(selfself):
        return Label(text='Hello Kivy')


# A().run() create and run the app; Kivy opens a window and shows the label.
A().run()
