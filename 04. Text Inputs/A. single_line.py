from kivy.app import App
from kivy.uix.textinput import TextInput


class A(App):
    def build(self):
        # TextInput(text='Type here', multiline=False): creates a single - line editable text box.
        # return TextInput(...): shows the text box as the app’s root widget.
        return TextInput(text='Type here', multiline=False)


if __name__ == '__main__':
    A().run()